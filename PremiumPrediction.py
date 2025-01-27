import os
import streamlit as st
import requests
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Load environment variables from .env file (if you use a .env file for other secrets)
load_dotenv()

# Fetch API URL from environment variable
api_url = os.environ.get("API_URL")  # Add your API URL or keep a default for testing

# Fetch Google Credentials JSON from GitHub Secret (passed via environment variable)
google_credentials_json = os.environ.get("GOOGLE_CREDENTIALS_JSON")

# Check if the secret is fetched
if google_credentials_json is None:
    st.error("Google Credentials JSON not found in environment variables.")
else:
    # Load the JSON credentials from the environment variable
    credentials_info = json.loads(google_credentials_json)

    # Set up Google Sheets API credentials using the loaded JSON
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_info, scope)
    client = gspread.authorize(credentials)

    # Open the Google Sheet by title (change to your specific sheet title)
    sheet = client.open("Health Insurance Premium Data").sheet1  # Replace with your sheet name

    # Streamlit UI Setup
    col1, col2, col3 = st.columns([1.5, 5, 1.5])

    with col1:
        st.image("Safety.png", width=100)

    with col2:
        st.title("Health Insurance Premium Predictor")

    with col3:
        st.image("Safety.png", width=100)

    st.markdown("<h6 style='text-align: center;'>Estimate your health insurance premium based on personal and health data.</h6>", unsafe_allow_html=True)

    # Input Form for User Details
    with st.container():
        with st.form(key="insurance_form", clear_on_submit=False):
            st.markdown("<h3 style='text-align: center;'>Enter Your Details</h3>", unsafe_allow_html=True)

            # Form Fields (Age, BMI, Health Conditions)
            col1, col2 = st.columns(2)
            with col1:
                age = st.number_input("Age", min_value=18, max_value=100, step=1, help="Enter your age.")
            with col2:
                bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1, help="Enter your Body Mass Index.")

            col3, col4 = st.columns(2)
            with col3:
                weight = st.number_input("Weight (in kg)", min_value=30, max_value=200, step=1, help="Enter your weight.")
            with col4:
                height = st.number_input("Height (in cm)", min_value=100, max_value=250, step=1, help="Enter your height.")

            # Additional Health Conditions
            col5, col6 = st.columns(2)
            with col5:
                diabetes = st.radio("Do you have diabetes?", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
            with col6:
                blood_pressure = st.radio("Do you have blood pressure problems?", options=[0, 1], format_func=lambda x: "Yes" if x else "No")

            col7, col8 = st.columns(2)
            with col7:
                transplants = st.radio("Have you had any transplants?", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
            with col8:
                chronic_diseases = st.radio("Do you have chronic diseases?", options=[0, 1], format_func=lambda x: "Yes" if x else "No")

            col9, col10 = st.columns(2)
            with col9:
                allergies = st.radio("Do you have allergies?", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
            with col10:
                cancer_history = st.radio("Is there a family history of cancer?", options=[0, 1], format_func=lambda x: "Yes" if x else "No")

            major_surgeries = st.selectbox("How many major surgeries have you had?", options=[0, 1, 2, 3], help="Enter the number of surgeries you've had.")

            # Ensure all required fields are filled
            all_filled = all([age, bmi, weight, height, diabetes is not None, blood_pressure is not None, transplants is not None,
                              chronic_diseases is not None, allergies is not None, cancer_history is not None, major_surgeries is not None])

            # Submit button for prediction
            submit_button = st.form_submit_button(label="Calculate Premium", disabled=not all_filled)

            if submit_button:
                # Prepare data to send to the API
                input_data = {
                    "Age": age,
                    "Diabetes": diabetes,
                    "BloodPressureProblems": blood_pressure,
                    "AnyTransplants": transplants,
                    "AnyChronicDiseases": chronic_diseases,
                    "Height": height,
                    "Weight": weight,
                    "KnownAllergies": allergies,
                    "HistoryOfCancerInFamily": cancer_history,
                    "NumberOfMajorSurgeries": major_surgeries,
                    "BMI": bmi
                }

                # Make a prediction using the API
                try:
                    response = requests.post(api_url, json=input_data)

                    if response.status_code == 200:
                        premium = response.json().get("PredictedPremium")

                        # Display result to the user
                        st.success(f"Predicted Premium Price: {premium}", icon="💸")
                        st.toast(f"Predicted Premium Price: {premium}")

                        # Append the data to the Google Sheet
                        new_data = [
                            [age, bmi, weight, height, diabetes, blood_pressure, transplants, chronic_diseases,
                             allergies, cancer_history, major_surgeries, premium]
                        ]
                        sheet.append_rows(new_data)

                    else:
                        st.error("Failed to retrieve prediction. Please check the API.", icon="❌")

                except Exception as e:
                    st.error(f"Error: {e}", icon="❌")
