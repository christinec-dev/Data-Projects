# Excel to CSV Converter

A simple Python utility to convert all sheets in an Excel file to individual CSV files.

## Features

- GUI dialog to select an Excel file
- Converts each sheet to a separate CSV file
- Preserves sheet names in the output filenames
- Shows conversion summary with statistics

## Requirements

- Python 3.6+
- pandas
- openpyxl

## Installation

1. Ensure you have Python installed on your system
2. Install the required packages:
   ```
   pip install pandas openpyxl xlrd
   ```

## Usage

1. Run the script:
   ```
   python app.py
   ```
2. Select an Excel file using the file dialog
3. The script will:
   - Read all sheets from the Excel file
   - Create a folder named "{filename}_csv_output" in the same directory
   - Convert each sheet to a CSV file named "{filename}_{sheet_name}.csv"
   - Show a summary dialog with conversion statistics

## Output

The CSV files will be saved in a new directory with the naming pattern:
`{original_excel_filename}_csv_output/{original_excel_filename}_{sheet_name}.csv`
