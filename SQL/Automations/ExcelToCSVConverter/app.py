import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import time

def select_excel_file():
    """
    Opens a file dialog to select an Excel file
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel Files", "*.xlsx *.xls"), ("All Files", "*.*")]
    )
    
    return file_path

def convert_excel_to_csv(excel_file):
    """
    Convert all sheets in an Excel file to individual CSV files
    """
    if not excel_file:
        return False, "No file selected."
    
    try:
        # Get the directory and filename without extension
        directory = os.path.dirname(excel_file)
        file_name = os.path.splitext(os.path.basename(excel_file))[0]
        
        # Create output directory if it doesn't exist
        output_dir = os.path.join(directory, f"{file_name}_csv_output")
        os.makedirs(output_dir, exist_ok=True)
        
        # Read Excel file
        print(f"Reading Excel file: {excel_file}")
        start_time = time.time()
        
        # Get all sheet names
        excel = pd.ExcelFile(excel_file)
        sheet_names = excel.sheet_names
        
        conversion_results = []
        
        # Process each sheet
        for sheet in sheet_names:
            sheet_start_time = time.time()
            print(f"Processing sheet: {sheet}")
            
            # Read the sheet
            df = pd.read_excel(excel, sheet_name=sheet)
            
            # Create CSV file name
            csv_file = os.path.join(output_dir, f"{file_name}_{sheet}.csv")
            
            # Export to CSV
            df.to_csv(csv_file, index=False)
            
            sheet_time = time.time() - sheet_start_time
            rows = len(df)
            cols = len(df.columns)
            
            conversion_results.append({
                'sheet': sheet,
                'rows': rows,
                'columns': cols,
                'time': sheet_time,
                'output': csv_file
            })
            
            print(f"Sheet '{sheet}' exported to {csv_file}")
        
        total_time = time.time() - start_time
        
        return True, {
            'total_sheets': len(sheet_names),
            'total_time': total_time,
            'output_dir': output_dir,
            'sheets': conversion_results
        }
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def show_results(result):
    """
    Display the conversion results
    """
    total_sheets = result['total_sheets']
    total_time = result['total_time']
    output_dir = result['output_dir']
    
    message = f"Successfully converted {total_sheets} sheets in {total_time:.2f} seconds.\n\n"
    message += f"CSV files saved to: {output_dir}\n\n"
    message += "Sheet details:\n"
    
    for sheet_data in result['sheets']:
        message += f"- {sheet_data['sheet']}: {sheet_data['rows']} rows, {sheet_data['columns']} columns\n"
    
    return message

def main():
    print("Excel to CSV Converter")
    print("=====================")
    print("Select an Excel file to convert all sheets to CSV files.")
    
    # Select Excel file
    excel_file = select_excel_file()
    
    if not excel_file:
        print("No file selected. Exiting.")
        return
    
    print(f"Selected file: {excel_file}")
    
    # Convert Excel to CSV
    success, result = convert_excel_to_csv(excel_file)
    
    if success:
        message = show_results(result)
        print("\nConversion Results:")
        print(message)
        
        # Show GUI message box with results
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Conversion Complete", message)
    else:
        print(f"Conversion failed: {result}")
        
        # Show error message
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Conversion Failed", result)

if __name__ == "__main__":
    main()