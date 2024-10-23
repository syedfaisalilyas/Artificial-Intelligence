import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(42)
dates = pd.date_range(end=pd.Timestamp.today(), periods=365).to_pydatetime()
num_rows = 500
products = ['laptop' , 'Mouse' , 'Keyboard' , 'Monitor' , 'Printer','Scanner','Speaker','Headphone','Webcam','Microphone']
products = np.random.choice(products , size = num_rows)
purchase_dates = np.random.choice (dates , size = num_rows)
price = np.random.uniform(10 , 1000 , size = num_rows)
Quantity = np.random.randint(1 ,20, size = num_rows)




dummy_data = pd.DataFrame({
    'Date': purchase_dates,
    'Product': products,
    'Price': price,
    'Quantity': Quantity
})

print(dummy_data.head())

# Convert the Price and Quantity columns to NumPy arrays
price_array = dummy_data['Price'].to_numpy()
Quantity_array = dummy_data['Quantity'].to_numpy()
total_sales = price_array * Quantity_array

# Add the total_sales column to the DataFrame
# Add the total_sales column to the DataFrame
dummy_data['total_sales'] = total_sales

high_value_sales = dummy_data[dummy_data['total_sales'] > 100]
print("high_value_sales", high_value_sales)


## Group by Product and calculate the total quantity sold
total_quantity_sold = dummy_data.groupby('Product')['Quantity'].sum()
print("total_quantity_sold" , total_quantity_sold)

## Scatter plot of Price vs Quantity
plt.figure(figsize=(8, 6))
plt.scatter(dummy_data['Price'], dummy_data['Quantity'], alpha=0.6, edgecolor='k')

plt.title('Scatter Plot of Price vs Quantity of Products Sold')
plt.xlabel('Price ($)')
plt.ylabel('Quantity Sold')


## Histogram of Total Sales
plt.figure(figsize=(8, 6))
plt.hist(dummy_data['total_sales'], bins=20, color='purple', edgecolor='black')

# Add titles and labels
plt.title('Distribution of Total Sales Values')
plt.xlabel('Total Sales ($)')
plt.ylabel('Frequency')


plt.grid(True)
plt.show()

