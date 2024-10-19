


import pandas as pd 
from sklearn.datasets import load_iris 
from sklearn.datasets import fetch_california_housing

# Iris
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data,columns=iris.feature_names)
iris_df['target']= iris.target

print('Iris Dataset:')
print(iris_df.head())

print('Missing Values:')
print(iris_df.isnull().sum())

iris_features = iris_df.columns[:-1]  
iris_target = 'target'

# California Dataset

california_housing = fetch_california_housing()
california_df = pd.DataFrame(data=california_housing.data, columns=california_housing.feature_names)
california_df['target'] = california_housing.target

print("\nCalifornia Housing Dataset:")
print(california_df.head())

print("Missing values in California Housing dataset:")
print(california_df.isnull().sum())

california_features = california_df.columns[:-1]  
california_target = 'target'