# INFILE Creator

A Python tool for automatically generating MySQL LOAD DATA INFILE statements from CREATE TABLE definitions.

## Features

- Parses CREATE TABLE statements to extract table name and column definitions
- Auto-detects CSV file format (delimiters, line terminators, quotes)
- Generates properly formatted LOAD DATA INFILE statements with column mappings
- Handles NULL values with NULLIF transformations
- Properly handles AUTO_INCREMENT columns (excludes them from CSV mapping)
- GUI file selection dialogs for easy use
- Configurable CSV file path and delimiters

## Usage

### Interactive Mode (Default)

Simply run the script and it will guide you through file selection:

```bash
python app.py
```

The script will:
1. **Step 1**: Ask you to select your SQL file containing the CREATE TABLE statement
2. **Step 2**: Ask you to select your CSV file to import
3. **Step 3**: Optionally ask where to save the generated query
4. **Generate**: Create the LOAD DATA INFILE statement with proper formatting

### Command Line Mode

```bash
python app.py [input_file] [--csv CSV_PATH] [--output OUTPUT_FILE] [--no-gui]
```

#### Arguments:

- `input_file`: Optional file containing the CREATE TABLE statement
- `--csv`: Path to the CSV file to load (defaults to table_name.csv in MySQL uploads folder)
- `--output`: Write the generated query to this file instead of stdout
- `--no-gui`: Disable GUI file dialogs and use command line only

#### Examples:

```bash
# Interactive mode (default) - GUI will guide you through file selection
python app.py

# Command line mode with specific files
python app.py create_table.sql --csv "C:\path\to\data.csv" --output "load_query.sql"

# Command line mode without GUI
python app.py create_table.sql --csv "C:\path\to\data.csv" --no-gui

# From stdin (no GUI)
echo "CREATE TABLE..." | python app.py --no-gui
```

#### Dependencies:

```bash
# Install required packages
pip install chardet
```

### Interactive Usage

If no input file is provided, the script will prompt for input:

```
Enter/paste CREATE TABLE statement (press Ctrl+D or Ctrl+Z+Enter when finished):
```

## Example Output

For a CREATE TABLE statement like:

```sql
CREATE TABLE IF NOT EXISTS `sample_db`.`customers` (
  `customer_id` INT AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  PRIMARY KEY (customer_id)
);
```

The generated INFILE statement would be:

```sql
-- Load data into `sample_db`.`customers`
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 9.3\\Uploads\\customers.csv'
INTO TABLE `sample_db`.`customers`
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(
  @customer_id,                  -- 1
  @name,                         -- 2
  @email,                       -- 3
)
SET
  customer_id          = NULLIF(@customer_id,''),
  name                 = NULLIF(@name,''),
  email                = NULLIF(@email,'');
```
