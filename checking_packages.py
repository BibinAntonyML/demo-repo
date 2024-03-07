import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dummy data
data = {
    'product': ['A', 'B', 'C', 'D', 'E'],
    'sales_A': [100, 200, 150, 300, 250],
    'sales_B': [150, 250, 200, 350, 300],
    'sales_C': [200, 300, 250, 400, 350]
}

# Convert the dictionary into a DataFrame
data = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(data.head())

# Basic statistics of the numerical columns
print("Basic statistics of the numerical columns:")
print(data.describe())

# Check for missing values
print("Missing values in the DataFrame:")
print(data.isnull().sum())

# Data manipulation
# Example: Creating a new column 'total_sales' by summing up 'sales_A', 'sales_B', and 'sales_C'
data['total_sales'] = data['sales_A'] + data['sales_B'] + data['sales_C']

# Example: Filtering the DataFrame to show only rows where 'total_sales' is greater than 1000
filtered_data = data[data['total_sales'] > 1000]

# Visualization using matplotlib
# Example: Plotting a bar chart of total sales for each product
plt.figure(figsize=(10, 6))
plt.bar(data['product'], data['total_sales'])
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Example: Scatter plot of 'sales_A' vs 'sales_B'
plt.figure(figsize=(8, 6))
plt.scatter(data['sales_A'], data['sales_B'])
plt.title('Scatter Plot of Sales A vs Sales B')
plt.xlabel('Sales A')
plt.ylabel('Sales B')
plt.show()

# Example: Histogram of 'total_sales'
plt.figure(figsize=(8, 6))
plt.hist(data['total_sales'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Total Sales')
plt.xlabel('Total Sales')
plt.ylabel('Frequency')
plt.show()


from scipy import stats

# Sample data
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Mean
mean = np.mean(data)
print("Mean:", mean)

# Median
median = np.median(data)
print("Median:", median)

# Mode
mode = stats.mode(data)
print("Mode:", mode.mode[0])

# Standard deviation
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

# Variance
variance = np.var(data)
print("Variance:", variance