# Null Check Generator

This automation script generates SQL queries to check for missing (NULL) values in all columns of a table, eliminating the need to manually write each column check.

## Features

- **Multiple Data Sources**: Works with Excel files, CSV files, text files, and database tables
- **Column Selection**: Interactive dialog to select which columns to include in the null check
- **Smart Column Handling**: Automatically handles column names with spaces and special characters
- **Name Cleaning**: Option to clean column names for SQL compatibility
- **Multiple Database Support**: Works with SQLite and SQL Server databases
- **Export Options**: Save queries to SQL files and copy to clipboard

## How It Works

The script will generate a query like this:
```sql
SELECT
    SUM(store_address IS NULL) AS store_address_nulls,
    SUM(longitude IS NULL) AS longitude_nulls,
    SUM(latitude IS NULL) AS latitude_nulls,
    SUM(rating_count IS NULL) AS rating_count_nulls,
    SUM(review_time IS NULL) AS review_time_nulls,
    SUM(rating_num IS NULL) AS rating_num_nulls
FROM reviews;
```

## Usage

1. Run the script: `python app.py`
2. Choose your data source:
   - **File**: Select an Excel, CSV, or text file to extract column names
   - **Database**: Connect to a database table directly
3. Select which columns to include in the null check
4. Choose whether to clean column names for SQL compatibility
5. Save the generated query to a file

## Requirements

Install the required packages:
```bash
pip install pandas tkinter slugify pyodbc
```

## Supported File Types

- Excel files (.xlsx, .xls)
- CSV files (.csv)
- Text files (.txt) with various delimiters (tab, comma, pipe, semicolon)

## Database Support

- SQLite databases (.db, .sqlite files)
- SQL Server (via ODBC connection strings)
- Other ODBC-compatible databases

## Example Output

For a table named `reviews` with 6 columns, the script generates:
```sql
-- Null check query for table: reviews
-- Generated on: 2025-06-23 14:30:15
-- Columns checked: 6

SELECT
    SUM(store_address IS NULL) AS store_address_nulls,
    SUM(longitude IS NULL) AS longitude_nulls,
    SUM(latitude IS NULL) AS latitude_nulls,
    SUM(rating_count IS NULL) AS rating_count_nulls,
    SUM(review_time IS NULL) AS review_time_nulls,
    SUM(rating_num IS NULL) AS rating_num_nulls
FROM reviews;
```

## Benefits

- **Time Saving**: No need to manually type each column name
- **Error Reduction**: Eliminates typos in column names
- **Consistency**: Standardized query format
- **Flexibility**: Works with various data sources and formats
- **Interactive**: Easy-to-use GUI for column selection
