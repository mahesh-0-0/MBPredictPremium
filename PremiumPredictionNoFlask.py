import streamlit as st
import pandas as pd
import pickle
import warnings
from sklearn.exceptions import InconsistentVersionWarning

# Suppress only the specific warning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

# Load the pre-trained model from the pickle file
with open('final_predict_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title and Description
col1, col2, col3 = st.columns([1.5, 5, 1.5])  # Define relative column width (e.g., 1 for image, 5 for title)

with col1:
    st.image("Safety.png", width=100)  # Image on the left

with col2:
    st.title("MB - Health Insurance Premium Calculator")  # Title on the right

with col3:
    st.image("Safety.png", width=100)  # Image on the left
st.markdown("<h6 style='text-align: center;'>Estimate your insurance premium based on your personal and health data.</h6>", unsafe_allow_html=True)


st.markdown("""<style>.form-container {border-radius: 50px;}</style>""", unsafe_allow_html=True)

# Create a container for the form
with st.container():
    # Apply the border style to the form using a CSS class
    with st.form(key="insurance_form", clear_on_submit=False):

        # Centered Heading for User Details Section
        st.markdown("<h3 style='text-align: center;'>Add your details to get Predicted Premium</h3>", unsafe_allow_html=True)

        # Create two columns side by side for Age and BMI
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("Age", min_value=18, max_value=66, step=1, help="Enter your age (18-66).")
        with col2:
            bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1, help="Enter your Body Mass Index (BMI).")

        # Create another two columns for Weight and Height
        col3, col4 = st.columns(2)

        with col3:
            weight = st.number_input("Weight (in kg)", min_value=30, max_value=200, step=1, help="Enter your weight in kilograms.")
        with col4:
            height = st.number_input("Height (in cm)", min_value=100, max_value=250, step=1, help="Enter your height in centimeters.")

        # Create another two columns for Diabetes and Blood Pressure
        col5, col6 = st.columns(2)

        with col5:
            diabetes = st.radio("Do you have diabetes?", options=[0, 1], format_func=lambda x: "Yes" if x else "No", help="Select 'Yes' if you have diabetes, otherwise select 'No'.")
        with col6:
            blood_pressure = st.radio("Do you have blood pressure problems?", options=[0, 1], format_func=lambda x: "Yes" if x else "No", help="Select 'Yes' if you have blood pressure issues.")

        # Create another two columns for Transplants and Chronic Diseases
        col7, col8 = st.columns(2)

        with col7:
            transplants = st.radio("Have you undergone any transplants?", options=[0, 1], format_func=lambda x: "Yes" if x else "No", help="Select 'Yes' if you've had any transplants.")
        with col8:
            chronic_diseases = st.radio("Do you have any chronic diseases?", options=[0, 1], format_func=lambda x: "Yes" if x else "No", help="Select 'Yes' if you have chronic illnesses.")

        # Create another two columns for Allergies and Cancer History
        col9, col10 = st.columns(2)

        with col9:
            allergies = st.radio("Do you have known allergies?", options=[0, 1], format_func=lambda x: "Yes" if x else "No", help="Select 'Yes' if you have allergies.")
        with col10:
            cancer_history = st.radio("Is there a history of cancer in your family?", options=[0, 1], format_func=lambda x: "Yes" if x else "No", help="Select 'Yes' if there's a family history of cancer.")

        # Create one more field for Major Surgeries
        major_surgeries = st.selectbox("Number of major surgeries", options=[0, 1, 2, 3], help="Enter the number of major surgeries you've had.")

        # Condition to check if all required fields are filled
        all_filled = all([age, bmi, weight, height, diabetes is not None, blood_pressure is not None, transplants is not None,
                          chronic_diseases is not None, allergies is not None, cancer_history is not None, major_surgeries is not None])

        # Submit Button for Prediction (disabled until all fields are filled)
        submit_button = st.form_submit_button(label="Calculate Premium", disabled=not all_filled)

        if submit_button:
            # Prepare input data for the prediction (Make sure to match column names exactly as the model expects)
            # Ensure input data matches the order of features the model was trained with
            input_data = pd.DataFrame({
                'Age': [age],
                'BMI': [bmi],
                'Weight': [weight],
                'Height': [height],
                'Diabetes': [diabetes],
                'BloodPressureProblems': [blood_pressure],   # Rename to match model training
                'AnyTransplants': [transplants],              # Rename to match model training
                'AnyChronicDiseases': [chronic_diseases],     # Rename to match model training
                'KnownAllergies': [allergies],                # Rename to match model training
                'HistoryOfCancerInFamily': [cancer_history],  # Rename to match model training
                'NumberOfMajorSurgeries': [major_surgeries]   # Rename to match model training
            })

            # Reorder columns to match the model's training order
            input_data = input_data[model.feature_names_in_]

            # Make the prediction using the model
            predicted_premium = model.predict(input_data)[0]


            # Show the predicted premium
            st.success(f"Predicted Insurance Premium: {predicted_premium:.2f}", icon="💸")
            st.toast(f"Predicted Insurance Premium: {predicted_premium:.2f}")
            
