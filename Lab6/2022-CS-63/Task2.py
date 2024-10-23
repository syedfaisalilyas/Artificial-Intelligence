import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
np.random.seed(42)
data = {
    "EmpID": range(1, 1501),
    "Age": np.random.randint(22, 61, 1500),
    "Experience": np.random.randint(1, 41, 1500),
    "Gender": np.random.choice(['M', 'F'], 1500),
    "PerfRating": np.random.randint(1, 6, 1500)
}
df = pd.DataFrame(data)
print("Dataset Overview (First 15 Entries):")
print(df.head(15))
print("\nMissing Data in Columns:")
print(df.isnull().sum())
missing_rows = np.random.choice(df.index, size=100, replace=False)
df.loc[missing_rows, 'Experience'] = np.nan
df['Experience'].fillna(df['Experience'].mean(), inplace=True)
print("\nMissing Data in 'Experience' After Imputation:")
print(df['Experience'].isnull().sum())
df['Gender'] = df['Gender'].map({'M': 1, 'F': 0})
print("\nDataset Overview After Gender Encoding:")
print(df.head())
exp_outliers = df['Experience'] > 40
outliers = df[exp_outliers]
print("\nDetected Outliers in 'Experience':")
print(outliers)
df = df[~exp_outliers]
scaler = StandardScaler()
df[['Age', 'Experience']] = scaler.fit_transform(df[['Age', 'Experience']])
plt.figure(figsize=(10, 6))
plt.boxplot(df['PerfRating'], vert=True)
plt.title('Boxplot: Performance Rating')
plt.xlabel('Performance Rating')
plt.show()
plt.figure(figsize=(10, 6))
plt.scatter(df['Experience'], df['PerfRating'], alpha=0.5, color='red')
plt.title('Experience vs Performance Rating')
plt.xlabel('Experience')
plt.ylabel('Performance Rating')
plt.show()
correlation = df[['Age', 'Experience', 'PerfRating']].corr()
print("\nCorrelation Matrix:")
print(correlation)
df['ExpPerAge'] = df['Experience'] / df['Age']
df.drop(columns=['EmpID'], inplace=True)
X = df.drop(columns=['PerfRating'])
y = df['PerfRating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nData Splits (Shapes):")
print(f"Training Data: {X_train.shape}, Test Data: {X_test.shape}, Training Labels: {y_train.shape}, Test Labels: {y_test.shape}")