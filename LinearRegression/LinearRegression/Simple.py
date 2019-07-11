import numpy as np #Multidimensionals arrays
import pandas as pd #Organize data in a tabular form 
import matplotlib.pyplot as plt #Plotting library
import statsmodels.api as sm #Simplifies Machine Learning for user
import seaborn as sns #Upgrade for matplotlib
#import scipy #Python ecosystem w/ tools for scientific calculations
#import sklearn #Machine learning
sns.set()

# Allways create meaningfull regressions (y = b0 + b1*x1)
# Is someone more likely to graduate from University with a higher GPA if they got a higher SAT score?

# Load the data (SAT, GPA) or (Price, Size) by changing the if statment
if 1 == 0:
  data = pd.read_csv('Simple linear regression.csv')
else:
  data = pd.read_csv('Real estate price size.csv')
print(data)
col1 = str(data.columns[0]) #SAT
col2 = str(data.columns[1]) #GPA
# Usefull statastics from the data frame
print(data.describe())

# Regression 
# Define the dependent and independent variables
y = data[col2]
x1 = data[col1]
# Add a constent of 1 to find b0
x = sm.add_constant(x1)
# Fit the model using Ordinary Least Squares Regression
results = sm.OLS(y,x).fit()
print(results.summary())
# regression line: y = b0 + b1*x1
b0 = round(results.params[0],4)
b1 = round(results.params[1],4)
yhat = b0 + (b1 * x1)
# plot the data and regression line
plt.scatter(x1,y)
fig = plt.plot(x1, yhat, lw=4, c='orange', label='regression line')
plt.xlabel(col1,fontsize='20')
plt.ylabel(col2,fontsize='20')
plt.show()