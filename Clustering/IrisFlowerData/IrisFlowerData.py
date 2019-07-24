import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.cluster import KMeans
from sklearn import preprocessing

# Load the Data (sepal_length, sepal_width, petal_length, petal_width)
data = pd.read_csv('Iris Dataset.csv')
print('The Data:\n', data.head(21), '\n')

# Plot the Data
plt.figure(figsize = (12, 5))
plt.subplot(1,2,1)
plt.scatter(data['sepal_width'], data['sepal_length'])
plt.title('Flower Sepal Measurments')
plt.xlabel('Width')
plt.ylabel('Length')
plt.subplot(1,2,2)
plt.scatter(data['petal_width'], data['petal_length'])
plt.title('Flower Petal Measurments')
plt.xlabel('Width')
plt.ylabel('Length')
plt.show()

# Select the features (Longitude & Latitude)
x1 = data.iloc[:,0:2]
x2 = data.iloc[:,2:4]

# k-Means Clustering with 2 clusters
kmeans1 = KMeans(2)
kmeans2 = KMeans(2)
kmeans1.fit(x1)
kmeans2.fit(x2)

# Clustering Results
clusters1 = x1.copy()
clusters2 = x2.copy()
clusters1['cluster_pred'] = kmeans1.fit_predict(x1)
clusters2['cluster_pred'] = kmeans2.fit_predict(x2)

plt.figure(figsize = (12, 5))
plt.subplot(1,2,1)
plt.scatter(clusters1['sepal_width'], clusters1['sepal_length'],c=clusters1['cluster_pred'],cmap='rainbow')
plt.title('Unstandardized Flower Sepal Measurments')
plt.xlabel('Width')
plt.ylabel('Length')
plt.subplot(1,2,2)
plt.scatter(clusters2['petal_width'], clusters2['petal_length'],c=clusters2['cluster_pred'],cmap='rainbow')
plt.title('Unstandardized Flower Petal Measurments')
plt.xlabel('Width')
plt.ylabel('Length')
plt.show()

# Standardizing the variables
x1_scaled = preprocessing.scale(x1)
x2_scaled = preprocessing.scale(x2)

# WCSS
wcss1=[]
wcss2=[]

for i in range(1,12):
  kmeans = KMeans(i)
  kmeans.fit(x1)
  wcss_iter = kmeans.inertia_
  wcss1.append(wcss_iter)

for i in range(1,12):
  kmeans = KMeans(i)
  kmeans.fit(x2)
  wcss_iter = kmeans.inertia_
  wcss2.append(wcss_iter)

# The Elbow Method
plt.figure(figsize = (12, 5))
plt.subplot(1,2,1)
plt.plot(range(1,12),wcss1)
plt.title('Elbow Method for Flower Sepal Measurments')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.subplot(1,2,2)
plt.plot(range(1,12),wcss2)
plt.title('Elbow Method for Flower Petal Measurments')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Means Clustering using the Standardizing data
k=1
plt.figure(figsize = (12, 20))
for i in range(2,6):
  kmeans1 = KMeans(i)
  kmeans2 = KMeans(i)
  kmeans1.fit(x1_scaled)
  kmeans2.fit(x2_scaled)
  #Solution is standardized, but the plotted data is not
  clusters1 = x1.copy()
  clusters2 = x2.copy()
  clusters1['cluster_pred'] = kmeans1.fit_predict(x1_scaled)
  clusters2['cluster_pred'] = kmeans2.fit_predict(x2_scaled)

  plt.subplot(6,2,k)
  k += 1
  plt.scatter(clusters1['sepal_width'], clusters1['sepal_length'],c=clusters1['cluster_pred'],cmap='rainbow')
  if i == 2:
    plt.title('Standardized Sepal Measurments k=' + str(i))
  elif i == 5:
    plt.xlabel('Width')
  plt.ylabel('Length')
  plt.subplot(6,2,k)
  k += 1
  plt.scatter(clusters2['petal_width'], clusters2['petal_length'],c=clusters2['cluster_pred'],cmap='rainbow')
  if i == 2:
    plt.title('Standardized Petal Measurments k=' + str(i))
  elif i == 5:
    plt.xlabel('Width')

plt.subplots_adjust(bottom=0, top=0.97)
plt.show()

