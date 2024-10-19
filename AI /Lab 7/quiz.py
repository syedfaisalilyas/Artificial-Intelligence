import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating an array
array = np.arange(1, 10).reshape(3, 3)
print(array)

# Creating a DataFrame
data = {
    'Name': ['A', 'B', 'C'],
    'Age': [40, 20, 30],
    'City': ['N', np.nan, 'C']
}
df = pd.DataFrame(data)
print(df)

# Drop missing rows
df.dropna(inplace=True)
print(df)

# Add column
df['Salary'] = [2000, 3000]

# Adding a new row
df.loc[len(df)] = ['Faisal', 20, 'Lahore', 9000]
print(df)

# Filtering data
filtered_data = df[df['Age'] <= 20]
print(filtered_data)

# Grouping 
grouped_data = df.groupby('City').size()
print(grouped_data)

# Normalize Age
min_age = df['Age'].min()
max_age = df['Age'].max()
df['Normalized Age'] = (df['Age'] - min_age) / (max_age - min_age)

# Display normalized DataFrame
print('Normalized Age:')
print(df)

# Scatter plot
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
plt.scatter(x, y)  
plt.title('Scatter Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Histogram
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, color='blue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()
