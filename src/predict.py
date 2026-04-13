import joblib
import numpy as np

# Load model
model = joblib.load('models/model.pkl')

def predict_failure(temperature, vibration, pressure):
    
    # Feature Engineering (same as training)
    temp_vibration_ratio = temperature / vibration
    pressure_temp_ratio = pressure / temperature

    # Input data
    data = np.array([[temperature, vibration, pressure,
                      temp_vibration_ratio, pressure_temp_ratio]])

    # Prediction
    result = model.predict(data)

    return result[0]


# Test prediction
if __name__ == "__main__":
    prediction = predict_failure(80, 25, 110)

    if prediction == 1:
        print("⚠️ High Risk of Failure")
    else:
        print("✅ Machine is Healthy")