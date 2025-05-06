# Task 2
import pandas as pd

# Recreate the cleaned dataset
data = {
    "Order ID": [1001, 1002, 1003, 1004],
    "Product": ["Laptop", "Tablet", "Monitor", "Mouse"],
    "Quantity": [1, 2, 1, 5],
    "Price": [1200.00, 300.00, 250.00, 25.00],
    "Customer": ["Alice", "Bob", "Charlie", "David"]
}

df = pd.DataFrame(data)

# Step 1: Compute basic statistics of numerical columns
print("Basic Statistics:")
print(df.describe())

# Step 2: Perform grouping on the 'Product' column and compute mean of numerical columns
print("\nAverage Quantity and Price per Product:")
grouped = df.groupby("Product")[["Quantity", "Price"]].mean()
print(grouped)

# Step 3: Identify patterns or interesting findings
print("\nInteresting Findings:")
if grouped["Price"].max() > 1000:
    print("- Laptops are the most expensive product.")
if grouped["Quantity"].max() > 4:
    print("- Mice are often bought in bulk (average quantity > 4).")
