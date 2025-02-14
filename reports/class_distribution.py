import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv("data/cleaned_credit_data.csv")

# Create count plot
plt.figure(figsize=(6,4))
sns.countplot(x="default", data=df, palette="coolwarm")
plt.title("Loan Default Distribution")
plt.xlabel("Default (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.savefig("reports/class_distribution.png")
plt.show()
