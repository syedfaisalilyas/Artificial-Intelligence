import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Data Generation Task: Generate a dummy dataset with 365 rows
np.random.seed(42)  # For reproducibility
dates = pd.date_range(start="2023-01-01", periods=365)
temperature = np.random.uniform(10, 40, size=365)  # Temperature between 10°C and 40°C
humidity = np.random.uniform(30, 90, size=365)  # Humidity between 30% and 90%
wind_speed = np.random.uniform(0, 20, size=365)  # Wind Speed between 0 and 20 km/h
weather_condition = np.random.choice(['Sunny', 'Rainy', 'Cloudy'], size=365)

# Create a DataFrame
weather_data = pd.DataFrame({
    'Date': dates,
    'Temperature': temperature,
    'Humidity': humidity,
    'Wind Speed': wind_speed,
    'Weather Condition': weather_condition
})

# 2. NumPy Task: Convert the Temperature column to a NumPy array
temperature_array = weather_data['Temperature'].to_numpy()

# Calculate mean, median, and standard deviation
mean_temperature = np.mean(temperature_array)
median_temperature = np.median(temperature_array)
std_temperature = np.std(temperature_array)

print(f"Mean Temperature: {mean_temperature}")
print(f"Median Temperature: {median_temperature}")
print(f"Standard Deviation of Temperature: {std_temperature}")

# 3. Pandas Task: Filter the data for days when the temperature was above 30°C and it was Sunny
sunny_and_hot_days = weather_data[(weather_data['Temperature'] > 30) & (weather_data['Weather Condition'] == 'Sunny')]
sunny_and_hot_days_count = sunny_and_hot_days.shape[0]
print(f"Number of sunny and hot days (>30°C): {sunny_and_hot_days_count}")

# 4. Pandas Task: Group the dataset by Weather Condition and calculate the average Humidity
average_humidity_by_weather = weather_data.groupby('Weather Condition')['Humidity'].mean()
print(average_humidity_by_weather)

# 5. Matplotlib Task: Plot a line graph showing the temperature variation over the year
plt.figure(figsize=(10, 6))
plt.plot(weather_data['Date'], weather_data['Temperature'], label='Temperature')
plt.title('Temperature Variation Over the Year')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# 6. Matplotlib Task: Create a bar plot showing the number of days for each weather condition
weather_counts = weather_data['Weather Condition'].value_counts()
plt.figure(figsize=(8, 5))
weather_counts.plot(kind='bar', color=['orange', 'blue', 'gray'])
plt.title('Number of Days for Each Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Days')
plt.show()
