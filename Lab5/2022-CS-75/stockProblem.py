import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

np.random.seed(42)
start_date = datetime.now() - timedelta(days=730)
date_list = [start_date + timedelta(days=random.randint(0, 730)) for _ in range(1000)]
companies = ['CompanyA', 'CompanyB', 'CompanyC', 'CompanyD', 'CompanyE']
data = {
    'Date': date_list,
    'Company': np.random.choice(companies, 1000),
    'Open Price': np.random.uniform(50, 500, 1000),
    'Close Price': np.random.uniform(50, 500, 1000),
    'Volume Traded': np.random.randint(1000, 1000000, 1000)
}
df = pd.DataFrame(data)
close_price_array = df['Close Price'].to_numpy()
daily_percentage_change = np.diff(close_price_array) / close_price_array[:-1] * 100
df['Daily Percentage Change'] = np.insert(daily_percentage_change, 0, 0)
price_increase_df = df[df['Daily Percentage Change'] > 2]
total_volume_by_company = df.groupby('Company')['Volume Traded'].sum()
company = 'CompanyA'
company_data = df[df['Company'] == company].sort_values('Date')
plt.figure(figsize=(10, 6))
plt.plot(company_data['Date'], company_data['Close Price'], marker='o', color='b', alpha=0.6)
plt.title(f'Trend of Close Price over Time for {company}')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.show()
avg_percentage_change_by_company = df.groupby('Company')['Daily Percentage Change'].mean()

plt.figure(figsize=(8, 5))
avg_percentage_change_by_company.plot(kind='bar', color='orange', alpha=0.8)
plt.title('Average Daily Percentage Change in Close Price by Company')
plt.xlabel('Company')
plt.ylabel('Average Percentage Change')
plt.show()
print("\nDays when stock price increased by more than 2%:")
print(price_increase_df.head())
print("\nTotal Volume Traded by Company:")
print(total_volume_by_company)
