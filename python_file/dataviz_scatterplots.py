import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import inline as inline

insurance_filepath = "insurance.csv"
insurance_data = pd.read_csv(insurance_filepath)
# print(insurance_data.head())

# scatter plots
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# To double-check the strength of this relationship, you might like to add a regression line, or the line that best
# fits the data. We do this by changing the command to sns.regplot.
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# Color - coded scatter plots
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
