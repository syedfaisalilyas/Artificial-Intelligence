import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
order_ids = np.arange(1, 501)
products = np.random.choice(['Laptop', 'Headphones', 'Mouse', 'Keyboard', 'Monitor', 'Smartphone', 
                             'Tablet', 'Camera', 'Smartwatch', 'Charger'], size=500)
prices = np.random.randint(10, 1001, size=500)
quantities = np.random.randint(1, 21, size=500)
purchase_dates = pd.date_range(end=pd.Timestamp.today(), periods=500).to_numpy()
sales_data = pd.DataFrame({
    'Order ID': order_ids,
    'Product': products,
    'Price': prices,
    'Quantity': quantities,
    'Date of Purchase': purchase_dates
})
print(sales_data.head())
price_array = sales_data['Price'].to_numpy()
quantity_array = sales_data['Quantity'].to_numpy()
total_sales = price_array * quantity_array
sales_data['Total Sales'] = total_sales
print(sales_data.head())
high_value_sales = sales_data[sales_data['Total Sales'] > 100]
print(f"\nOrders with Total Sales > $100:\n{high_value_sales}")
total_quantity_by_product = sales_data.groupby('Product')['Quantity'].sum().reset_index()
print(f"\nTotal Quantity Sold by Product:\n{total_quantity_by_product}")

plt.figure(figsize=(10, 6))
plt.scatter(sales_data['Price'], sales_data['Quantity'], alpha=0.7, color='b')
plt.title('Price vs Quantity of Products Sold')
plt.xlabel('Price ($)')
plt.ylabel('Quantity Sold')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(sales_data['Total Sales'], bins=20, color='g', alpha=0.7)
plt.title('Distribution of Total Sales Values')
plt.xlabel('Total Sales ($)')
plt.ylabel('Number of Orders')
plt.grid(True)
plt.tight_layout()
plt.show()
