# Phishing URL Detection: Random Forest Classification

## Description

The purpose of this model is to classify whether or not a URL is legitimate or a phishing attempt. Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers. In this case, phishing is determined from the URL—analyzing features such as special characters, redirects, SSL certificates, and domain information. Additionally, we complement the model's predictions by testing against VirusTotal results and a whitelist of known legitimate domains. These external verification results are cached for future use, improving efficiency and accuracy in ongoing detection efforts.

The model employs RandomForest Classification to make these predictions. Random Forest Classification is a machine learning algorithm that uses an ensemble of decision trees to make predictions, particularly for classification tasks. It combines the predictions of multiple, uncorrelated decision trees to improve accuracy and robustness. 

To test the final model, execute `streamlit run app.py`. You can also run it via the deployed model [here](https://phishingurlmodel-gpheh7xkq9urwtjkz6eyzm.streamlit.app).

## Data Acquisition

The original data aqcuired from Kaggle can be accessed through the link provided below:
- [Download Data](https://www.kaggle.com/datasets/danielfernandon/web-page-phishing-dataset)

### Key Features of the Dataset

- **url_length**:  The length of the URL.

- **n_slash**: The count of ‘/’ characters in the URL.

- **n_questionmark**: The count of ‘?’ characters in the URL.

- **n_equal**: The count of ‘=’ characters in the URL.

- **n_at**: The count of ‘@’ characters in the URL.

- **n_and**:  The count of ‘&’ characters in the URL.

- **n_exclamation**: The count of ‘!’ characters in the URL.

- **n_asterisk**: The count of ‘*’ characters in the URL.

- **n_hastag**: The count of ‘#’ characters in the URL.

- **n_percent**: The count of ‘%’ characters in the URL.

- **dots_per_length**: The amount of '.' per URL query.

- **hyphens_per_length**: The amount of '-' per URL query.

- **is_long_url**: Is the URL query an abnormally long string.

- **has_many_dots**: Does it have abnomormal amounts of '.'

- **has_ssl**: Does it have an SSL certificate.

- **is_cloudflare_protected**: Is the URL Cloudflare protected.

- **special_char_density**: Ratio of special characters (*&@#) within URL.

- **suspicious_tld_risk**: Risk of URL containing suspicious extensions, domains, and patterns.

- **has_redirects**: Does URL have redirects.

- **risk_score**: Ultimate risk score of URL based on characteristics.

- **url_complexity**: Ultimate URL complexity based on characteristics.

- **phishing**: The Labels of the URL. 1 is phishing and 0 is legitimate.

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
- **streamlit/app.py**: Streamlit application code for deployment.
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
![Screenshot 2025-04-16 153917](https://github.com/user-attachments/assets/4ccf5e2b-29f7-4f8c-8272-fe1e9e7adc08)
![Screenshot 2025-04-16 153848](https://github.com/user-attachments/assets/1b61cbb9-35fc-424d-84dc-efddc6e381a7)
![Screenshot 2025-04-16 153936](https://github.com/user-attachments/assets/469bcf65-c314-4e0c-929e-42e809438c31)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or suggestions, please contact me via the email on my profile or [LinkedIn](https://www.linkedin.com/in/christine-coomans/).
