import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/cleaned_credit_data.csv")

# Class distribution plot
plt.figure(figsize=(6,4))
sns.countplot(x="default", data=df)
plt.title("Defaulted vs. Non-Defaulted Customers")
plt.savefig("reports/class_distribution.png")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.savefig("reports/correlation_heatmap.png")
plt.show()

print("Visualization completed and saved.")
