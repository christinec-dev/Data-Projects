# Yield-Boost Playbook: Hotel Revenue Analysis Dashboard

## Project Overview

This project delivers a data-driven revenue optimization playbook for Sunrise Hospitality Group, analyzing booking patterns and revenue opportunities across their Resort Hotel and City Hotel properties. The analysis aims to identify revenue leaks and provide actionable insights for improving RevPAR (Revenue Per Available Room). 

Dataset aqcuired from [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand?select=hotel_bookings.csv). This data set contains booking information for a city hotel and a resort hotel, and includes information such as when the booking was made, length of stay, the number of adults, children, and/or babies, and the number of available parking spaces, among other things.

The dashboard for this project can be viewed on [Tableau](https://public.tableau.com/views/Dashboard_17506986538430/Story?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

## Project Workflow

1. **Data Preparation**: 
   - Created SQL database structure using `create_table_query.sql`
   - Imported raw hotel booking data from CSV
   - Cleaned and processed data (handling null values, standardizing formats) with `table_data_query.sql`
   - Exported final dataset using `export_data_query.sql`

2. **Data Visualization**:
   - Developed interactive Tableau dashboards (`Dashboard.twb`) to analyze key metrics
   - Created visualizations to answer specific business questions
   - Implemented filters for property type, time period, and market segment analysis

## Business Questions & Key Findings

### 1. Cancellation Rates by Lead-Time
- **Resort Hotel**: Exhibits lower cancellation rates (1%, 3%, 6%, 14% across lead-time buckets)
- **City Hotel**: Shows significantly higher cancellation rates (1%, 9%, 19%, 44%), especially for bookings made far in advance

### 2. Average Daily Rate (ADR) Trends
- 2017 rates are lower than 2016 rates during mid-year periods
- Underpricing identified in all months except January-June
- Opportunity for rate optimization in peak seasons

### 3. Distribution Channel Performance
- **GDS**: Consistently highest ADR ($120-$106) from 2015-2017
- **Direct**: Showing positive growth trend ($90 to $107)
- **Corporate**: Consistently lowest performing channel

### 4. No-Show Analysis
- 35 bookings resulted in no-shows despite having deposits
- 1,172 no-shows occurred among bookings without deposits
- Deposit policy effectiveness needs evaluation

### 5. Stay Duration Impact
- Shorter stays have higher cancellation rate (89%) with ADR of $102
- Longer stays (7+ nights) show lower cancellation rate (11%) with slightly higher ADR ($104)

### 6. Repeat Guest Value
- Repeat guests represent only 3% of total bookings vs. 97% for first-timers
- Repeat guests show significantly lower cancellation rate (14% vs. 38%)
- Lower ADR for repeat guests ($64 vs. $103) suggests opportunity for loyalty pricing strategy

### 7. Room Assignment Analysis
- Room type mismatch occurs in 12.5% of bookings
- Correct room assignments show higher ADR ($104 vs. $83)
- Revenue opportunity through improved room inventory management

### 8. Parking Space Correlation
- Parking space requests correlate with 34% higher ADR ($137 vs. $102)
- No significant correlation between parking requests and stay duration
- Opportunity to bundle parking with premium room packages

### 9. Special Requests Analysis
- Individual guests generate substantially more special requests (56,000+) than business guests (2,971)
- Higher ADR ($107) associated with special requests vs. lower ADR ($83-$86) for bookings without requests
- Service personalization opportunities to drive revenue

## Tools & Technologies

- **Database**: MySQL (data storage, cleaning, and preparation)
- **Data Visualization**: Tableau (interactive dashboards and analysis)
- **Project Files**: SQL queries, Tableau workbooks, processed datasets

## Project Structure
```
Hotel_Bookings/
├── Dashboard.twb                 # Main Tableau dashboard file
├── Data/
│   ├── bookings_final.csv        # Processed dataset used for visualization
│   └── hotel_bookings_original.csv # Original data source
├── Queries/
│   ├── create_table_query.sql    # SQL query to create database schema
│   ├── export_data_query.sql     # SQL query to export processed data
│   └── table_data_query.sql      # SQL queries for data cleaning/preparation
└── sunrise-logo.png              # Company logo for dashboard branding
```