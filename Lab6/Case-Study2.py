import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler

np.random.seed(42)

data = {
    "EmployeeID": range(1, 1501),
    "Age": np.random.randint(22, 61, 1500),
    "Years of Experience": np.random.randint(1, 41, 1500),
    "Gender": np.random.choice(['Male', 'Female'], 1500),
    "Performance Rating": np.random.randint(1, 6, 1500)
}

df = pd.DataFrame(data)

print("First 15 rows of the dataset:")
print(df.head(15))

print("\nMissing values in each column:")
print(df.isnull().sum())

missing_indices = np.random.choice(df.index, size=100, replace=False)
df.loc[missing_indices, 'Years of Experience'] = np.nan

df['Years of Experience'].fillna(df['Years of Experience'].mean(), inplace=True)

print("\nMissing values in 'Years of Experience' after filling:")
print(df['Years of Experience'].isnull().sum())

df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

print("\nFirst few rows after encoding:")
print(df.head())

outlier_condition = df['Years of Experience'] > 40
outliers = df[outlier_condition]

print("\nOutliers in 'Years of Experience':")
print(outliers)

df = df[~outlier_condition]

scaler = StandardScaler()
df[['Age', 'Years of Experience']] = scaler.fit_transform(df[['Age', 'Years of Experience']])

plt.figure(figsize=(10, 6))
plt.boxplot(df['Performance Rating'], vert=False)
plt.title('Box Plot of Performance Rating')
plt.xlabel('Performance Rating')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Years of Experience'], df['Performance Rating'], alpha=0.5, color='purple')
plt.title('Scatter Plot of Years of Experience vs Performance Rating')
plt.xlabel('Years of Experience')
plt.ylabel('Performance Rating')
plt.show()

correlation_matrix = df[['Age', 'Years of Experience', 'Performance Rating']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

df['Experience per Age'] = df['Years of Experience'] / df['Age']

df.drop(columns=['EmployeeID'], inplace=True)

X = df.drop(columns=['Performance Rating'])
y = df['Performance Rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nShapes of the resulting datasets:")
print(f"X_train: {X_train.shape}, X_test: {X_test.shape}, y_train: {y_train.shape}, y_test: {y_test.shape}")
