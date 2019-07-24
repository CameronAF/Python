import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.cluster import KMeans
from sklearn import preprocessing

# Load the Data
data = pd.read_csv('Market Data.csv')
print('The Data:\n', data.head(21), '\n')
# Loyalty measured by num of purchases for 1y + other factors (-2.5 to 2.5)

# Plot the Data
plt.scatter(data['Satisfaction'], data['Loyalty'])
plt.title('Market Data')
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
plt.show()


# Select the features (Longitude & Latitude)
x = data.copy()

# k-Means Clustering with 2 clusters
kmeans = KMeans(2)
kmeans.fit(x)

# Clustering Results
clusters = x.copy()
clusters['cluster_pred'] = kmeans.fit_predict(x)
print('Clustering Results:\n', clusters.head(21))

plt.scatter(clusters['Satisfaction'], clusters['Loyalty'],c=clusters['cluster_pred'],cmap='rainbow')
plt.title('Unstandardized Clustered Data')
plt.xlabel('Satisfaction')
plt.ylabel('Loyalty')
plt.show()

# Standardizing the variables
x_scaled = preprocessing.scale(x)

# WCSS
wcss=[]

for i in range(1,10):
  kmeans = KMeans(i)
  kmeans.fit(x)
  wcss_iter = kmeans.inertia_
  wcss.append(wcss_iter)

# The Elbow Method
plt.plot(range(1,10),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# 2-Means Clustering using the Standardizing data
kmeans2 = KMeans(2)
kmeans2.fit(x_scaled)
#Solution is standardized, but the plotted data is not
clusters = x.copy()
clusters['cluster_pred'] = kmeans2.fit_predict(x_scaled)
plt.scatter(clusters['Satisfaction'], clusters['Loyalty'],c=clusters['cluster_pred'],cmap='rainbow')
plt.title('2 Clusters of standardized Market Data')
plt.show()

# 3-Means Clustering using the Standardizing data
kmeans2 = KMeans(3)
kmeans2.fit(x_scaled)
#Solution is standardized, but the plotted data is not
clusters = x.copy()
clusters['cluster_pred'] = kmeans2.fit_predict(x_scaled)
plt.scatter(clusters['Satisfaction'], clusters['Loyalty'],c=clusters['cluster_pred'],cmap='rainbow')
plt.title('3 Clusters of standardized Market Data')
plt.show()

# 4-Means Clustering using the Standardizing data
kmeans2 = KMeans(4)
kmeans2.fit(x_scaled)
#Solution is standardized, but the plotted data is not
clusters = x.copy()
clusters['cluster_pred'] = kmeans2.fit_predict(x_scaled)
plt.scatter(clusters['Satisfaction'], clusters['Loyalty'],c=clusters['cluster_pred'],cmap='rainbow')
plt.title('4 Clusters of standardized Market Data')
plt.show()

# 5-Means Clustering using the Standardizing data
kmeans2 = KMeans(5)
kmeans2.fit(x_scaled)
#Solution is standardized, but the plotted data is not
clusters = x.copy()
clusters['cluster_pred'] = kmeans2.fit_predict(x_scaled)
plt.scatter(clusters['Satisfaction'], clusters['Loyalty'],c=clusters['cluster_pred'],cmap='rainbow')
plt.title('5 Clusters of standardized Market Data')
plt.show()