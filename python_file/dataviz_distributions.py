import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import inline as inline

iris_filepath = "iris.csv"
iris_data = pd.read_csv(iris_filepath, index_col="Id")

# histogram
sns.histplot(iris_data['Petal Length (cm)'])

# KDE plot
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)


