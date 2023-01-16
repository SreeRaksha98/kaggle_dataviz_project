import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import inline as inline

spotify_filepath = "spotify.csv"
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# print(spotify_data.head())

# Line chart showing daily streams of each song
sns.lineplot(data=spotify_data)

# graph size
plt.figure(figsize=(14, 6))

plt.title("Daily Global Streams of Popular Songs in 2017-2018")
print(sns.lineplot(data=spotify_data))

# plot subset of the data
print(list(spotify_data.columns))