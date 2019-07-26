import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load The Data
data = pd.read_csv('Country Clusters Standardized.csv', index_col='Country')
x_scaled = data.copy()
x_scaled = x_scaled.drop(['Language'], axis=1)
print(x_scaled.head())

# Plot the Data
sns.clustermap(x_scaled, cmap='mako')
plt.show()