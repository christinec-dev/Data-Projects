# McDonald's U.S. Operations Analysis

## Project Overview

This repository contains a data analysis project for McDonald's U.S. Operations. The analysis focuses on customer reviews across McDonald's locations in the United States, identifying which stores delight customers, which ones hurt the brand, and what operational factors might explain the differences.

View the Tableau dashboard created for this [here](https://public.tableau.com/shared/GSSMTK3FR?:display_count=n&:origin=viz_share_link).

## Business Context

This analysis was prepared for the VP of Operations who requested a quarterly report on store performance as measured through customer reviews. The report aims to:
- Benchmark current performance against historical data
- Identify regional variations in customer satisfaction
- Flag underperforming stores with high visibility
- Track performance trends over time
- Identify stores with inconsistent customer experiences
- Explore relationships between review volume and ratings
- Measure performance against corporate goals

## Dataset

The dataset includes over 33,000 anonymized reviews of McDonald's stores in the United States, scraped from Google reviews. It contains valuable customer experience data including:
- Store names
- Categories
- Addresses
- Geographic coordinates
- Review ratings
- Review texts
- Timestamps

Data source: [Kaggle - McDonald's Store Reviews](https://www.kaggle.com/datasets/nelgiriyewithana/mcdonalds-store-reviews)

## Repository Structure

```
/
├── Dashboard.twb              # Tableau workbook with visualizations
├── Data/
│   ├── reviews_final.csv      # Cleaned review data
│   └── reviews_original.csv   # Original review data
└── queries/
    ├── data_cleaning_query.sql    # SQL query for data cleaning
    ├── data_export_query.sql      # SQL query for exporting data
    └── table_creator_query.sql    # SQL query for table creation
```

## Key Findings

### 1. Company-wide average star rating
**Finding:** Current quarter average: 3.0 stars
**Comparison:** 0.2 stars lower than same quarter last year

### 2. States with significant rating deviations
**Finding:** Overall average rating is 3.1 stars
**Outliers:**
- Below average: Florida (2.87), Utah (2.53)
- Above average: Washington D.C. (3.7, 3.5)

### 3. Underperforming high-visibility stores
Top 10 stores by review count with ratings below 3 stars:
1. 151 West 34th Street, New York (1.9)
2. 1650 Washington Ave, Miami, Florida (2.0)
3. 160 Broadway, New York (2.3)
4. 501 W Imperial Hwy, Los Angeles (2.5)
5. 219 5th Street, Salt Lake City, UT (2.5)
6. 3501 Biscayne Blvd, Miami, Florida (2.6)
7. 9814 International Dr, Orlando, Florida (2.6)
8. 8500 Austin, Texas (2.7)
9. 555 13th Street, Washington D.C. (2.7)
10. 5725 W Irlo Bronson Memorial Hwy, Kissimmee, Florida (2.8)

### 4. Month-to-month rating trends
**Finding:** Ratings are declining slightly nationwide

### 5. Stores with largest rating variability
Stores with highest standard deviation in ratings:
1. 10451 Santa Monica Blvd, Los Angeles
2. 160 Broadway, New York
3. 114 Delancey Street, New York

### 6. Relationship between review count and rating
**Finding:** No significant correlation (p-value: 0.52)
Trendline shows slight downward slope, but no clear clusters as ratings vary widely per review count

### 7. Corporate goal achievement
**Finding:** Only 13% of stores met the corporate goal of ≥ 4.0 stars this quarter

## Technologies Used
- SQL for data preparation and cleaning
- Tableau for data visualization and analysis
- Jupyter Notebook for data exploration

## Contact Information

For questions or further information about this analysis, please contact the McDonald's U.S. Operations data analytics team.
