import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Generate dataset
num_rows = 1000
date_range = pd.date_range(end=pd.Timestamp.today(), periods=730)
dates = np.random.choice(date_range, size=num_rows)
companies = ['Tech Innovations Inc.', 'Green Earth Solutions', 'Future Enterprises', 'Skyline Technologies', 'Oceanic Holdings']
company_names = np.random.choice(companies, size=num_rows)
open_prices = np.random.uniform(50, 500, size=num_rows)
close_prices = np.random.uniform(50, 500, size=num_rows)
volume_traded = np.random.randint(1000, 1000000, size=num_rows)

# Create DataFrame
stock_data = pd.DataFrame({
    'Date': dates,
    'Company': company_names,
    'Open Price': open_prices,
    'Close Price': close_prices,
    'Volume Traded': volume_traded
})

# Calculate daily percentage change in stock prices
stock_data['Percentage Change'] = stock_data['Close Price'].pct_change() * 100

# Filter days when the stock price increased by more than 2%
increased_days = stock_data[stock_data['Percentage Change'] > 2]
print("Number of days when stock price increased by more than 2%:", len(increased_days))

# Group the data by Company and calculate the total Volume Traded
total_volume_by_company = stock_data.groupby('Company')['Volume Traded'].sum()
print("Total Volume Traded by Company:\n", total_volume_by_company)

# Plot Close Price trend for a particular company
company_to_plot = 'Tech Innovations Inc.'
company_data = stock_data[stock_data['Company'] == company_to_plot].sort_values(by='Date')

plt.figure(figsize=(10, 6))
plt.plot(company_data['Date'], company_data['Close Price'], marker='o', linestyle='-')
plt.title(f'Close Price Trend for {company_to_plot}')
plt.xlabel('Date')
plt.ylabel('Close Price ($)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

# Plot average percentage change in Close Price by company
average_percentage_change = stock_data.groupby('Company')['Percentage Change'].mean()

plt.figure(figsize=(10, 6))
average_percentage_change.plot(kind='bar', color='skyblue')
plt.title('Average Percentage Change in Close Price by Company')
plt.xlabel('Company')
plt.ylabel('Average Percentage Change (%)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
