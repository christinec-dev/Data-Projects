# Premier League 2024/25 Season Data Scraper

This project provides a Python-based scraper designed to extract and present Premier League standings and player performance data from multiple APIs, including the [football-data.org API](https://www.football-data.org/documentation/quickstart). By automating data collection, this scraper facilitates efficient analysis and visualization of team and player performance during the 2024/25 Premier League season. Leveraging libraries like `requests` and `pandas`, the scraper retrieves, processes, and transforms the data into a structured format for further insights. 

The final exported data can be viewed through two methods:
- Using the Excel file `data/plf_data.xlsx`
- Utilizing the CSV file `data/plf_data.csv`


## Navigation
1. [Objective](#objective)
2. [Data Source](#data-source)
3. [Features](#features)
4. [Usage](#usage)

## Objective
The primary objective of this scraper is to automate the collection of Premier League standings and player performance data, enabling analysts to efficiently perform in-depth analysis and visualization using tools like Excel and pandas.

## Data Source
- **API:** [Football-Data.org API](https://www.football-data.org/documentation/quickstart)
- **Endpoints:**
    - `/v4/competitions/{id}/standings` to fetch the current standings of the Premier League.
    - `/v4/competitions/{id}/scorers` to fetch the top scorers and their performance data.
    - `/v4/teams/{id}` to fetch detailed team information, including coach details.
- **Data Points:** The API provides the following data points:
    - Team Name
    - Played Games
    - Form
    - Wins, Draws, Losses
    - Points
    - Goals For, Goals Against, Goal Difference
    - Coach
    - Top Scorer
    - Goals, Penalties, Assists

## Features
### Data Extraction:
- The scraper sends requests to the football-data.org API to retrieve Premier League standings and player performance data.
- It processes the JSON response to extract relevant data points.
- The data is then combined into a singular DataFrame using `pandas`.

### Data Preprocessing:
- The extracted data is organized into a pandas DataFrame, making it easy to manipulate and analyze.
- The extracted data is formatted, renamed (e.g., changing column names for better readability), and cleaned (e.g., converting data types, handling missing values) before exporting.
- The DataFrame includes columns for each data point provided by the API.

### Data Export:
- The processed data is exported to both Excel and CSV formats.
- This allows users to perform further analysis using spreadsheet software or import the data into other analytical tools.

### Error Handling:
- The scraper includes error handling to manage potential issues such as network errors, rate limits, or invalid API responses.

## Usage
### Prerequisites
- Python 3.8+.
- Install the required libraries: `pip install -r requirements.txt.`
- Create an account on [football-data.org API](https://www.football-data.org/documentation/quickstart).
- Add **API KEY** to `.env` file and assign it to variable called `API_KEY={your-api_key}`.
- Get device and browser details from this site: https://www.whatismybrowser.com.
- Add **USER AGENT** to `.env` file and assign it to variable called `USER_AGENT={your-user-agent}`.

### Running the Scraper

**Using the Jupyter Notebook:**
1. Open `scraper.ipynb` in Jupyter Notebook.
2. Run all cells in the notebook.

**Using the Python Script:**
- Open a terminal or command prompt.
- Navigate to the project directory.
- Run the script: `python scraper.py`
