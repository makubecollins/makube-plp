import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("your_data.csv")

# Clean data (remove rows with missing values)
df = df.dropna()

# Analyze data (group by category and calculate mean)
grouped_data = df.groupby("category")["value"].mean()

# Visualize data (create a bar chart)
plt.bar(grouped_data.index, grouped_data.values)
plt.xlabel("Category")
plt.ylabel("Mean Value")
plt.title("Mean Value by Category")
plt.show()