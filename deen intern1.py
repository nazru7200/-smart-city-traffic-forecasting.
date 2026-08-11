# ================================
# Smart City Traffic Forecasting
# Step 1: Load Test Dataset
# ================================

import pandas as pd

# Load dataset
df = pd.read_csv("f:/cse4/Downloads/datasets_8494_11879_test_BdBKkAj.csv")

# Display first 5 rows
print("First 5 Rows")
print(df.head())

# Dataset information
print("\nDataset Information")
print(df.info())

# Dataset shape
print("\nRows and Columns")
print(df.shape)

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Convert DateTime column
df["DateTime"] = pd.to_datetime(df["DateTime"])

# Create new features
df["Year"] = df["DateTime"].dt.year
df["Month"] = df["DateTime"].dt.month
df["Day"] = df["DateTime"].dt.day
df["Hour"] = df["DateTime"].dt.hour
df["DayOfWeek"] = df["DateTime"].dt.dayofweek

print("\nUpdated Dataset")
print(df.head())

# Save processed dataset
df.to_csv("f:/cse4/Downloads/datasets_8494_11879_test_BdBKkAj.csv", index=False)

print("\nProcessed dataset saved successfully!")

 