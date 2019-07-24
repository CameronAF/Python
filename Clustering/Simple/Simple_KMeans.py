import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.cluster import KMeans

# Load the Data
if 1 == 0:
  data = pd.read_csv('Country Clusters 1.csv')
else:
  data = pd.read_csv('Country Clusters 2.csv')
print('The Data:\n', data, '\n')

# Plot the Data
plt.scatter(data['Longitude'], data['Latitude'])
plt.title('Data')
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show()

# Select the features (Longitude & Latitude)
x = data.iloc[:,1:3] #[rows to keep, cols to keep]
x = x[['Latitude','Longitude']]

# k-Means Clustering with 3 clusters
kmeans = KMeans(7)
kmeans.fit(x)

# Clustering Results
identified_clusters = kmeans.fit_predict(x)
data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
print('Clustering Results:\n', data_with_clusters)

plt.scatter(data_with_clusters['Longitude'], data_with_clusters['Latitude'],c=data_with_clusters['Cluster'],cmap='rainbow')
plt.title('Clustered Data')
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show()