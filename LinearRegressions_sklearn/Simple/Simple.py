import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression

predict = False
# Allways create meaningfull regressions (y = b0 + b1*x1)
# Is someone more likely to graduate from University with a higher GPA if they got a higher SAT score?
# Are Houses more likely to be more expensive the bigger they are?

# Load the data (GPA, SAT) or (Price, Size) by changing the if statment
if 1 == 1:
  data = pd.read_csv('Simple linear regression.csv')
  col1 = str(data.columns[1]) #GPA
  col2 = str(data.columns[0]) #SAT
  predict = True
else:
  data = pd.read_csv('Real Estate Price Size.csv')
  col1 = str(data.columns[0]) #Price
  col2 = str(data.columns[1]) #Size
print('The Data:\n', data.head(), '\n')

# Usefull statastics from the data frame
print('The Data Described:\n', data.describe(), '\n')

# Regression 
# Declare the dependent and independent variables
y = data[col1] # target (output)
x = data[col2] # feature (input)
x_matrix = x.values.reshape(-1,1) #sklearn requires a 2D matrix
# create the regression
reg = LinearRegression()
reg.fit(x_matrix,y)

# R-Squared
reg.score(x_matrix, y)

# Coefficiennts
reg.coef_

# Intercept
reg.intercept_

# regression line: y = b0 + b1*x1
yhat = reg.intercept_ + (reg.coef_ * x_matrix)
# plot the data and regression line
plt.scatter(x,y)
fig = plt.plot(x, yhat, lw=2, c='orange', label='regression line')
plt.ylabel(col1,fontsize='20')
plt.xlabel(col2,fontsize='20')
plt.show()

# Make Predictions
if predict:
  # 1 data
  reg.predict(1740)
  # multiple data
  new_data = pd.DataFrame(data=[1740,1760], columns=[col2])
  reg.predict(new_data)

  new_data['Predicted_GPA'] = reg.predict(new_data)
  print('Making Predictions:\n',new_data)