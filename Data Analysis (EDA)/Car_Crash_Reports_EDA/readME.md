# Car Crash Factors: Exploratory Data Analysis

**IMPORTANT:** This EDA needs to be run to be able to view the `plotly` graphs in section 7. This can be done either via the instructions below, or it can be viewed directly on [Kaggle](https://www.kaggle.com/code/christinecoomans/car-crash-reports-eda). 

## Description

The objective of this Exploratory Data Analysis (EDA) is to explore and understand the factors influencing vehicle accidents. The dataset, sourced from [Data.Gov](https://catalog.data.gov/dataset/crash-reporting-drivers-data), provides comprehensive information on road accidents, such as collision severity, weather conditions, road types, and contributing elements, offering valuable insights for the analysis and enhancement of overall road safety measures.

### Research Questions
- **Route Types and Accidents:**
    - Which route types have the highest frequency of accidents?

- **Car Types in Accidents:**
    - What are the most common car types involved in accidents?

- **Frequency of Accidents:**
    - Are certain car types more likely to be involved in accidents at specific times of the day or week?

- **Agency and Substance-Induced Incidents:**
    - Are there specific times or conditions under which substance-induced incidents are more prevalent?

- **Environmental Conditions and Crash Frequency:**
    - How do different weather conditions affect the frequency and severity of crashes?

- **Vehicle Movement vs. Collision Type:**
    - How does vehicle movement at the time of the accident affect the severity of the collision?
    - 
## Data Acquisition

The data provided by Data.Gov can be accessed through the link provided below:
- [Download Data](https://catalog.data.gov/dataset/crash-reporting-drivers-data)

#### Key Features of the Dataset

- Agency Name	
- ACRS Report Type	
- Crash Date/Time	
- Route Type	
- Collision Type	
- Weather	Surface Condition	
- Driver Substance Abuse	
- Vehicle Damage Extent	
- Vehicle Body Type	
- Vehicle Movement	
- Speed Limit	
- Vehicle Make	
- Vehicle Model	
- Latitude	
- Longitude

### Notice
Please note that the dataset is highly biased, primarily concerning Monroe County. This data does not accurately represent all car crashes overall.

## Features
- Data cleaning and preprocessing
- Statistical, univariate, and bivariate analysis
- Visualization of data distributions and relationships
- Interactive plots using Plotly

## Project Structure
- **data/:** Contains the dataset used for analysis.
- **data/Exported:** Contains the final datasets created during analysis.
- **notebooks/:** Jupyter notebooks with the EDA process.
- **images/:** Saved plots and visualizations.
- **README.md:** Project documentation.

## Installation
### Prerequisites
- `Python` Version: 3.13.2 | packaged by Anaconda
- `jupyter` notebook version 7.3.3
- Install the required libraries using: `pip install -r requirements.txt`.

### Running the Notebook

1. Open the `.ipynb` file in Jupyter by running: `jupyter notebook`.
2. Run all cells in the notebook.

## Usage
This EDA can help uncover meaningful insights into the multifaceted nature of vehicle accidents, including route types, vehicle characteristics, and environmental conditions. By leveraging these insights, policymakers and transportation authorities can implement targeted interventions to enhance road safety, reduce accident rates, and minimize injury severity.

## Sample Visualization
![newplot2](https://github.com/user-attachments/assets/d551bb96-9642-4d51-8f8f-fd73a781ab4f)
![newplot](https://github.com/user-attachments/assets/a5c63635-f618-4454-a9bc-7c2bac3cd3ad)
![newplot4](https://github.com/user-attachments/assets/c9687c0c-c804-40c4-8471-14caa3594641)
![newplot3](https://github.com/user-attachments/assets/d24d9805-9316-42e0-8150-f241eb34d33b)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or suggestions, please contact me via the email on my profile or [LinkedIn](https://www.linkedin.com/in/christine-coomans/).
