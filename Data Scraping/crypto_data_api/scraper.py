# Imports
import requests
import pandas as pd
import matplotlib.pyplot as plt

#region EXTRACTION

# Site to scrape (first 100 coins)
BASE_URL = 'https://api.coinlore.net/api/tickers/?start=0&limit=100'

# Device scraping details
# Received from https://www.whatismybrowser.com 
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0' 
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5'
}

# Scrape site for cryptocurrencies
def get_data():
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER)
    return res.json()
scraped_data = get_data()

# Convert to DataFrame
df = pd.DataFrame(scraped_data['data'])

#endregion

#region PREPROCESSING

# Remove missing values
df.fillna("", inplace=True) # replace NaN with empty spaces
df.drop("msupply", axis=1, inplace=True) # too many missing values to impute meaning

# Drop redundant columns
df.drop(['id', 'nameid'], axis=1, inplace=True)

# Rename columns
df.columns = df.columns.str.capitalize()
df.rename({"Price_usd": "Price (USD)", "Percent_change_24h": "Percent Change (24h)", "Percent_change_1h": "Percent Change (1h)", "Percent_change_7d": "Percent Change (7 days)", "Price_btc": "Price (Bitcoin)", "Market_cap_usd": "Market Cap (USD)", "Volume24": "Trading Volume (24h)", "Volume24a": "Adjusted Volume (24h)", "Csupply": "Circulating Supply", "Tsupply": "Total Supply"}, axis=1, inplace=True)

#endregion

#region EXPORTING

# File names
csv_file = 'crypto_data.csv'
excel_file = 'crypto_data.xlsx'

# Export to CSV
try:
    df.to_csv(csv_file, index=False)
    print(f"Data exported to {csv_file}")
except PermissionError as e:
    print(f"Permission error while writing to {csv_file}: {e}")

# Export to Excel
try:
    df.to_excel(excel_file, index=False, sheet_name='Top 100 Crypto')
    print(f"Data exported to {excel_file}")
except PermissionError as e:
    print(f"Permission error while writing to {excel_file}: {e}")

#endregion