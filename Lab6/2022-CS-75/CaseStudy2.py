import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Setting a random seed for consistent results
np.random.seed(42)

# Generating a sample dataset with employee data
data = {
    "EmployeeID": range(1, 1501),
    "EmployeeAge": np.random.randint(22, 61, 1500),
    "YearsOfExperience": np.random.randint(1, 41, 1500),
    "GenderCode": np.random.choice(['M', 'F'], 1500),
    "PerformanceScore": np.random.randint(1, 6, 1500)
}

df = pd.DataFrame(data)

# Display first few entries of the dataset
print("First 15 Records from Dataset:")
print(df.head(15))

# Checking for missing values
print("\nCount of Missing Values in Each Column:")
print(df.isnull().sum())

# Introducing some missing values in 'YearsOfExperience' column
rows_with_missing = np.random.choice(df.index, size=100, replace=False)
df.loc[rows_with_missing, 'YearsOfExperience'] = np.nan

# Imputing missing values with the mean
df['YearsOfExperience'].fillna(df['YearsOfExperience'].mean(), inplace=True)

# Confirming no missing values remain
print("\nMissing Values in 'YearsOfExperience' After Filling:")
print(df['YearsOfExperience'].isnull().sum())

# Encoding gender to numerical format (1 for Males, 0 for Females)
df['GenderCode'] = df['GenderCode'].map({'M': 1, 'F': 0})

# Display dataset after gender encoding
print("\nDataset After Gender Encoding:")
print(df.head())

# Identifying outliers based on 'YearsOfExperience'
experience_outliers = df['YearsOfExperience'] > 40
outliers = df[experience_outliers]

print("\nOutliers Detected in 'YearsOfExperience':")
print(outliers)

# Removing outliers from the dataset
df = df[~experience_outliers]

# Normalizing the 'EmployeeAge' and 'YearsOfExperience' columns
scaler = StandardScaler()
df[['EmployeeAge', 'YearsOfExperience']] = scaler.fit_transform(df[['EmployeeAge', 'YearsOfExperience']])

# Boxplot of performance ratings
plt.figure(figsize=(10, 6))
plt.boxplot(df['PerformanceScore'], vert=False)
plt.title('Boxplot: Employee Performance Ratings')
plt.xlabel('Performance Score')
plt.show()

# Scatter plot between experience and performance score
plt.figure(figsize=(10, 6))
plt.scatter(df['YearsOfExperience'], df['PerformanceScore'], alpha=0.5, color='green')
plt.title('Relationship Between Experience and Performance Score')
plt.xlabel('Years of Experience')
plt.ylabel('Performance Score')
plt.show()

# Calculating and printing the correlation matrix
correlation_matrix = df[['EmployeeAge', 'YearsOfExperience', 'PerformanceScore']].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Creating a new feature: Experience-to-Age ratio
df['ExperienceToAgeRatio'] = df['YearsOfExperience'] / df['EmployeeAge']

# Dropping the 'EmployeeID' column as it's not needed for analysis
df.drop(columns=['EmployeeID'], inplace=True)

# Preparing feature set (X) and target variable (y) for model training
X = df.drop(columns=['PerformanceScore'])
y = df['PerformanceScore']

# Splitting the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Displaying the shapes of the training and testing datasets
print("\nShapes of Training and Testing Sets:")
print(f"Training Data Shape: {X_train.shape}, Test Data Shape: {X_test.shape}")
print(f"Training Labels Shape: {y_train.shape}, Test Labels Shape: {y_test.shape}")
