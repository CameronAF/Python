import numpy as np #Multidimensionals arrays
import pandas as pd #Organize data in a tabular form 
import matplotlib.pyplot as plt #Plotting library
import statsmodels.api as sm #Simplifies Machine Learning for user
import seaborn as sns #Upgrade for matplotlib
#import scipy #Python ecosystem w/ tools for scientific calculations
#import sklearn #Machine learning
sns.set()

plot = False
# Allways create meaningfull regressions (y = b0 + b1*x1)
# Is someone more likely to graduate from University with a higher GPA if they got a higher SAT score and higher attendance?
# Are Houses more likely to be more expensive the bigger they are, the how old they are, and they have a view of the sea?

# Load the data (GPA, SAT, Attendance) or (Price, Size, Year, View) by changing the if statment
if 1 == 1:
  data = pd.read_csv('Dummies.csv')
  data['Attendance'] = data['Attendance'].map({'Yes': 1, 'No': 0})
  col1 = str(data.columns[1]) #GPA
  col2 = str(data.columns[0]) #SAT
  col3 = str(data.columns[2]) #Attendance
  # Define the dependent and independent variables
  y = data[col1]
  x1 = data[[col2, col3]]
  plot = True
else:
  data = pd.read_csv('Real_Estate_Price_Size_Year_View.csv')
  data['view'] = data['view'].map({'Sea view': 1, 'No sea view': 0})
  col1 = str(data.columns[0]) #Price
  col2 = str(data.columns[1]) #Size
  col3 = str(data.columns[2]) #Year
  col4 = str(data.columns[3]) #View
  # Define the dependent and independent variables
  y = data[col1]
  x1 = data[[col2, col3, col4]]

# Usefull statastics from the data frame
print(data)
print(data.describe())

# Regression 
# Add a constent of 1 to find b0
x = sm.add_constant(x1)
# Fit the model using Ordinary Least Squares Regression
results = sm.OLS(y,x).fit()
print(results.summary())

# plot if the using the first csv
if plot:
  # regression line: y = b0 + b1*x1
  b0 = round(results.params[0],4)
  b1 = round(results.params[1],4)
  b2 = round(results.params[2],4)
  yhat_1 = b0 + (b1 * data[col2])
  yhat_2 = b0 + b2 + (b1 * data[col2])
  # plot the data and regression line
  plt.scatter(data[col2],data[col1], c=data[col3], cmap='RdYlGn_r')
  fig = plt.plot(data[col2], yhat_1, lw=2, c='green', label='regression line')
  fig = plt.plot(data[col2], yhat_2, lw=2, c='red', label='regression line')
  plt.ylabel(col1,fontsize='20')
  plt.xlabel(col2,fontsize='20')
  #plt.show()

  # making Predictions
  # create new data orgonized the same was as x
  new_data = pd.DataFrame({'const':1, 'SAT':[1700,1670], 'Attendance':[0,1]})
  new_data = new_data[['const', 'SAT', 'Attendance']]
  new_data.rename(index={0:'Bob', 1:'Alice'})
  print(new_data)
  # make a prediction with the new data
  predictions = results.predict(new_data)
  # transform predictions to a dataframe and join with the original data
  predictionsdf=pd.DataFrame({'Predictions':predictions})
  joined = new_data.join(predictionsdf)
  joined.rename(index={0:'Bob', 1:'Alice'})
  print(joined)
