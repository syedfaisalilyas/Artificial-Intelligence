import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

np.random.seed(42)

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U']
departments = ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
data = {
    'Employee ID': np.arange(1, 301),
    'Name': np.random.choice(names, 300),
    'Department': np.random.choice(departments, 300),
    'Salary': np.random.uniform(30000, 120000, 300),
    'Years of Experience': np.random.randint(1, 26, 300)
}
df = pd.DataFrame(data)
salary_array = df['Salary'].to_numpy()
average_salary = np.mean(salary_array)
max_salary = np.max(salary_array)
min_salary = np.min(salary_array)

filtered_df = df[(df['Years of Experience'] > 5) & (df['Salary'] > average_salary)]
mean_salary_by_dept = df.groupby('Department')['Salary'].mean()

plt.figure(figsize=(8, 5))
mean_salary_by_dept.plot(kind='bar', color='c', alpha=0.7)
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()
plt.figure(figsize=(8, 5))
plt.plot(df['Years of Experience'], df['Salary'], marker='o', linestyle='-', color='b', alpha=0.6)
plt.title('Salary Distribution by Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

print(f"Average Salary: ${average_salary:.2f}")
print(f"Maximum Salary: ${max_salary:.2f}")
print(f"Minimum Salary: ${min_salary:.2f}")
print("\nFiltered Data (Employees with >5 years experience and salary > average):")
print(filtered_df.head())
print("\nAverage Salary by Department:")
print(mean_salary_by_dept)
