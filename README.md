# Predicting Health Insurance Premium Prices Using Machine Learning

## Target Metric
- The target variable for this project is the insurance premium price (PremiumPrice), a continuous numeric value that represents the cost of an individual's health insurance.
- Key performance metrics used to evaluate the models are:
  - R² Score: Indicates how well the model explains the variance in the data.
  - Mean Absolute Error (MAE): Measures the average absolute difference between predicted and actual values.
  - Root Mean Squared Error (RMSE): Provides a measure of the average squared error, giving more weight to larger errors.

## Steps Taken to Solve the Problem
### **1. Tableau Visualization**
#### Key Features  
- **Premium Trends:** Analysis of average premium price, age distribution, and health risk factors.  
- **Health Condition Impact:** Breakdown of premiums based on conditions like diabetes, BP issues, chronic diseases, and surgeries.  
- **Age & BMI Influence:** Visualization of premium variations across age groups and BMI categories.  
- **Surgical & Transplant Impact:** Comparative premium costs for individuals with major surgeries and transplants.
    
### **2. Exploratory Data Analysis (EDA) and Hypothesis Testing**
#### EDA Approaches  
- **Distribution Analysis:** Additional visualizations beyond Tableau to explore data distribution.  
- **Correlation Analysis:** Heatmap to identify relationships between premium prices and predictors.  
- **Outlier Detection:** Using IQR to detect and assess outliers.  

#### Hypothesis Testing  
- **T-tests/ANOVA:** Comparing premium means across categories.  
- **Chi-square Test:** Evaluating associations between categorical health factors.  
- **Regression Analysis:** Applying linear models to assess premium price determinants.
  
### **3. ML Modeling**
#### Data Preprocessing:
1. **Handling Missing Values**: Prepares strategies for missing data (though initial checks may not show missing values).
2. **Feature Engineering**: Creates new features like Body Mass Index (BMI) from height and weight to improve model performance.
3. **Scaling and Encoding**: Applies scaling to numerical features and encoding to categorical features for machine learning models.

#### Model Selection:
1. **Linear Regression**: Establishes a baseline prediction model.
2. **Tree-based Models**: Implements Decision Trees, Random Forests, and Gradient Boosting Machines for handling non-linear relationships and feature importance analysis.

#### Model Evaluation and Validation:
1. **Cross-Validation**: Uses k-fold cross-validation to evaluate model performance on different subsets.
2. **Performance Metrics**: Evaluates models with RMSE, MAE, and R² depending on business objectives.
3. **Confidence/Prediction Intervals**: Provides prediction intervals to assess model reliability.

#### Interpretability and Explainability:
1. **Feature Importance**: Uses permutation importance and SHAP values for model explainability.
2. **Model Insights**: Delivers actionable insights on factors influencing insurance premiums, helping with targeted interventions.

### **4. Web-Based Calculator for Estimating Insurance Premiums**
#### API Development with Flask:
1. **Flask Setup**: Creates a backend using Flask to handle incoming requests and process data through the machine learning model.
2. **Endpoint Creation**: Implements API endpoints that receive user inputs as JSON and return estimated premium predictions.
3. **Model Integration**: Integrates the trained machine learning model with Flask, allowing it to process user inputs and provide premium predictions.

#### Streamlit Application:
1. **Streamlit Setup**: Develops a user-friendly interface for interacting with the model.
2. **User Input Forms**: Utilizes Streamlit widgets to collect user inputs (age, BMI, health conditions, etc.).
3. **Model Invocation**: Connects the input data to the machine learning model and displays premium predictions directly in the application.

## Final Model Scores:
### Random Forest Model:
- **R² Score (Train)**: 0.8727 — Indicates the model explains 87.27% of the variance in the training data.
- **Train MAE (Mean Absolute Error)**: 900.22 — Suggests an average prediction error of 900.22 units on the training data.
- **Train RMSE (Root Mean Squared Error)**: 2165.04 — Shows the average squared difference between predicted and actual values during training.

- **R² Score (Test)**: 0.8775 — Indicates the model explains 87.75% of the variance in the test data.
- **Test MAE (Mean Absolute Error)**: 1099.30 — Suggests an average prediction error of 1099.30 units on the test data.
- **Test RMSE (Root Mean Squared Error)**: 2317.51 — Shows the average squared difference between predicted and actual values during testing.


## Deployment Steps:
1. **Model Training**: A machine learning model (e.g., Random Forest or Gradient Boosting) was trained on preprocessed data to predict health insurance premiums.
2. **API Development**:
   - Flask was used to create an API that handles user requests and returns predictions based on the model.
   - Endpoints were set up to accept user inputs (e.g., age, health conditions) and return estimated premiums.
3. **Streamlit Front-End**:
   - A Streamlit app was created to allow users to input their data via forms and view predicted premiums in real-time.
   - The model is invoked directly from the front-end to display results instantly.
4. **Deployment**: 
   - Deployed the Flask API and Streamlit app on platforms using Render for accessible, real-time predictions.

## Links:
- Tableau Dashboard: https://public.tableau.com/views/MB-HealthInsurancePremiumAnalysis/InsuranceAnalyticsDashboard
- EDA Colab: https://colab.research.google.com/drive/1MRIVJ1Ur4IBxV5HIcfl8IcBqnOfFwZZ5?usp=sharing
- ML Modeling Colab: https://colab.research.google.com/drive/1YI6QgjxhQPI62_TeCCY0xGLI-uYV5uvJ
- App URL without Flask API(Streamlit): https://premiumpredictionwala.streamlit.app/
- Render Dashboard: https://premiumpredictionwala.onrender.com
- App URL with Flask API(Streamlit): https://premiumpricepredictionwala.streamlit.app/
