import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data Generation Task
np.random.seed(42)
num_rows = 200
student_ids = np.arange(1 , num_rows+1)
names = ['Student' + str(i) for i in range(1 , num_rows+1)]
subjects = ['Maths', 'Science', 'History', 'Geography', 'English'] 
subject_choices = np.random.choice(subjects , size = num_rows)
scores = np.random.randint(0, 100, size=num_rows)

student_data = pd.DataFrame({
    'Student ID': student_ids,
    'Name': names,
    'Subject': subject_choices,
    'Score': scores,
    'Total Marks': 100
})


mean_of_score = np.mean(student_data['Score'])
meadian_of_score= np.median(student_data['Score'])
standard_dev_score = np.std(student_data['Score'])

print("Mean of Score: ", mean_of_score)
print("Median of Score: ", meadian_of_score)
print("Standard Deviation of Score: ", standard_dev_score)

highest_score = student_data[student_data['Score']>80]
count_of_student= highest_score.shape[0]
print("Number of students who scored above 80%: ", count_of_student)


subject_group = student_data.groupby('Subject')
average_score = subject_group['Score'].mean()

print("Average Score by Subject: ", average_score)


## Histogram of scores distribution across all students

plt.figure(figsize=(8,6))
plt.hist(student_data['Score'], bins = 15 , color = 'pink' , edgecolor = 'black')
plt.title('Distribution of Scores Across All Students')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()


## Bar chart to compare average scores across different subjects

plt.figure(figsize=(8,6))
plt.bar(average_score.index , average_score.values , color = 'blue')
plt.title('Average Scores by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Score')
plt.grid(True)
plt.show()




