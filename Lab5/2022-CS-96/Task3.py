import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(42)

num_rows = 300 

employees_id =np.arange (1 , num_rows+1)
employees_name =['John' , 'Doe' , 'Jane' , 'Smith' , 'Alex' , 'Kate' , 'Mike' , 'Emily' , 'Chris' , 'Lily' , 'David' , 'Sarah' , 'Tom' , 'Olivia' , 'James' , 'Sophia' , 'Daniel' , 'Ella' , 'William' , 'Grace'] 
employees_name = np.random.choice(employees_name , size = num_rows)

department_names  = ['HR' , 'IT' , 'Finance' , 'Marketing' , 'Operations']
department_names = np.random.choice(department_names , size = num_rows)

salary = np.random.randint(30000 , 120000 , size = num_rows)
experience = np.random.randint(1, 25 , size = num_rows)


employes_data =pd.DataFrame({
    'Employee ID': employees_id,
    'Employee Name': employees_name,
    'Department': department_names,
    'Salary': salary,
    'Experience': experience
})

print(employes_data.head())


salary_array = employes_data['Salary'].to_numpy()

# Calculate average, maximum, and minimum salary
average_salary = np.mean(salary_array)
maximum_salary = np.max(salary_array)
minimum_salary = np.min(salary_array)

print("Average Salary: ", average_salary)
print("Maximum Salary: ", maximum_salary)
print("Minimum Salary: ", minimum_salary)


## Filter employees with more than 5 years of experience and salary greater than the average
experience_salary = employes_data[(employes_data['Experience'] > 5) & (employes_data['Salary'] > average_salary)]


##Group by Department and calculate the average salary

average_sal_by_dept = employes_data.groupby('Department')['Salary'].mean()
print("average_sal_by_dept" , average_sal_by_dept)


## bar plot of average salary by department

plt.figure(figsize = (8, 6))
plt.bar(average_sal_by_dept.index , average_sal_by_dept.values , color = 'green')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')



##line plot of salary varition with the experience 

mean_salary_by_experience = employes_data.groupby('Experience')['Salary'].mean()

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(mean_salary_by_experience.index, mean_salary_by_experience.values, marker='o', linestyle='-')

# Add titles and labels
plt.title('Salary Distribution with Increasing Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Average Salary ($)')
plt.grid(True)
plt.xticks(mean_salary_by_experience.index)  # Show all experience levels on the x-axis





plt.grid(True)
plt.show()

 