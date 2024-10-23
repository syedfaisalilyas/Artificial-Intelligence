import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Set a seed for reproducibility
np.random.seed(42)

# Generating synthetic data for customers
data = {
    "CustID": np.arange(1, 1001),
    "CustomerAge": np.random.randint(18, 71, size=1000),
    "IncomePerYear": np.random.randint(20000, 120001, size=1000),
    "Sex": np.random.choice(["M", "F"], size=1000),
    "Purchased": np.random.choice([0, 1], size=1000)
}

df = pd.DataFrame(data)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Fill missing values in 'IncomePerYear' with the median
df['IncomePerYear'].fillna(df['IncomePerYear'].median(), inplace=True)

# Confirm that missing values have been filled
print("Missing values in 'IncomePerYear' after filling:", df['IncomePerYear'].isnull().sum())

# Convert 'Sex' to numeric (1 for Males, 0 for Females)
df['Sex'] = df['Sex'].map({'M': 1, 'F': 0})

# Display the first few rows after encoding 'Sex'
print("\nDataset after gender encoding:")
print(df.head())

# Normalize 'CustomerAge' and 'IncomePerYear' using min-max scaling
df['CustomerAge'] = (df['CustomerAge'] - df['CustomerAge'].min()) / (df['CustomerAge'].max() - df['CustomerAge'].min())
df['IncomePerYear'] = (df['IncomePerYear'] - df['IncomePerYear'].min()) / (df['IncomePerYear'].max() - df['IncomePerYear'].min())

# Display the first few rows after normalization
print("\nDataset after normalization:")
print(df.head())

# Plot the age distribution
plt.figure(figsize=(10, 6))
plt.hist(df['CustomerAge'], bins=15, color='lightblue', edgecolor='black')
plt.title('Distribution of Customer Age')
plt.xlabel('Customer Age')
plt.ylabel('Count')
plt.show()

# Scatter plot to show relationship between Age and Income
plt.figure(figsize=(10, 6))
plt.scatter(df['CustomerAge'], df['IncomePerYear'], alpha=0.6, color='green')
plt.title('Age vs Annual Income')
plt.xlabel('Customer Age')
plt.ylabel('Annual Income')
plt.show()

# Calculate the correlation matrix to understand relationships between variables
correlation_matrix = df[['CustomerAge', 'IncomePerYear', 'Purchased']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Create a new feature: Income per unit of Age
df['IncomeToAgeRatio'] = df['IncomePerYear'] / df['CustomerAge']

# Display the first few rows with the new feature
print("\nDataset with 'IncomeToAgeRatio':")
print(df.head())

# Prepare data for modeling
X = df.drop(columns=['Purchased'])  # Features (without target)
y = df['Purchased']  # Target variable

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the training and testing datasets
print(f"\nTraining Data Shape: {X_train.shape}")
print(f"Testing Data Shape: {X_test.shape}")
print(f"Training Labels Shape: {y_train.shape}")
print(f"Testing Labels Shape: {y_test.shape}")
