import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

np.random.seed(42)

data = {
    "CustomerID": np.arange(1, 1001),
    "Age": np.random.randint(18, 71, size=1000),
    "AnnualIncome": np.random.randint(20000, 120001, size=1000),
    "Gender": np.random.choice(["Male", "Female"], size=1000),
    "HasPurchased": np.random.choice([0, 1], size=1000)
}

df = pd.DataFrame(data)

print(df.head())
print(df.head(10))

print("\nMissing values in each column:")
print(df.isnull().sum())

df['AnnualIncome'].fillna(df['AnnualIncome'].median(), inplace=True)

print("Missing values in 'AnnualIncome' after filling:", df['AnnualIncome'].isnull().sum())

df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

print(df.head())

df['Age'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
df['AnnualIncome'] = (df['AnnualIncome'] - df['AnnualIncome'].min()) / (df['AnnualIncome'].max() - df['AnnualIncome'].min())

print(df.head())

plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['AnnualIncome'], alpha=0.5, color='purple')
plt.title('Relationship Between Age and Annual Income')
plt.xlabel('Age')
plt.ylabel('Annual Income')
plt.show()

correlation_matrix = df[['Age', 'AnnualIncome', 'HasPurchased']].corr()
print(correlation_matrix)

df['IncomePerAge'] = df['AnnualIncome'] / df['Age']
print(df.head())

df['AnnualIncome'] = df['AnnualIncome'].fillna(df['AnnualIncome'].median())


X = df.drop(columns=['HasPurchased'])  
y = df['HasPurchased']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
