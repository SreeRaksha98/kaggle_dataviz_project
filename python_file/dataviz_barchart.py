import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import inline as inline

flight_filepath = "flight_delays.csv"
flight_data = pd.read_csv(flight_filepath, index_col="Month")

# Bar chart
plt.figure(figsize=(10, 6))
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")
sns.barplot(x=flight_data.index, y=flight_data['NK'])
plt.ylabel("Arrival delay in minutes")
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# Heatmaps
plt.figure(figsize=(14, 7))
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")
sns.heatmap(data=flight_data, annot=True)
plt.xlabel("Airline")
sns.heatmap(data=flight_data, annot=True)
