import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset from the specified CSV file
file_path = r'D:\5thSemester\ArtificialLAB\Lab_5\2022-CS-96\SuperMarket.csv'

def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path, parse_dates=['Date']).fillna(0)
    else:
        print(f"Error: The file '{file_path}' does not exist.")
        return None

def display_basic_info(data):
    print("First 5 rows of the dataset:")
    print(data.head())
    print("\nBasic Information:")
    print(data.info())
    print("\nSummary Statistics:")
    print(data.describe())

def analyze_data(data):
    print("\nCustomer Type Count:")
    print(data['Customer type'].value_counts())
    print("\nTotal Sales by Branch:")
    print(data.groupby('Branch')['Sales'].sum())
    print("\nAverage Rating by Product Line:")
    print(data.groupby('Product line')['Rating'].mean())
    high_sales_days = data[data['Sales'] > 500]
    print("\nDays with Sales greater than $500:")
    print(high_sales_days[['Date', 'Sales']])
    high_sales_days.to_csv(r'D:\5thSemester\ArtificialLAB\Lab_5\2022-CS-96\High_Sales_Days.csv', index=False)
    print(f"\nTotal Sales: ${np.sum(data['Sales']):.2f}")
    print(f"Mean Sales: ${np.mean(data['Sales']):.2f}")

def plot_data(data):
    plt.figure(figsize=(10, 6))
    data.groupby('Branch')['Sales'].sum().plot(kind='bar', color='grey')
    plt.title('Total Sales by Branch')
    plt.xlabel('Branch')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    plt.figure(figsize=(10, 6))
    data.groupby('Product line')['Rating'].mean().plot(kind='bar', color='purple')
    plt.title('Average Rating by Product Line')
    plt.xlabel('Product Line')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    data = load_data(file_path)
    if data is not None:
        display_basic_info(data)
        analyze_data(data)
        plot_data(data)

if __name__ == "__main__":
    main()
