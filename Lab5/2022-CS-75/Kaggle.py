import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Path to your CSV file
file_path = r'D:\\Semester5\\AILab\\Lab5\\2022-CS-75\\Customer_support_data.csv'

# Load the data from the CSV file
df = pd.read_csv(file_path)

# Numpy Task
# Extract the 'CSAT Score' column
csat_scores = df['CSAT Score'].to_numpy()

# Calculate mean, median, and standard deviation
mean_csat = np.mean(csat_scores)
median_csat = np.median(csat_scores)
std_dev_csat = np.std(csat_scores)

# Display the results
print("Mean CSAT Score:", mean_csat)
print("Median CSAT Score:", median_csat)
print("Standard Deviation of CSAT Score:", std_dev_csat)

# Pandas Task
#1
filtered_df = df[df['CSAT Score'] > 4]
# Display the filtered data
print("filtered ",filtered_df)
#2
# Count the number of issues handled by each agent
agent_issue_count = df['Agent_name'].value_counts()
# Display the count of issues handled by each agent
print(agent_issue_count)
#3
# Group by 'category' and calculate the average CSAT Score
average_csat_by_category = df.groupby('category')['CSAT Score'].mean()
# Display the average CSAT Score for each category
print(average_csat_by_category)


# Matplot Task 1
# Plot a histogram for the 'CSAT Score'
plt.figure(figsize=(8, 6))
plt.hist(df['CSAT Score'], bins=5, edgecolor='black', color='skyblue')
plt.title('Distribution of CSAT Scores')
plt.xlabel('CSAT Score')
plt.ylabel('Frequency')
plt.grid(True)
# Display the histogram
plt.show()

# Matplot Task 2
# Group by 'category' and calculate the average CSAT Score
average_csat_by_category = df.groupby('category')['CSAT Score'].mean()
# Create a bar chart
plt.figure(figsize=(10, 6))
average_csat_by_category.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average CSAT Score by Category')
plt.xlabel('Category')
plt.ylabel('Average CSAT Score')
plt.xticks(rotation=45)
plt.grid(axis='y')
# Display the bar chart
plt.tight_layout()
plt.show()