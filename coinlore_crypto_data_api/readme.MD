# Coinlore Cryptocurrency Data Scraper: Extract, Transform, and Export

This project provides a Python-based scraper to efficiently extract cryptocurrency data from the [Coinlore API](https://www.coinlore.com/cryptocurrency-data-api#global). By automating data collection, this scraper saves time and enables in-depth analysis of key cryptocurrency metrics such as price, market cap, and trading volume. The scraper leverages libraries such as `requests` and `pandas` to retrieve, process, and export data to Excel and CSV formats for further analysis.

The final exported data can be viewed through two methods:
- Using the Excel file `data/crypto_data.xlsx`
- Utilizing the CSV file `data/crypto_data.csv`

## Navigation
1. [Objective](#objective)
2. [Data Source](#data-source)
3. [Features](#features)
4. [Usage](#usage)

## Objective
The primary objective of this scraper is to automate the collection of cryptocurrency data from Coinlore, enabling analysts to efficiently perform in-depth analysis and visualization using tools like Excel and pandas.

## Data Source
- **API:** [Coinlore API](https://www.coinlore.com/cryptocurrency-data-api#global)
- **Endpoint:** The scraper uses the `/api/tickers/` endpoint to fetch real-time data for various cryptocurrencies.
- **Data Points:** The API provides the following data points:
    - Symbol
    - Name
    - Rank
    - Price (USD)
    - Percent Change (24h, 1h, 7 days)
    - Price (Bitcoin)
    - Market Cap (USD)
    - Trading Volume (24h)
    - Adjusted Volume (24h)
    - Circulating Supply
    - Total Supply

## Features
### Data Extraction:
- The scraper sends requests to the Coinlore API to retrieve cryptocurrency data.
- It processes the JSON response to extract relevant data points.

### Data Preprocessing:
- The extracted data is organized into a pandas DataFrame, making it easy to manipulate and analyze.
- The extracted data is formatted, renamed (e.g. changing column names for better readability), and cleaned (e.g., converting data types, handling missing values) before exporting.
- The DataFrame includes columns for each data point provided by the API.

### Data Export:
- The processed data is exported to both Excel and CSV formats.
- This allows users to perform further analysis using spreadsheet software or import the data into other analytical tools.

### Error Handling:
- The scraper includes error handling to manage potential issues such as network errors or invalid API responses.

## Usage

### Prerequisites

- Python 3.8+.
- Install the required libraries: `pip install -r requirements.txt`.

### Running the Scraper

**Using the Jupyter Notebook:**

1.  Open `scraper.ipynb` in Jupyter Notebook.
2.  Run all cells in the notebook.

**Using the Python Script:**

1.  Open a terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the script: `python scraper.py`
