# Amazon Sales 2025: Exploratory Data Analysis

**IMPORTANT:** This EDA needs to be run to be able to view the `plotly` graphs in section 7. This can be done either via the instructions below, or it can be viewed directly on [Kaggle](https://www.kaggle.com/code/christinecoomans/amazon-sales-2025-eda). 

## Description

The objective of this Exploratory Data Analysis (EDA) is to gain valuable insights into sales performance, product trends, customer behavior, and operational dynamics of Amazon sales for 2025. The dataset, sourced from [Kaggle](https://www.kaggle.com/datasets/zahidmughal2343/amazon-sales-2025), contains 250 records of Amazon sales transactions, including details about the products sold, customers, payment methods, and order statuses.

### Research Questions

**1. Sales Performance Over Time**

- How do total sales vary over time? Are there any noticeable trends or seasonal patterns in sales?
- What are the peak sales days or months, and what might be driving these peaks?

**2. Product and Category Analysis**

- Which products are the best sellers, and how do they compare across different categories?
- Are there any categories that consistently outperform others in terms of total sales?

**3. Customer Behavior and Preferences**

- What are the most common payment methods used by customers, and how do they correlate with the order status (e.g., completed, pending, cancelled)?
- How do customer locations affect purchasing behavior? Are there regions with higher sales volumes or specific product preferences?

**4. Order and Transaction Analysis**

- What is the average order value, and how does it vary across different categories and payment methods?
- How does the quantity of products purchased affect total sales and order status?

**5. Order Status Insights**

- What percentage of orders are completed, pending, or cancelled, and what factors might influence these statuses?
- Are there specific products or categories with higher cancellation rates?

**6. Price and Quantity Relationship**

- How does the price of products relate to the quantity purchased? Are there any patterns indicating bulk purchases or discounts?

**7. Customer Segmentation**

- Can we segment customers based on their purchasing behavior, such as frequent buyers, high spenders, or category-specific shoppers?

## Data Acquisition

The data provided by Kaggle can be accessed through the link provided below:
- [Download Data](https://www.kaggle.com/datasets/zahidmughal2343/amazon-sales-2025)

### Key Features of the Dataset

- **Order ID:** Unique identifier for each order (e.g., ORD0001).

- **Date:** Date of the order.

- **Product:** Name of the product purchased.

- **Category:** Product category (Electronics, Clothing, Home Appliances, etc.).

- **Price:** Price of a single unit of the product.

- **Quantity:** Number of units purchased in the order.

- **Total Sales:** Total revenue from the order (Price × Quantity).

- **Customer Name:** Name of the customer.

- **Customer Location:** City where the customer is based.

- **Payment Method:** Mode of payment (Credit Card, Debit Card, PayPal, etc.).

- **Status:** Order status (Completed, Pending, or Cancelled).

### Notice
The dataset analyzed in this study is highly biased, as it covers only a small percentage of Amazon's total sales, categories, and products. Consequently, the findings may not accurately represent the broader trends or dynamics of Amazon's e-commerce operations. This data should be used with caution and treated as indicative rather than definitive. It provides a narrow perspective that may overlook diverse customer behaviors, regional variations, and product performance across the platform.

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
These findings can guide strategic decision-making to optimize sales and enhance customer satisfaction.

## Sample Visualization
![newplot](https://github.com/user-attachments/assets/d9df88c3-ad6f-4f25-8207-b79df3186c67)
![output2](https://github.com/user-attachments/assets/438b703f-3df5-4792-93bd-353e78d9b1ed)
![output](https://github.com/user-attachments/assets/78a3ab76-6526-420f-aca6-ef4dcbf61a29)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or suggestions, please contact me via the email on my profile or [LinkedIn](https://www.linkedin.com/in/christine-coomans/).
