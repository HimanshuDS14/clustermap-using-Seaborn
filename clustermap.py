import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("flights.csv")
print(data)

flights = data.pivot("month" , "year" , "passengers")
print(flights)
sns.heatmap(flights)
plt.xlabel("year")
plt.ylabel("Month")
plt.title("Heatmap")
plt.show()

sns.clustermap(flights)
plt.xlabel("year")
plt.ylabel("Month")
plt.title("Clustermap")
plt.show()