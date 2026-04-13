import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/raw/data.csv')

# Count failure values
counts = df['failure'].value_counts()

# Plot graph
counts.plot(kind='bar')

plt.title("Failure Distribution")
plt.xlabel("Failure (0 = No, 1 = Yes)")
plt.ylabel("Count")

plt.show()