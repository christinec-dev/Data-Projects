# Imports
from selenium import webdriver
from currency_converter import CurrencyConverter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import pandas as pd
import time

#region EXTRACTION

def get_soup_from_driver(driver):
    """Get a BeautifulSoup object from a Selenium WebDriver"""
    return bs(driver.page_source, 'html.parser')

def get_product_details(driver):
    """Extract product details"""
    products = []
    base_url = "https://www.ebay.com/b/Pokemon-TCG/2536/bn_7117595258"
    
    # Navigate the first five pages
    for page in range(1, 5):
        # Parse the loaded page
        url = f"{base_url}?_pgn={page}"
        driver.get(url)
        time.sleep(2)
        soup = get_soup_from_driver(driver)
        
        # Find all product elements
        link_elements = soup.find_all('a', class_='bsig__title__wrapper')
        title_elements = soup.find_all('h3', class_='textual-display bsig__title__text')
        price_elements = soup.find_all('span', class_='textual-display bsig__price bsig__price--displayprice')
        logistic_elements = soup.find_all('span', class_='textual-display bsig__generic bsig__logisticsCost')
        delivery_elements = soup.find_all('span', class_='textual-display bsig__generic bsig__deliveryOptions bold')
        sold_elements = soup.find_all('span', class_='textual-display negative')
        image_elements = soup.find_all('img', class_='brwrvr__item-card__image')
        
        # Determine the minimum length to avoid index errors
        min_length = min(len(title_elements), len(link_elements), len(price_elements), len(logistic_elements), len(sold_elements))
        
        # Extract text or attributes from the first element only
        for i in range(min_length):
            link = link_elements[i]['href']
            title = title_elements[i].text.strip()
            price = price_elements[i].text.strip()
            logistics = logistic_elements[i].text.strip()
            delivery = delivery_elements[i].text.strip() if i < len(delivery_elements) else None
            sold = sold_elements[i].text.strip() if i < len(sold_elements) else None
            image = image_elements[i]['src']
            
            products.append((title, image, link, price, logistics, delivery, sold))
    
    return products

# Set up Selenium WebDriver (in this case Chrome)
driver = webdriver.Chrome()

# Get product details
product_details = get_product_details(driver)

# Convert to DataFrame
df = pd.DataFrame(product_details, columns=['Title', 'Image', 'Link', 'Price (USD)', 'Shipping Cost (USD)', 'Delivery', 'Amount Sold'])

# Close the driver
driver.quit()

#endregion

#region PREPROCESSING

# Fill missing values
df_copy = df.copy()
df_copy['Delivery'] = df_copy['Delivery'].fillna('Not Available')

# Convert currency to dollars
c = CurrencyConverter()

def extract_max_price_and_convert(price_str):
    # Remove 'ZAR' and split the string
    price_range = price_str.replace('ZAR', '').split('to')
    # Convert the prices to floats and get the maximum value
    price_zar = max(float(price.strip().replace(',', '')) for price in price_range)
    # Convert the maximum ZAR price to USD
    price_usd = c.convert(price_zar, 'ZAR', 'USD')
    return price_usd

# Apply the function to the 'Price' column
df_copy['Price (USD)'] = df_copy['Price (USD)'].apply(extract_max_price_and_convert).round(2)

# Convert shipping cost to USD
def convert_shipping_to_usd(shipping_str):
    if 'Free shipping' in shipping_str:
        return 0.0
    else:
        shipping_zar = float(shipping_str.replace('ZAR', '').replace('shipping', '').strip())
        shipping_usd = c.convert(shipping_zar, 'ZAR', 'USD')
        return shipping_usd

# Apply the conversion function to the 'Shipping' column
df_copy['Shipping Cost (USD)'] = df_copy['Shipping Cost (USD)'].apply(convert_shipping_to_usd).round(2)

# Remove the text 'sold' and commas, and strip whitespace
df_copy['Amount Sold'] = df_copy['Amount Sold'].str.replace('sold', '').str.replace(',', '').str.strip()
df_copy = df_copy[df_copy['Amount Sold'].str.isnumeric()]
df_copy['Amount Sold'] = df_copy['Amount Sold'].astype(float)

# Reformat dataframe
df_copy = df_copy.reindex(columns=['Title', 'Image', 'Link', 'Price (USD)', 'Shipping Cost (USD)', 'Delivery', 'Amount Sold'])

#endregion

#region EXPORTING

# File names
csv_file = 'pokemon_cards_data.csv'
excel_file = 'pokemon_cards_data.xlsx'

# Export to CSV
try:
    df_copy.to_csv(csv_file, index=False)
    print(f"Data exported to {csv_file}")
except PermissionError as e:
    print(f"Permission error while writing to {csv_file}: {e}")

# Export to Excel
try:
    df_copy.to_excel(excel_file, index=False, sheet_name='eBay Listings')
    print(f"Data exported to {excel_file}")
except PermissionError as e:
    print(f"Permission error while writing to {excel_file}: {e}")

#endregion