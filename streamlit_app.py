import streamlit as st
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Predictive Maintenance App-Final",
    page_icon="⚙️",
    layout="centered"
)

<<<<<<< HEAD
st.title("⚙️ Engine Predictive Maintenance-Final")
=======
st.title("⚙️ Engine Predictive Maintenance")
>>>>>>> f75ee2101813f33191db588c827ba84fa8fa77b8
st.write("Enter the engine sensor readings to predict if maintenance is required.")

# --- Load the Model ---
@st.cache_resource
def load_model():
<<<<<<< HEAD
    repo_id = "Sirisha335/Predictive_Maintaince_final" # Your Hugging Face dataset repo ID
=======
    repo_id = "Sirisha335/Predictive_Maintaince" # Your Hugging Face dataset repo ID
>>>>>>> f75ee2101813f33191db588c827ba84fa8fa77b8
    model_filename = "models/best_random_forest_model.joblib" # Path in repo

    # Ensure the Hugging Face token is set if the model is private or requires authentication
    # In a deployed Hugging Face Space, you would set this as a Space secret.
    # For local testing, you might set it as an environment variable or uncomment below:
    # os.environ['HF_TOKEN'] = 'your_hugging_face_token'

    try:
        model_path = hf_hub_download(repo_id=repo_id, filename=model_filename, repo_type="dataset")
        model = joblib.load(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

model = load_model()

# --- Input Features ---
st.header("Engine Sensor Readings")

engine_rpm = st.slider("Engine RPM", min_value=0, max_value=2500, value=750, step=10)
lub_oil_pressure = st.slider("Lub Oil Pressure (bar)", min_value=0.0, max_value=8.0, value=3.0, step=0.1)
fuel_pressure = st.slider("Fuel Pressure (bar)", min_value=0.0, max_value=25.0, value=6.0, step=0.1)
coolant_pressure = st.slider("Coolant Pressure (bar)", min_value=0.0, max_value=8.0, value=2.0, step=0.1)
coolant_temp = st.slider("Coolant Temperature (°C)", min_value=60.0, max_value=130.0, value=80.0, step=0.1) # Capped at 120

# Create a DataFrame for prediction
input_data = pd.DataFrame([[
    engine_rpm, lub_oil_pressure, fuel_pressure, coolant_pressure, coolant_temp
]], columns=[
    'Engine rpm', 'Lub oil pressure', 'Fuel pressure', 'Coolant pressure', 'Coolant temp'
])

# --- Prediction ---
if st.button("Predict Engine Condition"): # Simplified button text
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]

    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f"⚠️ **Maintenance Required!** (Faulty Engine Predicted)")
        st.write(f"Confidence (Faulty): **{prediction_proba[1]*100:.2f}%**")
        st.write(f"Confidence (Normal): {prediction_proba[0]*100:.2f}%")
        st.warning("Immediate inspection and maintenance are recommended.")
    else:
        st.success(f"✅ **Engine Condition: Normal**")
        st.write(f"Confidence (Normal): **{prediction_proba[0]*100:.2f}%**")
        st.write(f"Confidence (Faulty): {prediction_proba[1]*100:.2f}%")
        st.info("Continue regular monitoring.")

st.markdown("---")
st.caption("This application predicts engine condition based on sensor readings using a pre-trained Random Forest Classifier.")
