import numpy as np #Multidimensionals arrays
import pandas as pd #Organize data in a tabular form 
import matplotlib.pyplot as plt #Plotting library
import statsmodels.api as sm #Simplifies Machine Learning for user
import seaborn as sns #Upgrade for matplotlib
sns.set()

# Allways create meaningfull regressions (y = b0 + b1*x1)
# Is someone more likely to graduate from University with a higher GPA if they got a higher SAT score?
# Are Houses more likely to be more expensive the bigger they are and the year the house was built?

# Load the data (GPA, SAT, Ran 1 2 3) or (Price, Size, Year) by changing the if statment
if 1 == 1:
  data = pd.read_csv('Multiple_Linear_Regression.csv')
  col1 = str(data.columns[1]) #GPA
  col2 = str(data.columns[0]) #SAT
  col3 = str(data.columns[2]) #Ran 1, 2, 3
else:
  data = pd.read_csv('Real_Estate_Price_Size_Year.csv')
  col1 = str(data.columns[0]) #price
  col2 = str(data.columns[1]) #size
  col3 = str(data.columns[2]) #year
print(data)

# Usefull statastics from the data frame
print(data.describe())

# Regression 
# Define the dependent and independent variables
y = data[col1]
x1 = data[[col2, col3]]
# Add a constent of 1 to find b0
x = sm.add_constant(x1)
# Fit the model using Ordinary Least Squares Regression
results = sm.OLS(y,x).fit()
print(results.summary())
