import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_credit_data.csv")

# Display dataset information
print(df.info())

# Summary statistics
print(df.describe())

# Check class distribution (Example: Defaulted vs. Not Defaulted)
print("Class Distribution:\n", df["default"].value_counts())

# Save basic statistics report
with open("reports/EDA_Report.txt", "w") as f:
    f.write(str(df.describe()))

print("EDA report saved.")
