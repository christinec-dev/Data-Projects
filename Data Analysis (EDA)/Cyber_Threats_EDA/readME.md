# Cybersecurity Threats (2015-2019): Exploratory Data Analysis

**IMPORTANT:** This EDA needs to be run to be able to view the `plotly` graphs in section 7. This can be done either via the instructions below, or it can be viewed directly on [Kaggle](https://www.kaggle.com/code/christinecoomans/cybersecurity-threats-205-2024-eda). 

## Description

The goal of this Exploratory Data Analysis (EDA) is to obtain insights into cybersecurity threats from 2015 to 2024. The dataset, sourced from [Kaggle](https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024), includes general trends, financial impacts, resolution times, vulnerabilities, defense mechanisms, and comparative aspects of threats during this period.

### Research Questions

**General Trends and Patterns**
- How has the frequency of different attack types evolved over the years?
- Which countries experience the highest number of cyberattacks, and how do they compare in terms of financial loss?
- What are the most common security vulnerabilities exploited in each industry?

**Financial Impact**
- Which attack types result in the highest financial losses on average?
- Is there a relationship between the number of affected users and financial loss for different attack types?
- How does financial loss vary by target industry and country?

**3. Resolution Time**
- Does the resolution time vary significantly across different attack types or defense mechanisms used?
- Are certain industries better at resolving incidents quickly compared to others?

**Vulnerabilities and Defense Mechanisms**
- What are the most common security vulnerabilities exploited by different attack sources (e.g., nation-state vs hacker group)?
- Which defense mechanisms are most commonly used for specific vulnerabilities, and how effective are they (e.g., based on resolution time)?

**Temporal Analysis**
- Are there any noticeable trends in the number of incidents or financial losses over time (e.g., pre-2020 vs post-2020)?
- Do certain attack types or vulnerabilities show seasonal or yearly patterns?

**Industry-Specific Insights**
- Which industries are most targeted by specific attack types (e.g., healthcare for ransomware)?
- How do industries differ in their choice of defense mechanisms?

**Comparative Analysis**
- How do nation-state attacks differ from hacker group attacks in terms of financial loss, affected users, and resolution time?
- Are there differences in attack patterns between developed countries (e.g., USA) and developing countries (e.g., Brazil)?

## Data Acquisition

The data provided by Kaggle can be accessed through the link provided below:
- [Download Data](https://www.kaggle.com/datasets/atharvasoundankar/global-cybersecurity-threats-2015-2024)

### Key Features of the Dataset

- **Country:** Country where the attack occurred.

- **Year:** Year of the incident.

- **Attack Type:** Method of attack (e.g., Phishing, SQL Injection).

- **Target Industry:** Industry targeted (e.g., Finance, Healthcare).

- **Number of Affected Users:** Volume of users impacted.

- **Financial Impact ($M):** Estimated financial loss in millions.

- **Response Time (Hours):** Time taken to mitigate the attack.

- **Defense Mechanism Used:** Countermeasures taken.

### Notice
The dataset analyzed in this study is extremely uniform. This narrow perspective may overlook diverse cybersecurity practices, regional variations, and the effectiveness of specific tools. Further research with enriched and more detailed data is essential to overcome these limitations and gain a deeper, more nuanced understanding of the cyber threat landscape.

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
These findings can guide strategic decision-making to mitigate the financial and operational impacts of cyber threats effectively.

## Sample Visualization
![output](https://github.com/user-attachments/assets/e16f91a9-1108-49ff-994c-963d0877819c)
![newplot2](https://github.com/user-attachments/assets/f95914be-e467-4247-a503-e528093a41c6)
![newplot](https://github.com/user-attachments/assets/ddba26d8-2ae1-4211-89fa-c251debbd85b)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or suggestions, please contact me via the email on my profile or [LinkedIn](https://www.linkedin.com/in/christine-coomans/).
