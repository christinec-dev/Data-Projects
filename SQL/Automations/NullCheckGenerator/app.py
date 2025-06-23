import os
import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk
import pandas as pd
import sqlite3
import pyodbc
from slugify import slugify
import re

# ---------- tweakables ----------
ROW_SAMPLE = 1_000  # rows to peek at for column detection
# ---------------------------------

def clean_name(txt: str) -> str:
    """
    Make a SQL-friendly identifier:
    - lower_case
    - spaces & punctuation -> underscore
    - leading digits -> prepend 'c_'
    """
    name = slugify(txt, separator="_")
    if re.match(r"^\d", name):
        name = f"c_{name}"
    return name.lower()

def get_columns_from_file(file_path):
    """
    Extract column names from various file types
    Returns a list of column names
    """
    file_ext = os.path.splitext(file_path)[1].lower()
    columns = []
    
    try:
        if file_ext in ['.xlsx', '.xls']:
            # For Excel files, get columns from first sheet
            xl = pd.ExcelFile(file_path)
            first_sheet = xl.sheet_names[0]
            df = xl.parse(first_sheet, nrows=ROW_SAMPLE)
            columns = df.columns.tolist()
        
        elif file_ext == '.csv':
            df = pd.read_csv(file_path, nrows=ROW_SAMPLE)
            columns = df.columns.tolist()
        
        elif file_ext == '.txt':
            # Try to detect separator (tab, comma, pipe, semicolon)
            for sep in ['\t', ',', '|', ';']:
                try:
                    df = pd.read_csv(file_path, sep=sep, nrows=100, encoding='utf-8')
                    if len(df.columns) > 1:
                        df = pd.read_csv(file_path, sep=sep, nrows=ROW_SAMPLE)
                        columns = df.columns.tolist()
                        break
                except:
                    continue
            else:
                df = pd.read_csv(file_path, sep='\t', nrows=ROW_SAMPLE, encoding='utf-8')
                columns = df.columns.tolist()
        
        else:
            # Try default CSV read
            df = pd.read_csv(file_path, nrows=ROW_SAMPLE)
            columns = df.columns.tolist()
    
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {str(e)}")
        return []
    
    return columns

def get_columns_from_database(connection_string, table_name):
    """
    Get column names from a database table
    Supports SQLite and SQL Server connections
    """
    columns = []
    
    try:
        if connection_string.lower().endswith('.db') or connection_string.lower().endswith('.sqlite'):
            # SQLite connection
            conn = sqlite3.connect(connection_string)
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [row[1] for row in cursor.fetchall()]
            conn.close()
        else:
            # SQL Server or other ODBC connection
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            cursor.execute(f"""
                SELECT COLUMN_NAME 
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_NAME = '{table_name}'
                ORDER BY ORDINAL_POSITION
            """)
            columns = [row[0] for row in cursor.fetchall()]
            conn.close()
    
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not connect to database or read table: {str(e)}")
        return []
    
    return columns

def generate_null_check_query(columns, table_name, clean_column_names=False):
    """
    Generate SQL query to check for null values in all columns
    """
    if not columns:
        return ""
    
    select_statements = []
    
    for col in columns:
        # Optionally clean column names for SQL compatibility
        column_name = clean_name(col) if clean_column_names else col
        
        # Handle column names with spaces or special characters
        if ' ' in column_name or any(char in column_name for char in ['-', '.', '(', ')', '#', '@']):
            column_ref = f'`{column_name}`'  # MySQL/SQLite style
        else:
            column_ref = column_name
        
        select_statements.append(f"    SUM({column_ref} IS NULL) AS {column_name}_nulls")
    
    select_clause = ",\n".join(select_statements)
    
    query = f"""SELECT
{select_clause}
FROM {table_name};"""
    
    return query

def show_column_selection_dialog(columns, table_name):
    """
    Show a dialog to let user select which columns to include
    """
    # Ensure root doesn't already exist
    try:
        root = tk.Tk()
        is_main_window = True
    except tk.TclError:
        # A root window already exists, create a Toplevel instead
        root = tk.Toplevel()
        is_main_window = False
    
    root.title("Select Columns for Null Check")
    root.geometry("500x600")
    root.lift()  # Bring window to front
    root.focus_force()  # Force focus
    root.attributes('-topmost', True)  # Keep on top
    
    # Variables to store selections
    selected_columns = []
    column_vars = {}
    
    # Main frame
    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Title
    title_label = ttk.Label(main_frame, text=f"Select columns for null check in table: {table_name}", 
                           font=('Arial', 12, 'bold'))
    title_label.pack(pady=(0, 10))
    
    # Select All / Deselect All buttons
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=(0, 10))
    
    def select_all():
        print("Select All clicked")
        for var in column_vars.values():
            var.set(True)
    
    def deselect_all():
        print("Deselect All clicked")
        for var in column_vars.values():
            var.set(False)
    
    select_all_btn = ttk.Button(button_frame, text="Select All", command=select_all)
    select_all_btn.pack(side=tk.LEFT, padx=(0, 5))
    
    deselect_all_btn = ttk.Button(button_frame, text="Deselect All", command=deselect_all)
    deselect_all_btn.pack(side=tk.LEFT)
      # Container frame for scrollable content
    container = ttk.Frame(main_frame)
    container.pack(fill=tk.BOTH, expand=True)
    
    # Scrollable canvas
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    
    # Scrollable frame for checkboxes
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Pack the canvas and scrollbar
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Create checkboxes for each column
    for i, col in enumerate(columns):
        var = tk.BooleanVar(value=True)  # Default to selected
        column_vars[col] = var
        cb = ttk.Checkbutton(scrollable_frame, text=col, variable=var)
        cb.grid(row=i, column=0, sticky=tk.W, pady=2, padx=5)
    
    # Bottom buttons
    bottom_frame = ttk.Frame(main_frame)
    bottom_frame.pack(pady=(10, 0), fill=tk.X)
    
    def on_generate():
        print("Generate button clicked")
        nonlocal selected_columns
        selected_columns = [col for col, var in column_vars.items() if var.get()]
        print(f"Selected {len(selected_columns)} columns")
        root.quit()  # This will exit mainloop without destroying the window
        root.destroy()  # Now destroy the window
    
    def on_cancel():
        print("Cancel button clicked")
        nonlocal selected_columns
        selected_columns = []
        root.quit()
        root.destroy()
    
    generate_btn = ttk.Button(bottom_frame, text="Generate Query", command=on_generate)
    generate_btn.pack(side=tk.LEFT, padx=(0, 5))
    
    cancel_btn = ttk.Button(bottom_frame, text="Cancel", command=on_cancel)
    cancel_btn.pack(side=tk.LEFT)
    
    # Bind events
    root.protocol("WM_DELETE_WINDOW", on_cancel)  # Handle window close button
    
    # Start the dialog and wait for user interaction
    if is_main_window:
        root.mainloop()
    else:
        root.wait_window()  # Wait for this window to be destroyed
    
    return selected_columns

def main():
    # Create a root window but hide it initially
    root = tk.Tk()
    root.withdraw()
    
    # Ask user for data source type
    source_type = messagebox.askyesnocancel(
        "Data Source",
        "Choose data source:\n\nYes = File (Excel, CSV, TXT)\nNo = Database Table\nCancel = Exit"
    )
    
    if source_type is None:  # Cancel was clicked
        return
    
    columns = []
    table_name = ""
    
    if source_type:  # File source
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
        
        # Get columns from file
        columns = get_columns_from_file(file_path)
        
        # Suggest table name based on filename
        suggested_table = Path(file_path).stem
        table_name = simpledialog.askstring(
            "Table Name",
            f"Enter the table name for the query:",
            initialvalue=clean_name(suggested_table)
        )
    else:  # Database source
        # Get connection details
        connection_string = simpledialog.askstring(
            "Database Connection",
            "Enter connection string or SQLite file path:\n\nExamples:\n- SQLite: C:\\path\\to\\database.db\n- SQL Server: DRIVER={SQL Server};SERVER=server;DATABASE=db;Trusted_Connection=yes"
        )
        
        if not connection_string:
            print("No connection string provided. Exiting.")
            return
        
        table_name = simpledialog.askstring(
            "Table Name",
            "Enter the table name:"
        )
        
        if not table_name:
            print("No table name provided. Exiting.")
            return
        
        # Get columns from database
        columns = get_columns_from_database(connection_string, table_name)
    
    if not columns:
        messagebox.showerror("Error", "No columns found or could not read data source.")
        return
    
    if not table_name:
        table_name = "your_table"
    
    print(f"Found {len(columns)} columns in table '{table_name}'")
    print("Opening column selection dialog...")
    
    # Show column selection dialog
    selected_columns = show_column_selection_dialog(columns, table_name)
    
    print(f"Dialog closed. Selected columns: {len(selected_columns) if selected_columns else 0}")
    
    if not selected_columns:
        print("No columns selected or operation canceled.")
        return
    
    print(f"Selected {len(selected_columns)} columns for null check")
    
    # Ask if user wants to clean column names
    clean_names = messagebox.askyesno(
        "Column Names",
        "Do you want to clean column names for SQL compatibility?\n(converts spaces to underscores, removes special characters)"
    )
    
    # Generate the null check query
    null_check_query = generate_null_check_query(selected_columns, table_name, clean_names)
      # Create a new root for showing results and saving
    result_root = tk.Tk()
    result_root.withdraw()
    
    print("\nGenerated SQL Query:")
    print("-" * 50)
    print(null_check_query)
    print("-" * 50)
    
    # Ask user where to save the SQL file
    output_path = filedialog.asksaveasfilename(
        title="Save SQL Query As",
        defaultextension=".sql",
        initialfile=f"{table_name}_null_check.sql",
        filetypes=[("SQL files", "*.sql"), ("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if output_path:
        with open(output_path, 'w') as f:
            f.write(f"-- Null check query for table: {table_name}\n")
            f.write(f"-- Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"-- Columns checked: {len(selected_columns)}\n\n")
            f.write(null_check_query)
        
        print(f"\nSQL query saved to: {output_path}")
        
        # Copy to clipboard and show message
        result_root.clipboard_clear()
        result_root.clipboard_append(null_check_query)
        messagebox.showinfo(
            "Success", 
            f"SQL query saved to:\n{output_path}\n\nQuery has also been copied to clipboard!"
        )
    else:
        print("Save operation canceled.")
        
        # Still copy to clipboard and show confirmation
        result_root.clipboard_clear()
        result_root.clipboard_append(null_check_query)
        messagebox.showinfo("Query Generated", "Query copied to clipboard!")
    
    # Clean up
    result_root.destroy()

if __name__ == "__main__":
    main()
