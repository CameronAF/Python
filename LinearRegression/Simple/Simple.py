import numpy as np #Multidimensionals arrays
import pandas as pd #Organize data in a tabular form 
import matplotlib.pyplot as plt #Plotting library
import statsmodels.api as sm #Simplifies Machine Learning for user
import seaborn as sns #Upgrade for matplotlib
sns.set()

# Allways create meaningfull regressions (y = b0 + b1*x1)
# Is someone more likely to graduate from University with a higher GPA if they got a higher SAT score?
# Are Houses more likely to be more expensive the bigger they are?

# Load the data (GPA, SAT) or (Price, Size) by changing the if statment
if 1 == 1:
  data = pd.read_csv('Simple linear regression.csv')
  col1 = str(data.columns[1]) #GPA
  col2 = str(data.columns[0]) #SAT
else:
  data = pd.read_csv('Real estate price size.csv')
  col1 = str(data.columns[0]) #Price
  col2 = str(data.columns[1]) #Size
print(data)

# Usefull statastics from the data frame
print(data.describe())

# Regression 
# Define the dependent and independent variables
y = data[col1]
x1 = data[col2]
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
plt.ylabel(col1,fontsize='20')
plt.xlabel(col2,fontsize='20')
plt.show()