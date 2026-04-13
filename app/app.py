import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('models/model.pkl')

st.title("🔧 AI Predictive Maintenance System")

st.write("Enter sensor values to predict machine health")

# Input sliders
temperature = st.slider("Temperature", 0, 100, 50)
vibration = st.slider("Vibration", 1, 50, 10)  # 1 रखा ताकि divide by zero ना हो
pressure = st.slider("Pressure", 50, 200, 100)

if st.button("Predict"):

    # Feature Engineering
    temp_vibration_ratio = temperature / vibration
    pressure_temp_ratio = pressure / temperature

    data = np.array([[temperature, vibration, pressure,
                      temp_vibration_ratio, pressure_temp_ratio]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Failure")
    else:
        st.success("✅ Machine is Healthy")