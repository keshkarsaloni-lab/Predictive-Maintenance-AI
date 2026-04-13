import pandas as pd

# Load data
df = pd.read_csv('data/data.csv')

print("Before Feature Engineering:")
print(df.head())

# Create new feature
df['temp_vibration_ratio'] = df['temperature'] / df['vibration']

# Optional: another feature
df['pressure_temp_ratio'] = df['pressure'] / df['temperature']

print("\nAfter Feature Engineering:")
print(df.head())