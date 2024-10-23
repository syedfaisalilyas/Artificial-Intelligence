# Import necessary libraries
import pandas as pd
from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

# Task 1: Data Preparation and Exploration

# Load the Iris dataset (classification task)
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['Species'] = iris.target

# Load the California Housing dataset (regression task)
california = fetch_california_housing()
california_df = pd.DataFrame(data=california.data, columns=california.feature_names)
california_df['MedianHouseValue'] = california.target

# Explore the Iris dataset
print("Iris Dataset Overview:")
print(iris_df.head())
print("\nMissing values in Iris dataset:")
print(iris_df.isnull().sum())

# Explore the California Housing dataset
print("\nCalifornia Housing Dataset Overview:")
print(california_df.head())
print("\nMissing values in California Housing dataset:")
print(california_df.isnull().sum())

# Task 2: Feature Scaling and Data Splitting

# Scale features for both datasets
scaler_iris = StandardScaler()
iris_scaled = scaler_iris.fit_transform(iris_df.drop(columns=['Species']))

scaler_california = StandardScaler()
california_scaled = scaler_california.fit_transform(california_df.drop(columns=['MedianHouseValue']))

# Split datasets into training and testing sets
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(
    iris_scaled, iris_df['Species'], test_size=0.2, random_state=42
)

X_train_california, X_test_california, y_train_california, y_test_california = train_test_split(
    california_scaled, california_df['MedianHouseValue'], test_size=0.2, random_state=42
)

# Task 3: Classification Models

# k-NN Classifier for Iris dataset (try different values of k)
print("\nk-NN Classifier Results:")
for k in range(1, 4):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_iris, y_train_iris)
    y_pred_iris = knn.predict(X_test_iris)
    print(f'k = {k}, Accuracy = {accuracy_score(y_test_iris, y_pred_iris)}')

# Support Vector Machine (SVM) for Iris dataset (with different kernels)
print("\nSVM Classifier Results:")
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
for kernel in kernels:
    svm = SVC(kernel=kernel)
    svm.fit(X_train_iris, y_train_iris)
    y_pred_iris = svm.predict(X_test_iris)
    print(f'SVM (kernel={kernel}), Accuracy = {accuracy_score(y_test_iris, y_pred_iris)}')

# Random Forest Classifier for Iris dataset
print("\nRandom Forest Classifier Results:")
rf = RandomForestClassifier(n_estimators=10)
rf.fit(X_train_iris, y_train_iris)
y_pred_iris = rf.predict(X_test_iris)
print(f'Random Forest Accuracy = {accuracy_score(y_test_iris, y_pred_iris)}')

# Task 4: Regression Models

# Linear Regression for California Housing dataset
print("\nLinear Regression Results:")
lr = LinearRegression()
lr.fit(X_train_california, y_train_california)
y_pred_california = lr.predict(X_test_california)
print(f'MSE = {mean_squared_error(y_test_california, y_pred_california)}, R² = {r2_score(y_test_california, y_pred_california)}')

# Decision Tree Regressor for California Housing dataset
print("\nDecision Tree Regression Results:")
dt = DecisionTreeRegressor()
dt.fit(X_train_california, y_train_california)
y_pred_california = dt.predict(X_test_california)
print(f'MSE = {mean_squared_error(y_test_california, y_pred_california)}, R² = {r2_score(y_test_california, y_pred_california)}')

# Task 5: Evaluation and Summary

# Final evaluation for classification models
print("\nClassification Model Comparison:")
print(f'Final k-NN Accuracy = {accuracy_score(y_test_iris, knn.predict(X_test_iris))}')
print(f'Final SVM Accuracy = {accuracy_score(y_test_iris, svm.predict(X_test_iris))}')
print(f'Final Random Forest Accuracy = {accuracy_score(y_test_iris, rf.predict(X_test_iris))}')

# Final evaluation for regression models
print("\nRegression Model Comparison:")
print(f'Final Linear Regression MSE = {mean_squared_error(y_test_california, lr.predict(X_test_california))}, R² = {r2_score(y_test_california, lr.predict(X_test_california))}')
print(f'Final Decision Tree MSE = {mean_squared_error(y_test_california, dt.predict(X_test_california))}, R² = {r2_score(y_test_california, dt.predict(X_test_california))}')
