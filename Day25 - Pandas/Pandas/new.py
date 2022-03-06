import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('Pandas/new_data.csv')
data["names"].value_counts().plot(kind='bar')