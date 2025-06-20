import re
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, simpledialog
import pandas as pd
from slugify import slugify

# ---------- tweakables ----------
ROW_SAMPLE    = 1_000                        # rows to peek at for dtype guessing
VARCHAR_LEN   = 100                          # default varchar length
# ---------------------------------

TYPE_MAP = {
    "object": f"VARCHAR({VARCHAR_LEN})",
    "int64": "INT",
    "float64": "DECIMAL(12,2)",
    "datetime64[ns]": "DATE"
}

def clean_name(txt: str) -> str:
    """
    Make a MySQL-friendly identifier:
    - lower_case
    - spaces & punctuation -> underscore
    - leading digits -> prepend 'c_'
    """
    name = slugify(txt, separator="_")
    if re.match(r"^\d", name):
        name = f"c_{name}"
    return name.lower()

def sql_for_sheet(sheet_name: str, df: pd.DataFrame, db_name: str) -> str:
    table = clean_name(sheet_name)
    cols  = []

    for col in df.columns:
        mysql_col = clean_name(col)
        pd_type   = str(df[col].dtype)

        # cheap override: if *Date* in original col name, force DATE
        if "date" in col.lower():
            mysql_type = "DATE"
        else:
            mysql_type = TYPE_MAP.get(pd_type, f"VARCHAR({VARCHAR_LEN})")

        cols.append(f"  `{mysql_col}` {mysql_type}")

    columns_block = ",\n".join(cols)
    return f"CREATE TABLE `{db_name}`.`{table}` (\n{columns_block}\n);\n"

def load_data(file_path):
    """
    Load data from Excel, CSV, or TXT file based on file extension
    Returns a dictionary of dataframes with sheet or filename as key
    """
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext in ['.xlsx', '.xls']:
        # For Excel files, return a dictionary of sheets
        xl = pd.ExcelFile(file_path)
        data_dict = {}
        for sheet in xl.sheet_names:
            data_dict[sheet] = xl.parse(sheet, nrows=ROW_SAMPLE)
    
    elif file_ext == '.csv':
        # For CSV files, just one dataframe with the filename as key
        filename = os.path.basename(os.path.splitext(file_path)[0])
        df = pd.read_csv(file_path, nrows=ROW_SAMPLE)
        data_dict = {filename: df}
    
    elif file_ext == '.txt':
        # For TXT files, try to infer separator
        filename = os.path.basename(os.path.splitext(file_path)[0])
        # Try to detect separator (tab, comma, pipe, semicolon)
        for sep in ['\t', ',', '|', ';']:
            try:
                df = pd.read_csv(file_path, sep=sep, nrows=100, encoding='utf-8')
                # If we have more than one column, assume this is the right separator
                if len(df.columns) > 1:
                    df = pd.read_csv(file_path, sep=sep, nrows=ROW_SAMPLE)
                    data_dict = {filename: df}
                    break
            except:
                continue
        else:  # If no separator works, use default
            df = pd.read_csv(file_path, sep='\t', nrows=ROW_SAMPLE, encoding='utf-8')
            data_dict = {filename: df}
    
    else:
        # For unknown file types, try default CSV read
        filename = os.path.basename(os.path.splitext(file_path)[0])
        try:
            df = pd.read_csv(file_path, nrows=ROW_SAMPLE)
        except:
            df = pd.DataFrame()  # Empty dataframe if can't read
        data_dict = {filename: df}
    
    return data_dict

def main():
    # Create a root window but hide it
    root = tk.Tk()
    root.withdraw()
      # Show the file selection dialog
    file_path = filedialog.askopenfilename(
        title="Select Data File",
        filetypes=[
            ("All supported files", "*.xlsx *.xls *.csv *.txt"),
            ("Excel files", "*.xlsx *.xls"),
            ("CSV files", "*.csv"),
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )
    
    if not file_path:
        print("No file selected. Exiting.")
        return
    
    source_file = Path(file_path)
    print(f"Selected file: {source_file}")
    
    # Prompt for database name
    db_name = simpledialog.askstring(
        "Database Name",
        "Enter the target database/schema name:",
        initialvalue="superstore_dw"    )
    if not db_name:
        print("No database name provided. Using 'default_db'.")
        db_name = "default_db"
    
    print(f"Using database name: {db_name}")
    
    # Load data based on file type
    data_dict = load_data(str(source_file))
    
    if not data_dict:
        print("Could not load data from the selected file.")
        return
        
    ddl_statements = []
    
    # Process each dataframe (each sheet/file)
    for name, df in data_dict.items():
        ddl_statements.append(sql_for_sheet(name, df, db_name))
    
    sql_out = "\n".join(ddl_statements)
    print(sql_out)
    
    # Ask user where to save the SQL file
    default_filename = source_file.stem + ".sql"
    output_path = filedialog.asksaveasfilename(
        title="Save SQL File As",
        defaultextension=".sql",
        initialfile=default_filename,
        filetypes=[("SQL files", "*.sql"), ("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if output_path:
        output_file = Path(output_path)
        with open(output_file, 'w') as f:
            f.write(sql_out)
        print(f"SQL has been saved to: {output_file}")
    else:
        print("Save operation canceled.")

if __name__ == "__main__":
    main()
