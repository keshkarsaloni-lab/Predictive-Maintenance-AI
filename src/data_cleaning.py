import pandas as pd

# Load data
df = pd.read_csv('data/data.csv')

print("Before Cleaning:")
print(df)

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

print("\nAfter Cleaning:")
print(df)

# Check null values
print("\nNull values:")
print(df.isnull().sum())