# eBay Pokémon Collectibles Scraper

This project provides a Python-based scraper designed to extract and analyze Pokémon collectible listings from the [eBay website](https://www.ebay.com/b/Sealed-Collectible-Card-Game-Packs/183456/bn_1893736). By automating data collection, this scraper facilitates efficient analysis and visualization of collectible details, including titles, images, prices, shipping costs, and sales data. By using libraries like `selenium`, `beautifulsoup4`, and `pandas`, the scraper retrieves, processes, and transforms the data into a structured format for further insights.

**The final exported data can be viewed through two methods:**
- Using the Excel file `data/pokemon_cards_data.xlsx`
- Utilizing the CSV file `data/pokemon_cards_data.csv`

**Here is a sample of the data scraped:**
| Title                                                                            | Image                                                                                                                                      | Link                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Price (USD) | Shipping Cost (USD) | Delivery   | Amount Sold |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ------------------- | ---------- | ----------- |
| Pokemon SV9 Journey Together Enhanced Booster with Box Topper Promo Card         | [https://i.ebayimg.com/thumbs/images/g/4x0AAeSwrppnxp-y/s-l1200.webp](https://i.ebayimg.com/thumbs/images/g/4x0AAeSwrppnxp-y/s-l1200.webp) | [https://www.ebay.com/itm/156759169279?itmmeta=01JQRMCXBWS1P8MPTBVYGKNRRA&hash=item247f9318ff:g:4x0AAeSwrppnxp-y&itmprp=enc%3AAQAKAAAA4MHg7L1Zz0LA5DYYmRTS30nPIuofh9eqq43eQ8%](https://www.ebay.com/itm/156759169279?itmmeta=01JQRMCXBWS1P8MPTBVYGKNRRA&hash=item247f9318ff:g:4x0AAeSwrppnxp-y&itmprp=enc%3AAQAKAAAA4MHg7L1Zz0LA5DYYmRTS30nPIuofh9eqq43eQ8%25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 240.27      | 0                   | Thu, Apr 3 | 446         |
| POKEMON TCG  1000 CARD GAME BULK LOT INSTANT COLLECTION NEAR MINT ENGLISH        | [Link](https://ir.ebaystatic.com/cr/v/c1/s_1x2.gif)                                                 | [Link](https://www.ebay.com/itm/116397108360?itmmeta=01JQRMCXBWW6WS4FQEYP0CSS8M&hash=item1b19ceec88:g:n5QAAOSwQhtnPOv0&itmprp=enc%3AAQAKAAAA4MHg7L1Zz0LA5DYYmRTS30kz6Ak0O2a3qQRxHh%2Bua0lOXgHW%2BjTZYjILytYlihwFcPm1DOopVdDRQOcm%2FoQXZi%2BIxn31wEBuduyLUFN%2BrTgx7yn%2FVX98SUps599Lx%2FB2VtdlMJNpDUrKLbvq%2B%2FLog8mwkbTi8FIhD3wdA0gwIBZ7%2BNC%2FqHqXgJhc64IoPO90wUXjr8bTZvHxao9zO1jpGa9oERjYuh52dNgO%2FHuB63mDkQZ6mbBItddsibn%2FBKDFFuIOajUhUoFhb69flldAV%2FyyXng1%2BuTatF1RIeg8pLW8%7Ctkp%3ABFBMitazlL5l) | 28.02       | 0                   | Fri, Apr 4 | 75          |
| POKEMON THE GLORY OF TEAM ROCKET - SV10 JAPANESE - SEALED BOOSTER BOX - PRE SALE | [Link](https://ir.ebaystatic.com/cr/v/c1/s_1x2.gif)                                                 | [Link](https://www.ebay.com/itm/356715350225?itmmeta=01JQRMCXBWQV1TPV1S99GZCES0&hash=item530de448d1:g:AZYAAOSwyWBn5fix&itmprp=enc%3AAQAKAAAAwMHg7L1Zz0LA5DYYmRTS30l4rnG8hskrFVNwwYeDX0GVfXOFYQNzMytkTrHL31ABvWCVEQ88qjsd43hDej0Sj%2FuB4QIxld4V2ugoIb8YDsSjzZ%2FiV5gtd2eFenlioRHwkKR85EJ3R7D7uTjCTPkrcIHNvi5AAVPJNf6zoUtFULevYaDBX1JgrxFVUZePfbajjYiyQC3vOSxCeLmyt1EVyVhU1qPm%2FRQkyqiZfNlgEKoGidkPflF9SOntdei3yzFjjg%3D%3D%7Ctkp%3ABk9SR4rWs5S-ZQ)                                                                                                                     | 185.22      | 0                   | Thu, Apr 3 | 338         |
| Pokemon 151 Singles - Reverse Holo, Full Arts, IR! $1 Shipping! Choose Your Card | [Link](https://i.ebayimg.com/thumbs/images/g/n5QAAOSwQhtnPOv0/s-l1200.webp) | [Link](https://www.ebay.com/itm/176105703833?itmmeta=01JQRMCXBW8CG859YCDJHP4JV4&hash=item2900b7c999:g:mIQAAOSwIWVmM-kd&itmprp=enc%3AAQAKAAAAwMHg7L1Zz0LA5DYYmRTS30lnOHHNbKiX6R5twjYV%2FYIoKEwPHpJS41dxN23awSQnatm1yd06BNl3bUUOXzMAtVhaUwu9k65Zr6AXqaBAr8hKYLjjEZY5fvBxty2yyh82xdWfUciGVMqh%2FIMv%2F%2BxD1Zofsr%2BIEgHalb0c3jncpXfL8rKixoRLUBQSASMl1J2in5wTDthmhygsUsW6BqXAnfOz85sK1vEDWF3ht9FlYu1QBtQZ8g5lrGDywvPai7%2Fosg%3D%3D%7Ctkp%3ABk9SR4rWs5S-ZQ&var=475872291799)                                                                       | 290.32      | 1                   | Thu, Apr 3 | 200         |
| Pokemon Scarlet & Violet Journey Together Enhanced Booster box 36 pack sealed    | [Link](https://i.ebayimg.com/thumbs/images/g/AZYAAOSwyWBn5fix/s-l1200.webp) | [Link](https://www.ebay.com/p/25063574029?iid=187091187074)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 235.16      | 0                   | Thu, Apr 3 | 5851        |

## Navigation
1. [Objective](#objective)
2. [Data Source](#data-source)
3. [Features](#features)
4. [Usage](#usage)
5. [Further Exploration](#further-exploration)

## Objective
The primary objective of this scraper is to automate the collection of Pokémon collectible listings from eBay, enabling analysts to efficiently perform in-depth analysis and visualization using tools like pandas and matplotlib.

## Data Source
- **URL:** [eBay Pokémon Collectibles](https://www.ebay.com/b/Pokemon-TCG/2536/bn_7117595258)
- **Endpoints:** It scrapes the first few pages of the eBay Pokémon collectibles section.
- **Data Points:** The scraper provides the following data points:
    - Title
    - Image
    - Link
    - Price (USD)
    - Shipping Cost (USD)
    - Delivery Date
    - Amount Sold

## Features
### Data Extraction:
- The scraper uses Selenium to navigate through multiple pages of listings and BeautifulSoup to parse the HTML content.
- It processes the data to extract relevant information such as titles, images, prices, and sales data.

### Data Preprocessing:
- The extracted data is organized into a pandas DataFrame, making it easy to manipulate and analyze.
- The data is formatted, cleaned, and enriched with additional metrics like realtime currency conversion and sales analysis.

### Data Export:
- The processed data is exported to both Excel and CSV formats.
- This allows users to perform further analysis using spreadsheet software or import the data into other analytical tools.

### Error Handling:
- The scraper includes error handling to manage potential issues such as network errors or changes in the website structure.

## Usage
### Prerequisites
- Python 3.8+.
- Install the required libraries: `pip install -r requirements.txt`.
- Ensure you have the appropriate WebDriver (e.g., ChromeDriver) installed and in your `PATH`.

### Running the Scraper

**Using the Jupyter Notebook:**
1. Open `scraper.ipynb` in Jupyter Notebook.
2. Run all cells in the notebook.

**Using the Python Script:**
- Open a terminal or command prompt.
- Navigate to the project directory.
- Run the script: `python scraper.py`

## Further Exploration
With the data, users can perform a variety of analytics to gain insights into Pokémon collectibles. Here are potential use-cases for the dataset:
- **Price Analysis:** Analyze the distribution of prices and identify trends in collectible values.
- **Sales Performance:** Examine sales data to determine which collectibles are most popular.
- **Shipping and Delivery:** Explore shipping costs and delivery times to assess logistical efficiency.
