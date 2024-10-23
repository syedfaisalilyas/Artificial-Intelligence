import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U']
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
data = {
    'Student ID': np.random.randint(1000, 2000, 200),
    'Name': np.random.choice(names, 200),
    'Subject': np.random.choice(subjects, 200),
    'Score': np.random.randint(0, 101, 200),
    'Total Marks': [100] * 200  
}
df = pd.DataFrame(data)
scores_array = df['Score'].to_numpy()
mean_score = np.mean(scores_array)
median_score = np.median(scores_array)
std_deviation = np.std(scores_array)
high_scorers = df[df['Score'] > 80]
num_high_scorers = high_scorers.shape[0]
avg_score_by_subject = df.groupby('Subject')['Score'].mean()
plt.figure(figsize=(8, 5))
plt.hist(df['Score'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Score Distribution Across All Students')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(8, 5))
avg_score_by_subject.plot(kind='bar', color='lightgreen', alpha=0.8)
plt.title('Average Scores by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Score')
plt.show()
print(f"Mean Score: {mean_score:.2f}")
print(f"Median Score: {median_score:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")
print(f"Number of students scoring above 80%: {num_high_scorers}")
print("\nAverage score by subject:")
print(avg_score_by_subject)
