# Task 1
import pandas as pd

# Step 1: Load the dataset (here we create a sample dataset)
data = {
    "Order ID": [1001, 1002, 1003, 1004, 1005],
    "Product": ["Laptop", "Tablet", "Monitor", "Mouse", "Keyboard"],
    "Quantity": [1, 2, 1, 5, None],
    "Price": [1200.00, 300.00, 250.00, 25.00, 45.00],
    "Customer": ["Alice", "Bob", "Charlie", "David", None]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Step 2: Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Explore the structure of the dataset
print("\nDataset Information:")
print(df.info())

# Step 4: Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 5: Clean the dataset by dropping rows with missing values
df_cleaned = df.dropna()

print("\nDataset after cleaning (dropped rows with missing values):")
print(df_cleaned)
