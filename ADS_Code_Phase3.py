# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your preprocessed dataset
# Replace 'your_dataset.csv' with the actual dataset file path
data = pd.read_csv('country_vaccinations.csv')

# Statistical Analysis
# Example: Calculate vaccine efficacy
total_vaccinated = data['total_vaccinated']
total_infected = data['total_infected']

vaccine_efficacy = ((total_infected[0] - total_infected[-1]) / total_infected[0]) * 100

# Data Visualization
plt.figure(figsize=(10, 6))

# Example: Create a line chart to show vaccination progress over time
plt.plot(data['date'], data['total_vaccinated'], label='Total Vaccinated', marker='o')
plt.plot(data['date'], data['total_infected'], label='Total Infected', marker='x')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Covid-19 Vaccination Progress Over Time')
plt.legend()
plt.grid(True)

# Display vaccine efficacy
print(f'Vaccine Efficacy: {vaccine_efficacy:.2f}%')

# Show the line chart
plt.show()
