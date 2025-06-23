import re
import os
import sys
import argparse
import csv
from io import StringIO
import chardet

def detect_csv_format(file_path, sample_size=8192):
    """
    Analyze a CSV file to detect delimiter, line ending, and quoting characters
    
    Args:
        file_path: Path to the CSV file
        sample_size: Number of bytes to sample from the beginning of the file
    
    Returns:
        dict: Contains detected delimiter, line ending, and quoting character
    """
    # Read a sample of the file to detect characteristics
    with open(file_path, 'rb') as f:
        raw_sample = f.read(sample_size)
    
    # Detect encoding
    result = chardet.detect(raw_sample)
    encoding = result['encoding'] or 'utf-8'
    
    # Convert sample to string using detected encoding
    try:
        sample = raw_sample.decode(encoding)
    except UnicodeDecodeError:
        # Fallback to utf-8 if detection fails
        sample = raw_sample.decode('utf-8', errors='replace')
    
    # Detect line endings
    line_ending = '\r\n' if '\r\n' in sample else '\n'
    
    # Count potential delimiters
    delimiters = [',', ';', '\t', '|']
    counts = {d: sample.count(d) for d in delimiters}
    
    # Choose delimiter with highest count
    delimiter = max(delimiters, key=lambda d: counts[d])
    
    # Check if values appear to be quoted
    lines = sample.split(line_ending)
    if len(lines) > 1:
        # Check first data line (skipping header)
        if '"' in lines[1]:
            quote_char = '"'
        elif "'" in lines[1]:
            quote_char = "'"
        else:
            quote_char = '"'  # Default
    else:
        quote_char = '"'  # Default
    
    # Check for escape character by looking for escaped quotes
    escape_char = '"' if f'{quote_char}{quote_char}' in sample else '\\'
    
    # Create final mapping for MySQL syntax
    line_term = '\\r\\n' if line_ending == '\r\n' else '\\n'
    
    return {
        'delimiter': delimiter,
        'line_terminator': line_term,
        'quote_char': quote_char,
        'escape_char': escape_char,
        'encoding': encoding
    }

def parse_create_table_statement(sql_text):
    """Extract table name and column definitions from CREATE TABLE statement"""
    # Extract table name
    table_match = re.search(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?[`"]?([^`"\s.]+)[`"]?\.?[`"]?([^`"\s]+)[`"]?', sql_text, re.IGNORECASE)
    
    if table_match:
        if len(table_match.groups()) >= 2:
            db_name = table_match.group(1)
            table_name = table_match.group(2)
        else:
            db_name = None
            table_name = table_match.group(1)
    else:
        print("Error: Could not find table name in the CREATE TABLE statement.")
        return None, None, [], []
    
    full_table_name = f"{db_name}.{table_name}" if db_name else table_name
    
    # Extract column definitions
    columns = []
    auto_increment_columns = []
    column_section = sql_text[sql_text.find('(') + 1:sql_text.rfind(')')]
    
    # Split by commas but ignore commas within parentheses (for nested definitions)
    level = 0
    start = 0
    column_defs = []
    
    for i, char in enumerate(column_section):
        if char == '(':
            level += 1
        elif char == ')':
            level -= 1
        elif char == ',' and level == 0:
            column_defs.append(column_section[start:i].strip())
            start = i + 1
    
    if start < len(column_section):
        column_defs.append(column_section[start:].strip())
    
    # Process each column definition
    for col_def in column_defs:
        # Skip PRIMARY KEY and other constraints
        if col_def.startswith('PRIMARY KEY') or col_def.startswith('FOREIGN KEY') or col_def.startswith('CONSTRAINT') or col_def.startswith('INDEX') or col_def.startswith('KEY'):
            continue
        
        # Extract column name
        col_match = re.search(r'^[`"]?([^`"\s]+)[`"]?\s+', col_def)
        if col_match:
            col_name = col_match.group(1)
            columns.append(col_name)
            
            # Check if column is auto_increment
            if 'AUTO_INCREMENT' in col_def.upper():
                auto_increment_columns.append(col_name)
    
    return db_name, table_name, columns, auto_increment_columns

def generate_infile_query(db_name, table_name, columns, auto_increment_columns, csv_file_path=None):
    """Generate LOAD DATA INFILE query based on table definition"""
    full_table_name = f"`{db_name}`.`{table_name}`" if db_name else f"`{table_name}`"
    
    if not csv_file_path:
        csv_file_path = f"C:\\ProgramData\\MySQL\\MySQL Server 9.3\\Uploads\\{table_name}.csv"
    
    # Format CSV path with double backslashes for SQL
    formatted_csv_path = csv_file_path.replace('\\', '\\\\')
    
    # Auto-detect CSV format if the file exists
    csv_format = None
    try:
        if os.path.exists(csv_file_path):
            csv_format = detect_csv_format(csv_file_path)
            print(f"CSV format detected: {csv_format}")
    except Exception as e:
        print(f"Warning: Could not detect CSV format: {e}")
        csv_format = None
    
    # Use detected format or fallback to defaults
    if csv_format:
        delimiter = csv_format['delimiter']
        line_terminator = csv_format['line_terminator']
        quote_char = csv_format['quote_char']
        escape_char = csv_format['escape_char']
        encoding = csv_format['encoding']
    else:
        delimiter = ','
        line_terminator = '\\r\\n'
        quote_char = '"'
        escape_char = '"'
        encoding = 'utf8mb4'
    
    query = f"""-- Load data into {full_table_name}
LOAD DATA INFILE '{formatted_csv_path}'
INTO TABLE {full_table_name}
CHARACTER SET {encoding}
FIELDS TERMINATED BY '{delimiter}'
OPTIONALLY ENCLOSED BY '{quote_char}'
ESCAPED BY '{escape_char}'
LINES TERMINATED BY '{line_terminator}'
IGNORE 1 LINES
(
"""
      # Add column mappings, excluding auto-increment columns
    csv_columns = []
    
    # Process each column
    for i, col in enumerate(columns):
        if col not in auto_increment_columns:
            csv_columns.append(col)
      # Format the column lines with commas in the proper place and comments after
    column_lines = []
    for i, col in enumerate(csv_columns):
        line = f"  @{col:<30}"
        if i < len(csv_columns) - 1:  # Add comma only if not the last item
            line += ","
        column_lines.append(line)
    
    # Add all column lines to the query
    query += "\n" + "\n".join(column_lines) + "\n"
    
    # Add SET section for NULL handling and skip auto_increment fields
    query += ")\nSET\n"
    
    # Create SET statements for non-auto-increment columns
    set_statements = []
    for col in columns:
        if col not in auto_increment_columns:
            set_statements.append(f"  {col:<30} = NULLIF(@{col},'')")
    
    # Join SET statements with commas
    query += ",\n".join(set_statements)
    query += ";"
    
    return query

def select_file_dialog(title="Select a file", filetypes=None):
    """Open a file selection dialog"""
    try:
        import tkinter as tk
        from tkinter import filedialog
        
        # Initialize Tk window but hide it
        root = tk.Tk()
        root.withdraw()
        
        # Show the file dialog
        file_path = filedialog.askopenfilename(
            title=title,
            filetypes=filetypes or [("All files", "*.*")]
        )
        
        # Close the hidden window
        root.destroy()
        
        return file_path
    except ImportError:
        print("Warning: tkinter is not available, cannot show file dialog")
        return None

def main():
    parser = argparse.ArgumentParser(description='Generate LOAD DATA INFILE statements from CREATE TABLE statements')
    parser.add_argument('--no-gui', action='store_true', help='Disable GUI file dialogs (use command line only)')
    parser.add_argument('input_file', nargs='?', help='SQL file containing CREATE TABLE statement')
    parser.add_argument('--csv', help='Path to CSV file to load')
    parser.add_argument('--output', help='Output file for generated query')
    
    args = parser.parse_args()
    
    # Use GUI by default unless --no-gui is specified
    use_gui = not args.no_gui
    
    # Step 1: Get the SQL file with CREATE TABLE statement
    if not args.input_file and use_gui:
        print("Step 1: Select your SQL file containing the CREATE TABLE statement...")
        sql_file = select_file_dialog("Select SQL file with CREATE TABLE statement", [("SQL files", "*.sql"), ("All files", "*.*")])
        if sql_file:
            args.input_file = sql_file
        else:
            print("No SQL file selected. Exiting.")
            return
    
    # Step 2: Get the CSV file to import
    if not args.csv and use_gui:
        print("Step 2: Select your CSV file to import...")
        csv_file = select_file_dialog("Select CSV file to import", [("CSV files", "*.csv"), ("All files", "*.*")])
        if csv_file:
            args.csv = csv_file
        else:
            print("No CSV file selected. Using default path.")
    
    # Step 3: Get output location (optional)
    if not args.output and use_gui:
        print("Step 3: Choose where to save the generated INFILE query (optional)...")
        output_file = select_file_dialog("Save generated query as...", [("SQL files", "*.sql"), ("All files", "*.*")])
        if output_file:
            args.output = output_file
    
    # Get SQL input from file or stdin
    if args.input_file:
        try:
            with open(args.input_file, 'r') as f:
                sql_text = f.read()
            print(f"✓ Loaded SQL file: {args.input_file}")
        except FileNotFoundError:
            print(f"Error: Could not find SQL file: {args.input_file}")
            return
    else:
        print("Enter/paste CREATE TABLE statement (press Ctrl+D or Ctrl+Z+Enter when finished):")
        sql_text = sys.stdin.read()    
    db_name, table_name, columns, auto_increment_columns = parse_create_table_statement(sql_text)
    
    if columns:
        print(f"✓ Parsed table: {db_name}.{table_name}" if db_name else f"✓ Parsed table: {table_name}")
        print(f"✓ Found {len(columns)} columns")
        if auto_increment_columns:
            print(f"✓ Auto-increment columns detected: {', '.join(auto_increment_columns)}")
        
        # Show CSV file being used
        if args.csv:
            print(f"✓ Using CSV file: {args.csv}")
        else:
            default_csv = f"C:\\ProgramData\\MySQL\\MySQL Server 9.3\\Uploads\\{table_name}.csv"
            print(f"✓ Using default CSV path: {default_csv}")
        
        infile_query = generate_infile_query(db_name, table_name, columns, auto_increment_columns, args.csv)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(infile_query)
            print(f"✓ Query written to: {args.output}")
            print("\n" + "="*50)
            print("GENERATED INFILE QUERY:")
            print("="*50)
            print(infile_query)
        else:
            print("\n" + "="*50)
            print("GENERATED INFILE QUERY:")
            print("="*50)
            print(infile_query)
            
        print("\n" + "="*50)
        print("SUMMARY:")
        print("="*50)
        print(f"• Table: {db_name}.{table_name}" if db_name else f"• Table: {table_name}")
        print(f"• Columns mapped: {len([c for c in columns if c not in auto_increment_columns])}")
        if auto_increment_columns:
            print(f"• Auto-increment columns excluded: {', '.join(auto_increment_columns)}")
        print("• Ready to execute in MySQL!")
    else:
        print("❌ Error: Failed to extract columns from CREATE TABLE statement")

if __name__ == "__main__":
    main()
