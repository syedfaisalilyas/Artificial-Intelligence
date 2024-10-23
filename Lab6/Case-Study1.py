import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split

np.random.seed(42)

data = {
    "CustomerID": range(1, 1001),
    "Age": np.random.randint(18, 71, 1000),
    "Annual Income": np.random.randint(20000, 120001, 1000),
    "Gender": np.random.choice(["Male", "Female"], 1000),
    "Purchased": np.random.choice([0, 1], 1000)
}

df = pd.DataFrame(data)

print(df.head())
print(df.head(10))

print("\nMissing values in each column:")
print(df.isnull().sum())
df['Annual Income'].fillna(df['Annual Income'].median(), inplace=True)

print("Missing values in 'Annual Income' after filling:", df['Annual Income'].isnull().sum())
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

print(df.head())
df['Age'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
df['Annual Income'] = (df['Annual Income'] - df['Annual Income'].min()) / (df['Annual Income'].max() - df['Annual Income'].min())

print(df.head())

plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Annual Income'], alpha=0.5, color='purple')
plt.title('Relationship Between Age and Annual Income')
plt.xlabel('Age')
plt.ylabel('Annual Income')
plt.show()

correlation_matrix = df[['Age', 'Annual Income', 'Purchased']].corr()
print(correlation_matrix)
df['Income per Age'] = df['Annual Income'] / df['Age']
print(df.head())

df['Annual Income'] = df['Annual Income'].fillna(df['Annual Income'].median())

# # Split the data into features (X) and target (y)
# X = df.drop(columns=['Purchased'])  # Features
# y = df['Purchased']  # Target variable

# # Split the data into training and testing sets (80% train, 20% test)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Display the shapes of the resulting datasets
# print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)