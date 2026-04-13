import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load data
df = pd.read_csv('data/data.csv')

# Feature Engineering (same as training)
df['temp_vibration_ratio'] = df['temperature'] / df['vibration']
df['pressure_temp_ratio'] = df['pressure'] / df['temperature']

# Split features and target
X = df.drop('failure', axis=1)
y = df['failure']

# Load trained model
model = joblib.load('models/model.pkl')

# Predict
y_pred = model.predict(X)

# Evaluation
print("Accuracy:", accuracy_score(y, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))