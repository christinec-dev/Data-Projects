# Cognitive Performance Prediction: Linear Regression Model

**IMPORTANT**: The notebook for this model can be run either via the instructions below, or it can be viewed directly on [Kaggle](https://www.kaggle.com/code/christinecoomans/cognitive-performance-notebook).

## Description

The purpose of this model is to predict users' cognitive performance based on several factors, including hours of sleep, stress levels, diet, exercise, reaction time, and memory test scores. Cognitive performance refers to the efficiency and effectiveness of mental processes such as thinking, learning, memory, problem-solving, and attention. It encompasses the functions that enable individuals to process information and perform tasks.

The model employs Linear Regression to make these predictions. Linear regression estimates the relationship between a dependent variable (cognitive performance) and one or more explanatory variables (such as sleep, exercise, diet, etc.). Cognitive performance is a continuous value, and thus linear regression is well-suited for continuous targets and provides interpretable results. 

To test the final model, execute `streamlit run app.py`. You can also run it via the deployed model [here](https://cognitiveperformancemodel-dlfhuqwmhsjjna6vvzaq2w.streamlit.app).

## Data Acquisition

The original data aqcuired from Kaggle can be accessed through the link provided below:
- [Download Data](https://www.kaggle.com/datasets/samxsam/human-cognitive-performance-analysis)

### Key Features of the Dataset

- **Age:** Age of the user

- **Gender:** Male/Female/Other

- **Sleep_Duration:** Sleep hours per night

- **Stress_Level:** Scale from 1 to 10

- **Diet_Type:** Vegetarian, Non-Vegetarian, Vegan

- **Daily_Screen_Time:** Hours spent on screens daily

- **Exercise_Frequency:** Low, Medium, High

- **Caffeine_Intake:** mg per day

- **Reaction_Time:** Time in milliseconds (ms)

- **Memory_Test_Score:** Score out of 100

- **Cognitive_Score:** ML model’s prediction of cognitive performance

## Features
- Data cleaning and preprocessing
- Statistical, univariate, and bivariate analysis
- Visualization of data distributions and relationships
- Training, evaluation, and deployment of Linear Regression model

## Project Structure
- **data/:** Contains the dataset used for modelling.
- **model/:**
    - `model.ipynb`: Jupyter notebook detailing the training process.
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
![Screenshot 2025-04-13 140018](https://github.com/user-attachments/assets/631e61fd-db89-4aab-aad5-036cda4314fa)
![Screenshot 2025-04-13 140009](https://github.com/user-attachments/assets/30ef8147-134e-4596-9724-d396873e1fdd)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or suggestions, please contact me via the email on my profile or [LinkedIn](https://www.linkedin.com/in/christine-coomans/).
