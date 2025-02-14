import pandas as pd

# Load dataset
df = pd.read_csv("data/credit_data.csv")

# Check missing values
print("Missing Values:\n", df.isnull().sum())

# Fill missing values (Example: Fill numerical columns with median)
df.fillna(df.median(), inplace=True)

# Save cleaned data
df.to_csv("data/cleaned_credit_data.csv", index=False)
print("Data cleaning completed. Saved as 'cleaned_credit_data.csv'")
