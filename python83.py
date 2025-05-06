# Task 3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset with dates
data = {
    "Order Date": pd.date_range(start="2024-01-01", periods=4, freq="M"),
    "Product": ["Laptop", "Tablet", "Monitor", "Mouse"],
    "Quantity": [1, 2, 1, 5],
    "Price": [1200.00, 300.00, 250.00, 25.00],
}

df = pd.DataFrame(data)
df["Total Sales"] = df["Quantity"] * df["Price"]

# Set visual style
sns.set(style="whitegrid")

# Line Chart: Total Sales Over Time
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Order Date", y="Total Sales", marker='o')
plt.title("Line Chart: Total Sales Over Time")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Bar Chart: Average Price per Product
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Product", y="Price")
plt.title("Bar Chart: Average Price per Product")
plt.xlabel("Product")
plt.ylabel("Price")
plt.tight_layout()
plt.show()

# Histogram: Distribution of Prices
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Price", bins=5, kde=True)
plt.title("Histogram: Distribution of Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter Plot: Quantity vs. Price
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Quantity", y="Price", hue="Product", s=100)
plt.title("Scatter Plot: Quantity vs. Price")
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.legend(title="Product")
plt.tight_layout()
plt.show()
