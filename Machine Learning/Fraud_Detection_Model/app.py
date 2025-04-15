import streamlit as st
import joblib
import pandas as pd

def apply_fraud_rules(transaction):
    """Apply rule-based checks to identify potentially fraudulent transactions."""
    rules_triggered = []
    # Rule 1: High distance from home
    if transaction['distance_from_home'] > 50:
        rules_triggered.append("High distance from home location")
    
    # Rule 2: Large distance gap from last transaction
    if transaction['distance_from_last_transaction'] > 20:
        rules_triggered.append("Unusual distance from last transaction")
    
    # Rule 3: Unusual purchase amount
    if transaction['ratio_to_median_purchase_price'] > 5:
        rules_triggered.append("Purchase amount significantly higher than usual")
    
    # Rule 4: Risky transaction pattern
    if (transaction['online_order'] == 1 and 
        transaction['repeat_retailer'] == 0 and 
        transaction['used_chip'] == 0):
        rules_triggered.append("Online order at new retailer without chip")
    
    return rules_triggered

def evaluate_transaction(transaction_data, ml_prediction):
    """Combine ML predictions with rule-based evaluation."""
    rules_triggered = apply_fraud_rules(transaction_data)
    # Final risk assessment (fraud/non-fraud)
    if ml_prediction == 1 or len(rules_triggered) >= 1:
        return True, rules_triggered 
    else:
        return False, rules_triggered 

# Load the trained model
model = joblib.load('fraud_detection_model.pkl')

# Title and sidebar of the app
st.title("Fraud Detection App")
st.sidebar.header("Input Option")
input_option = st.sidebar.radio("Choose how to provide input:", ("Manual Input", "Upload File"))

# Option to download test data for testing
test_data = pd.DataFrame({
    'distance_from_home': [5, 10, 15, 100, 150, 200, 7, 12, 8, 20, 18, 120, 180, 250, 300, 400],
    'distance_from_last_transaction': [0.5, 1, 1.5, 50, 75, 100, 0.7, 0.9, 1.2, 2, 1.8, 60, 90, 120, 150, 200],
    'ratio_to_median_purchase_price': [1, 1.2, 0.8, 10, 15, 20, 1.1, 0.9, 1.3, 1, 1.1, 12, 18, 25, 30, 40],
    'repeat_retailer': [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    'used_chip': [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    'used_pin_number': [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    'online_order': [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
})
csv = test_data.to_csv(index=False).encode('utf-8')
st.sidebar.header("Download Example Test Data")
st.sidebar.download_button(
    label="Download Example CSV",
    data=csv,
    file_name='test_transactions.csv',
    mime='text/csv'
)

# Rule threshold controls
st.sidebar.header("Rule Settings")
st.sidebar.write("Adjust thresholds for rule-based detection:")

distance_threshold = st.sidebar.slider(
    "Distance from home threshold (miles)", 
    min_value=10, max_value=200, value=50
)
transaction_distance_threshold = st.sidebar.slider(
    "Distance from last transaction threshold", 
    min_value=5, max_value=100, value=20
)
purchase_ratio_threshold = st.sidebar.slider(
    "Purchase ratio threshold", 
    min_value=2.0, max_value=20.0, value=5.0, step=0.5
)

# Update rule function to use custom thresholds
def apply_fraud_rules(transaction):
    rules_triggered = []
    
    if transaction['distance_from_home'] > distance_threshold:
        rules_triggered.append(f"Distance from home > {distance_threshold}")
    if transaction['distance_from_last_transaction'] > transaction_distance_threshold:
        rules_triggered.append(f"Distance from last transaction > {transaction_distance_threshold}")
    if transaction['ratio_to_median_purchase_price'] > purchase_ratio_threshold:
        rules_triggered.append(f"Purchase ratio > {purchase_ratio_threshold}")
    if (transaction['online_order'] == 1 and 
        transaction['repeat_retailer'] == 0 and 
        transaction['used_chip'] == 0):
        rules_triggered.append("Online order at new retailer without chip")
    
    return rules_triggered

# File Upload Option
if input_option == "Upload File":
    st.header("Upload a CSV File")
    uploaded_file = st.file_uploader("Choose a file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the uploaded CSV file into a DataFrame
        input_data = pd.read_csv(uploaded_file)
        
        # Display the uploaded data
        st.write("Uploaded Data:")
        st.dataframe(input_data)
        
        # Check if the required columns are present
        required_columns = [
            'distance_from_home', 
            'distance_from_last_transaction', 
            'ratio_to_median_purchase_price', 
            'repeat_retailer', 
            'used_chip', 
            'used_pin_number', 
            'online_order'
        ]
        
        if all(col in input_data.columns for col in required_columns):
            # ML model predictions
            ml_predictions = model.predict(input_data)
            
            # Apply rule-based system to each transaction
            rule_results = []
            final_predictions = []
            triggered_rules_list = []
            
            for i, row in input_data.iterrows():
                is_fraudulent, rules = evaluate_transaction(row, ml_predictions[i])
                final_predictions.append(1 if is_fraudulent else 0)
                rule_results.append("Yes" if rules else "No")
                triggered_rules_list.append("; ".join(rules) if rules else "None")
            
            # Add predictions and explanations to DataFrame
            input_data['ML_Prediction'] = ml_predictions
            input_data['Rules_Triggered'] = rule_results
            input_data['Triggered_Rules'] = triggered_rules_list
            input_data['Final_Prediction'] = final_predictions
            
            # Display results
            st.write("Prediction Results:")
            st.dataframe(input_data)
            
            # Summary statistics
            ml_flagged = sum(ml_predictions)
            rule_flagged = sum(1 for r in rule_results if r == "Yes")
            total_flagged = sum(final_predictions)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("ML Model Flagged", f"{ml_flagged} transactions")
            with col2:
                st.metric("Rules Flagged", f"{rule_flagged} transactions")
            with col3:
                st.metric("Total Flagged", f"{total_flagged} transactions")
            
            # Option to download results
            csv = input_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Predictions as CSV",
                data=csv,
                file_name="predictions_with_rules.csv",
                mime="text/csv",
            )

# Manual Input Option
elif input_option == "Manual Input":
    st.header("Enter Transaction Details")
    distance_from_home = st.number_input("Distance from Home", min_value=0.0, step=0.1)
    distance_from_last_transaction = st.number_input("Distance from Last Transaction", min_value=0.0, step=0.1)
    ratio_to_median_purchase_price = st.number_input("Ratio to Median Purchase Price", min_value=0.0, step=0.1)
    repeat_retailer = st.selectbox("Repeat Retailer (1 = Yes, 0 = No)", [1, 0])
    used_chip = st.selectbox("Used Chip (1 = Yes, 0 = No)", [1, 0])
    used_pin_number = st.selectbox("Used PIN Number (1 = Yes, 0 = No)", [1, 0])
    online_order = st.selectbox("Online Order (1 = Yes, 0 = No)", [1, 0])

    # Predict button
    if st.button("Predict"):
        # Prepare the input data as a DataFrame
        input_data = pd.DataFrame({
            'distance_from_home': [distance_from_home],
            'distance_from_last_transaction': [distance_from_last_transaction],
            'ratio_to_median_purchase_price': [ratio_to_median_purchase_price],
            'repeat_retailer': [repeat_retailer],
            'used_chip': [used_chip],
            'used_pin_number': [used_pin_number],
            'online_order': [online_order]
        })
        
        # ML model prediction
        ml_prediction = model.predict(input_data)[0]
        
        # Apply rule-based evaluation
        is_fraudulent, rules_triggered = evaluate_transaction(input_data.iloc[0], ml_prediction)
        
        # Display results with detailed explanation
        if is_fraudulent:
            st.error("⚠️ This transaction is flagged as potentially fraudulent!")
            
            # Explain why it was flagged
            if ml_prediction == 1:
                st.warning("• ML Model flagged this transaction as fraudulent")
            
            if rules_triggered:
                st.warning("• Rule-based checks identified risk factors:")
                for rule in rules_triggered:
                    st.write(f"  - {rule}")
        else:
            st.success("✅ This transaction appears to be legitimate.")
            
            if rules_triggered:
                st.info("Note: Some risk factors were identified, but not enough to flag the transaction:")
                for rule in rules_triggered:
                    st.write(f"  - {rule}")
