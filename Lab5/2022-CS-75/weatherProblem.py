import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dates = pd.date_range(start='2024-01-01', periods=365)
temperature = np.random.randint(10, 40, size=365)
humidity = np.random.randint(30, 90, size=365)
wind_speed = np.random.randint(0, 20, size=365)
weather_conditions = np.random.choice(['Sunny', 'Rainy', 'Cloudy'], size=365)

weather_data = pd.DataFrame({
    'Date': dates,
    'Temperature': temperature,
    'Humidity': humidity,
    'Wind Speed': wind_speed,
    'Weather Condition': weather_conditions
})
print(weather_data)


temperature_array = weather_data['Temperature'].to_numpy()
mean_temp = np.mean(temperature_array)
median_temp = np.median(temperature_array)
std_temp = np.std(temperature_array)

print(f'Mean Temperature: {mean_temp:.2f}°C')
print(f'Median Temperature: {median_temp:.2f}°C')
print(f'Standard Deviation of Temperature: {std_temp:.2f}°C')



sunny_hot_days = weather_data[(weather_data['Temperature'] > 30) & (weather_data['Weather Condition'] == 'Sunny')]
num_sunny_hot_days = sunny_hot_days.shape[0]

print(sunny_hot_days)
print(f"Number of days with temperature above 30°C and Sunny: {num_sunny_hot_days}")

average_humidity = weather_data.groupby('Weather Condition')['Humidity'].mean().reset_index()
average_humidity.columns = ['Weather Condition', ' Average']

print(average_humidity)


plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date'], weather_data['Temperature'])
plt.title('Temperature Variation Over the Year')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.show()

weather_condition_counts = weather_data['Weather Condition'].value_counts()

plt.figure(figsize=(8, 5))
weather_condition_counts.plot(kind='bar')
plt.title('Number of Days for Each Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Days')
plt.show()
