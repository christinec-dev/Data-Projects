# Fraud Detection: Random Forest Classification

## Description


The purpose of this model is to classify wether or not a transaction is fraudulent. Fraudulent data is determined by the distance the transaction was made from the persons home; distance from last purchase; average purchase total; and if the person used a card, chip, pin or made the purchase at a repeat retailer.

The model employs RandomForest Classification to make these predictions. Random Forest Classification is a machine learning algorithm that uses an ensemble of decision trees to make predictions, particularly for classification tasks. It combines the predictions of multiple, uncorrelated decision trees to improve accuracy and robustness. 

To test the final model, execute `streamlit run app.py`. You can also run it via the deployed model [here]().

## Data Acquisition

The original data aqcuired from Kaggle can be accessed through the link provided below:
- [Download Data](https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud)

### Key Features of the Dataset

- **distance_from_home** - the distance from home where the transaction happened.

- **distance_from_last_transaction** - the distance from last transaction happened.

- **ratio_to_median_purchase_price** - Ratio of purchased price transaction to median purchase price.

- **repeat_retailer** - Is the transaction happened from same retailer.

- **used_chip** - Is the transaction through chip (credit card).

- **used_pin_number** - Is the transaction happened by using PIN number.

- **online_order** - Is the transaction an online order.

- **fraud** - Is the transaction fraudulent.

## Features
- Data cleaning and preprocessing
- Statistical, univariate, and bivariate analysis.
- Visualization of data distributions and relationships.
- Training, evaluation, and deployment of Random Forest model.

## Project Structure
- **data/:** Contains the dataset used for modelling.
- **model/:**
    - `notebook.ipynb`: Jupyter notebook detailing the training process.
    - `requirements.txt`: Requirements for jupyter notebook.
- **app.py**: Streamlit application code for deployment.
- **requirements.txt**: Requirements for streamlit app.
- **README.md:** Project documentation.

## Installation
### Prerequisites
- `Python` Version: 3.13.2 | packaged by Anaconda
- `jupyter` notebook version 7.3.3
- Install the required libraries using: `pip install -r requirements.txt`.

### Running the Notebook

1. Open the `.ipynb` file in Jupyter by running: `jupyter notebook`.
2. Run all cells in the notebook.

## Sample Visualization

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or suggestions, please contact me via the email on my profile or [LinkedIn](https://www.linkedin.com/in/christine-coomans/).