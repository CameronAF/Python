import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.cluster import KMeans

# Load the Data
x = 0
if x == 1:
  data = pd.read_csv('Country Clusters 1.csv')
  col3 = str(data.columns[3]) # Language 
  k = 3
else:
  data = pd.read_csv('Country Clusters 2.csv')
  col3 = str(data.columns[3]) # continent
  k = 8
print('The Data:\n', data.head(21), '\n')

# Plot the Data
plt.scatter(data['Longitude'], data['Latitude'])
plt.title('Data colored by ' + col3)
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show()

# Map the Data
data_mapped = data.copy()
if x == 1:
  data_mapped[col3] = data_mapped[col3].map({'English':0, 'French':1, 'German':2})
else:
  data_mapped[col3] = data_mapped[col3].map({'North America':0,'Europe':1,'Asia':2,'Africa':3,'South America':4, 'Oceania':5,'Seven seas (open ocean)':6, 'Antarctica':7})


# Select the features (Longitude & Latitude)
x = data_mapped.iloc[:,1:4] #[rows to keep, cols to keep]

# k-Means Clustering with k clusters
kmeans = KMeans(k)
kmeans.fit(x)

# Clustering Results
identified_clusters = kmeans.fit_predict(x)
data_with_clusters = data_mapped.copy()
data_with_clusters['Cluster'] = identified_clusters
print('Clustering Results:\n', data_with_clusters.head(21))

plt.scatter(data_with_clusters['Longitude'], data_with_clusters['Latitude'],c=data_with_clusters['Cluster'],cmap='rainbow')
plt.title('Clustered Data')
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.show()

# Selecting the Number of CLusters
# WCSS
kmeans.inertia_
wcss=[]

max = data.count(axis = 0)[0]
if max > 50:
  max = 50
for i in range(1,max):
  kmeans = KMeans(i)
  kmeans.fit(x)
  wcss_iter = kmeans.inertia_
  wcss.append(wcss_iter)

# The Elbow Method
number_clusters = range(1,max)
plt.plot(number_clusters,wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Within-Cluster Sum of Squares')
plt.show()