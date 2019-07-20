import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def adj_r2(x,y):
  r2 = reg.score(x,y)
  n = x.shape[0]
  p = x.shape[1]
  adjusted_r2 = 1-(1-r2)*(n-1)/(n-p-1)
  return adjusted_r2

predict = False
# Allways create meaningfull regressions (y = b0 + b1*x1)
# Is someone more likely to graduate from University with a higher GPA if they got a higher SAT score?
# Are Houses more likely to be more expensive the bigger they are and the year the house was built?

# Load the data (GPA, SAT, Ran 1 2 3) or (Price, Size, Year) by changing the if statment
if 1 == 1:
  data = pd.read_csv('Multiple Linear Regression.csv')
  col1 = str(data.columns[2]) #GPA
  col2 = str(data.columns[0]) #SAT
  col3 = str(data.columns[1]) #Ran 1, 2, 3
  predict = True
else:
  data = pd.read_csv('Real Estate Price Size Year.csv')
  col1 = str(data.columns[0]) #price
  col2 = str(data.columns[1]) #size
  col3 = str(data.columns[2]) #year
print('The Data:\n', data.head(), '\n')

# Usefull statastics from the data frame
print('The Data Described:\n', data.describe(), '\n')

# Define the dependent and independent variables
y = data[col1]
x = data[[col2, col3]]

# Standardizing 
# subtract the mean and divide by the standard deviation
scaler = StandardScaler()
# calculate and store the mean and sd of each feature
scaler.fit(x)
x_scales = scaler.transform(x)

# create the regression with scaled features
reg = LinearRegression()
reg.fit(x_scales,y)

# Coefficients
reg.coef_ # array [col2,col3]

# Intercept
reg.intercept_

# R-Squared (goodness of fit)
reg.score(x,y)

# adjusted R-Squared
adjusted_r2 = adj_r2(x,y)

# Feature Selection
f_regression(x,y)
p_vals = f_regression(x,y)[1]

# Creating a summery
# Weight closer to 0 means its not a usefull feature
reg_summery = pd.DataFrame([['Bias'],[col2], [col3]], columns=['Features'])
reg_summery['Weights'] = reg.intercept_, reg.coef_[0], reg.coef_[1]
reg_summery['p-values'] = '---', p_vals.round(3)[0], p_vals.round(3)[1]
print('Weight and Bias table:\n', reg_summery, '\n')

# Make Predictions
if predict:
  # 1 data
  new_data = pd.DataFrame(data=[[1700,2],[1800,1]], columns=[col2, col3])
  new_data_scaled = scaler.transform(new_data)
  print('Making Predictions:\n', reg.predict(new_data))

