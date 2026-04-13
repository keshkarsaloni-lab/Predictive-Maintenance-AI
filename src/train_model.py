import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv('data/raw/data.csv')

# Feature Engineering (same as before)
df['temp_vibration_ratio'] = df['temperature'] / df['vibration']
df['pressure_temp_ratio'] = df['pressure'] / df['temperature']

# Define features and target
X = df.drop('failure', axis=1)
y = df['failure']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'models/model.pkl')

print("Model trained successfully ✅")