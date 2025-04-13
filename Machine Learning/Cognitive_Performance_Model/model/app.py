import streamlit as st
import joblib
import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Load the trained model
model = joblib.load('cognitive_model.pkl')

# Define user input fields
st.title("Cognitive Performance Prediction")
age = st.number_input("Age", min_value=18, max_value=80, step=1)
gender = st.radio("Gender", ["Male", "Female"])
sleep_duration = st.number_input("Sleep Duration (hours)", min_value=0.0, max_value=24.0, step=0.1)
stress_level = st.slider("Stress Level (1-10)", min_value=1, max_value=10)
diet_type = st.radio("Diet Type", ["Non-Vegetarian", "Vegan", "Vegetarian"])
screen_time = st.number_input("Daily Screen Time (hours)", min_value=0.0, max_value=24.0, step=0.1)
exercise = st.radio("Exercise Frequency", ["Low", "Medium", "High"])
caffeine = st.number_input("Caffeine Intake (mg)", min_value=0, max_value=500, step=1)
reaction_time = st.number_input("Reaction Time (ms)", min_value=200.0, max_value=600.0, step=0.1)
memory_score = st.number_input("Memory Test Score", min_value=0, max_value=100, step=1)

# Predict button
if st.button("Predict"):
    # Create a dictionary with user inputs
    input_dict = {
        'Age': age,
        'Sleep_Duration': sleep_duration,
        'Stress_Level': stress_level,
        'Daily_Screen_Time': screen_time,
        'Caffeine_Intake': caffeine,
        'Reaction_Time': reaction_time,
        'Memory_Test_Score': memory_score,
        'Gender_Female': 1 if gender == "Female" else 0,
        'Gender_Male': 1 if gender == "Male" else 0,
        'Gender_Other': 1 if gender == "Other" else 0,  
        'Diet_Type_Non-Vegetarian': 1 if diet_type == "Non-Vegetarian" else 0,
        'Diet_Type_Vegan': 1 if diet_type == "Vegan" else 0,
        'Diet_Type_Vegetarian': 1 if diet_type == "Vegetarian" else 0,
        'Exercise_Frequency_High': 1 if exercise == "High" else 0,
        'Exercise_Frequency_Low': 1 if exercise == "Low" else 0,
        'Exercise_Frequency_Medium': 1 if exercise == "Medium" else 0
    }

    # Convert to DataFrame to ensure correct feature order
    input_df = pd.DataFrame([input_dict])
    expected_columns = ['Age', 'Sleep_Duration', 'Stress_Level', 'Daily_Screen_Time',
                        'Caffeine_Intake', 'Reaction_Time', 'Memory_Test_Score',
                        'Gender_Female', 'Gender_Male', 'Gender_Other',
                        'Diet_Type_Non-Vegetarian', 'Diet_Type_Vegan', 'Diet_Type_Vegetarian',
                        'Exercise_Frequency_High', 'Exercise_Frequency_Low', 'Exercise_Frequency_Medium']
    input_df = input_df[expected_columns]

    # Make prediction
    prediction = model.predict(input_df)

    # Visualization of prediction
    st.write("## Prediction Analysis")
    col1, col2 = st.columns(2)
    col1.metric("Predicted Cognitive Score", f"{prediction[0]:.2f}")

    # Reaction time analysis (strong negative correlation visible in plot)
    if reaction_time > 500:
        col2.error("⚠️ High reaction time (>500ms) strongly correlates with lower cognitive scores")
    elif reaction_time > 400:
        col2.warning("⚠️ Moderate reaction time may impact cognitive performance")
    else:
        col2.success("✅ Fast reaction time correlates with higher cognitive scores")

    # Additional insights based on visualization relationships
    st.write("### Key Factors Affecting Your Score:")
    factors = []

    # Sleep duration impact
    if sleep_duration < 6:
        factors.append("⚠️ Low sleep duration (<6 hours) may negatively affect cognitive abilities")
    elif sleep_duration > 8:
        factors.append("✅ Optimal sleep duration detected (>8 hours)")
        
    # Memory score analysis (based on the banded distribution)
    if memory_score > 80:
        factors.append("✅ High memory test score strongly supports cognitive performance")
    elif memory_score < 50:
        factors.append("⚠️ Lower memory test scores may indicate cognitive challenges")

    # Stress level impact
    if stress_level > 7:
        factors.append("⚠️ High stress levels can impair cognitive function")
    elif stress_level < 4:
        factors.append("✅ Lower stress levels support better cognitive performance")

    # Screen time analysis
    if screen_time > 8:
        factors.append("⚠️ Extended screen time may contribute to cognitive fatigue")

    # Display all factors as a bulleted list
    for factor in factors:
        st.write(factor)

    # Visualization of where this score falls on distribution
    st.write("### Your Score in Context:")

    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.linspace(0, 100, 1000)
    y = np.exp(-0.5 * ((x - 50) / 15)**2) 
    ax.plot(x, y)
    ax.axvline(x=prediction[0], color='red', linestyle='--')
    ax.fill_between(x[x <= prediction[0]], y[x <= prediction[0]], alpha=0.3, color='red')
    ax.set_xlabel('Cognitive Score')
    ax.set_ylabel('Density')
    ax.set_xlim(0, 100)
    ax.set_title('Your Score Relative to Population Distribution')
    st.pyplot(fig)