# Coinlore Cryptocurrency Data Scraper: Extract, Transform, and Export

This project provides a Python-based scraper to efficiently extract cryptocurrency data from the [Coinlore API](https://www.coinlore.com/cryptocurrency-data-api#global). By automating data collection, this scraper saves time and enables in-depth analysis of key cryptocurrency metrics such as price, market cap, and trading volume. The scraper leverages libraries such as `requests` and `pandas` to retrieve, process, and export data to Excel and CSV formats for further analysis.

**The final exported data can be viewed through two methods:**
- Using the Excel file `data/crypto_data.xlsx`
- Utilizing the CSV file `data/crypto_data.csv`

**Here is a sample of the data scraped:**
| Symbol | Name     | Rank | Price (USD) | Percent Change (24h) | Percent Change (1h) | Percent Change (7 days) | Price (Bitcoin) | Market Cap (USD) | Trading Volume (24h) | Adjusted Volume (24h) | Circulating Supply | Total Supply     |
|--------|----------|------|-------------|-----------------------|---------------------|-------------------------|-----------------|------------------|----------------------|-----------------------|--------------------|------------------|
| BTC    | Bitcoin  | 1    | 83714.67    | -1.98                 | 0.01                | -0.19                   | 1.00            | 1661105111817.30 | 2.58E+10             | 2.6E+10               | 19842462.00        | 19842462         |
| ETH    | Ethereum | 2    | 1880.26     | -1.83                 | 0.08                | -4.73                   | 0.022459        | 226521042282.39  | 1.14E+10             | 1.21E+10              | 120473321.00       | 122375302        |
| USDT   | Tether   | 3    | 1.01        | 0.43                  | -0.16               | 0.19                    | 0.000012        | 140086894935.40  | 4.75E+10             | 5.05E+10              | 139329876218.00    | 141572991338.46  |
| XRP    | XRP      | 4    | 2.12        | -5.09                 | 0.02                | -11.35                  | 0.000025        | 122429487358.83  | 3.09E+09             | 2.51E+09              | 57641211234.00     | 99986586496      |

## Navigation
1. [Objective](#objective)
2. [Data Source](#data-source)
3. [Features](#features)
4. [Usage](#usage)
5. [Further Exploration](#further-exploration)

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

## Further Exploration
With the data users can perform a variety of analytics to gain insights into the cryptocurrency market performance. Here's potential use-cases for the dataset:
   - **Price Fluctuations:** Analyze the percent change in price over different time frames (24h, 1h, 7 days) to identify market trends and volatility.
   - **Market Cap Insights:** Evaluate the market capitalization of different cryptocurrencies to understand their market dominance and stability.
   - **Volume Trends:** Examine trading and adjusted volumes to assess liquidity and trading activity for each cryptocurrency.
   - **Supply Analysis:** Analyze circulating and total supply to understand scarcity and potential inflationary pressures.
   - **Cryptocurrency Comparisons:** Compare different cryptocurrencies based on price, market cap, and trading volume to identify investment opportunities.
   - **Performance Benchmarks:** Use Bitcoin as a benchmark to compare the performance of other cryptocurrencies in terms of price and market cap.
   - **Risk Assessment:** Use historical price changes and market cap data to assess the risk associated with investing in specific cryptocurrencies.
   - **Portfolio Diversification:** Develop strategies for diversifying a cryptocurrency portfolio based on performance metrics and market trends.
