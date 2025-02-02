import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Weather data (you can replace this with your actual data)
data = {
    'Temperature': [22, 25, 26, 18, 21, 19, 26, 27, 28],
    'Humidity': [60, 72, 78, 75, 80, 68, 69, 70, 71],
    'Wind Speed': [15, 10, 25, 12, 14, 18, 22, 11, 19],
    'Pressure': [1015, 1012, 1017, 1014, 1013, 1016, 1011, 1018, 1013]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Temperature'], df['Humidity'], color='blue')

# Adding labels and title
plt.title('Temperature vs Humidity', fontsize=14)
plt.xlabel('Temperature', fontsize=12)
plt.ylabel('Humidity', fontsize=12)

# Display the plot
plt.show()

#*******************************

plt.figure(figsize=(8, 6))

# Scatter plot
plt.scatter(df['Temperature'], df['Humidity'], color='blue', label='Stock A vs Stock B Returns')

# Adding labels and title
plt.title('Stock A vs Stock B Returns', fontsize=14)
plt.xlabel('Stock A Returns', fontsize=12)
plt.ylabel('Stock B Returns', fontsize=12)
plt.grid(True)
plt.legend()

# Show plot
plt.show()