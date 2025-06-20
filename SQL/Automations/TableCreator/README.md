# TableCreator

A Python utility that generates SQL CREATE TABLE statements from Excel, CSV, and TXT files.

## Overview

TableCreator is a tool that analyzes Excel spreadsheets, CSV files, and TXT files and automatically generates SQL DDL (Data Definition Language) statements to create corresponding database tables. It simplifies the process of creating database schemas based on existing data structures in various file formats.

## Features

- **Multiple File Format Support**: Works with Excel (.xlsx, .xls), CSV, and TXT files
- **GUI File Selection**: Choose files through a file explorer dialog
- **Custom Database Name**: Specify the target database/schema name through a dialog prompt
- **Custom Save Location**: Save the generated SQL to your preferred location
- **Data Type Inference**: Automatically maps data types to appropriate SQL data types
- **Date Detection**: Automatically detects date columns based on column names
- **Multiple Sheets Support**: Processes all sheets in an Excel workbook
- **Automatic Delimiter Detection**: Detects common delimiters (tab, comma, pipe, semicolon) in TXT files
- **Identifier Cleaning**: Converts column and sheet/file names to database-friendly identifiers

## Requirements

- Python 3.6+
- Required packages:
  - pandas
  - slugify

## Installation

1. Clone or download this repository
2. Install required packages:
```
pip install pandas python-slugify xlrd
```

## Usage

1. Run the script:
```
python app.py
```

2. Follow the GUI prompts:
   - Select your Excel, CSV, or TXT file when prompted
   - Enter a name for your target database/schema
   - Choose where to save the generated SQL file

## How It Works

1. The script reads the selected file (Excel, CSV, or TXT) and samples rows to determine data types
2. For TXT files, it automatically tries to detect the delimiter (tab, comma, pipe, semicolon)
3. For Excel files, it processes each sheet individually
4. Column names are converted to SQL-friendly identifiers
5. Data types are mapped to appropriate SQL data types
4. SQL CREATE TABLE statements are generated with proper formatting
5. The resulting SQL can be viewed in the console and saved to a file

## Data Type Mapping

| Excel Data Type | SQL Data Type |
|-----------------|---------------|
| object          | VARCHAR(255)  |
| int64           | INT           |
| float64         | DECIMAL(12,2) |
| datetime64[ns]  | DATE          |

Additionally, any column with "date" in its name will be mapped to the DATE data type regardless of the actual data type in Excel.

## Customization

You can modify the following parameters at the top of the script:
- `ROW_SAMPLE`: Number of rows to analyze for data type detection (default: 1,000)
- `VARCHAR_LEN`: Default VARCHAR length for string columns (default: 255)
