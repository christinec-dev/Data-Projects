# Google Job Listings Data Scraper

This project provides a Python-based scraper designed to extract and analyze job listings from the [Google Jobs](www.google.com/about/careers/applications/jobs) website. By automating data collection, this scraper facilitates efficient analysis and visualization of job details, including job titles, companies, locations, and levels. By using libraries like `selenium`, `beautifulsoup4`, and `pandas`, the scraper retrieves, processes, and transforms the data into a structured format for further insights.

**The final exported data can be viewed through two methods:**
- Using the Excel file `data/google_jobs_data.xlsx`
- Utilizing the CSV file `data/google_jobs_data.csv`

**Here is a sample of the data scraped:**
| Title                                      | Link                                           | Company | Location                  | Description                                      | Level    |
|--------------------------------------------|------------------------------------------------|---------|---------------------------|--------------------------------------------------|----------|
| MicroLED Display Product Engineer          | [Link](https://www.google.com/about/careers/applicati...) | Google  | Fremont, CA, USA          | Minimum qualifications: Bachelor’s degree in ...| Mid      |
| Software Engineer III, Infrastructure, Core| [Link](https://www.google.com/about/careers/applicati...) | Google  | Fremont, CA, USA          | Minimum qualifications: Bachelor’s degree or ...| Mid      |
| Staff Systems Development Engineering Manager | [Link](https://www.google.com/about/careers/applicati...) | Google  | Bengaluru, Karnataka, India | Minimum qualifications: Bachelor's degree in ...| Advanced |

## Navigation
1. [Objective](#objective)
2. [Data Source](#data-source)
3. [Features](#features)
4. [Usage](#usage)
5. [Further Exploration](#further-exploration)

## Objective
The primary objective of this scraper is to automate the collection of job listings from the first three pages on the Google Careers website, enabling analysts to efficiently perform in-depth analysis and visualization using tools like pandas and matplotlib.

## Data Source
- **URL:** [Google Careers](www.google.com/about/careers/applications/jobs)
- **Endpoints:** It scrapes the first three pages (`page=n`) of the Google Careers site, and each description link per job application.
- **Data Points:** The scraper provides the following data points:
    - Title
    - Link
    - Company
    - Location
    - Description
    - Level

## Features
### Data Extraction:
- The scraper uses Selenium to navigate through multiple pages of job listings and BeautifulSoup to parse the HTML content.
- It processes the data to extract relevant information such as job titles, companies, locations, and levels.

### Data Preprocessing:
- The extracted data is organized into a pandas DataFrame, making it easy to manipulate and analyze.
- The data is formatted, cleaned, and enriched with additional metrics like word count, sentiment analysis, and user activity.

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
With the data, users can perform a variety of analytics to gain insights into job listings. Here are potential use-cases for the dataset:
- **Location Analysis:** Analyze the distribution of job levels across different locations.
- **Trend Analysis:** Examine trends in job postings to determine which roles are in high demand.
- **Company Insights:** Explore the hiring patterns of different locations based on job listings.