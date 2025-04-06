#  F1 Performance Factors: Exploratory Data Analysis

## Description

The objective of this Exploratory Data Analysis (EDA) is to explore and understand the performance trends of drivers and teams over the 2024 Formula 1 season. The datasets, sourced from [Kaggle](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020?select=results.csv), provides comprehensive information on the Formula 1 races, drivers, constructors, qualifying, circuits, lap times, pit stops, championships from the latest 2024 season. This analysis aims to address questions that will help uncover insights into both individual and team dynamics, as well as broader race strategies.

#### Research Questions
- **Overall Performance:**
    - How many points did each driver score over the season? This helps assess overall performance and consistency.
    - How many races did each driver win? Winning races is a key indicator of a driver's competitiveness.

- **Qualifying vs. Race Performance:** 
    - How does a driver's starting position correlate with their finishing position? This can reveal insights into a driver's ability to improve positions during a race.
    - What is the average starting and finishing position for each driver? This helps identify drivers who consistently outperform their qualifying results.

- **Consistency and Reliability:** 
    - How many races did each driver finish vs. retire? This provides insights into reliability and consistency.
    - What is the distribution of race statuses (e.g., Finished, Retired) for each driver? Understanding race outcomes can highlight reliability issues.

- **Team Dynamics:** 
    - How do drivers within the same team compare in terms of points and wins? This can highlight the impact of driver skill vs. car performance.
    - Which teams have the most consistent driver pairings? Consistency within a team can indicate strong team dynamics and strategy.
        
- **Race-Specific Performance:** 
    - Which tracks or races did each driver perform best at? Identifying strong performances at specific tracks can inform future strategies.
    - How does driver performance vary across different types of tracks (e.g., street circuits vs. traditional tracks)? This can reveal strengths and weaknesses in different racing environments.

- **Strategic Insights**
    - How often did drivers achieve the fastest lap, and how does this correlate with their finishing position? Fastest laps can indicate strong race pace and strategic decisions.
    - What is the correlation between pit stop strategies and race outcomes for each driver? Understanding pit stop impacts can inform strategic decisions.

#### Data Acquisition

The data is compiled from http://ergast.com/mrd/. The data provided by Kaggle can be accessed through the link provided below:
- [Download Data](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020?select=results.csv)

#### Key Features of the Dataset

- **Race, Driver, Team Name**: Represents the race specific values.

- **Rank, Points, Wins, Status, Pit Stops**: Represents the race specific results per driver.

- **Start Position, End Position, Fastest Lap, Fastest Lap Speed, Fastest Time, Pit Stop Time**: Represents the race specific performance values per driver.

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
After running the notebook, you will gain insights into F1 Performance factor trends, including:
- Key performance indicators. 
- Strategic decisions.
- Team dynamics.

## Sample Visualization
![F1 Performance Factors](../images/newplot.png)
![F1 Performance Factors](../images/newplot2.png)
![F1 Performance Factors](../images/image.png)
![F1 Performance Factors](../images/image2.png)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or suggestions, please contact me via the email on my profile or [LinkedIn](https://www.linkedin.com/in/christine-coomans/).
