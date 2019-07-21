import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Allways create meaningfull regressions 
# Predict if a student will attend this university based on SAT scores
# Predict if the client will subscribe a term deposit (variable y)

# Load the data (Admitted, SAT) or (y, duration) by changing the if statment
if 1 == 1:
  raw_data = pd.read_csv('Admittance.csv')
  col1 = str(raw_data.columns[1]) #Admitted
  col2 = str(raw_data.columns[0]) #SAT
  yes = 'Yes'
  no = 'No'
else:
  raw_data = pd.read_csv('Bank Data.csv')
  col1 = str(raw_data.columns[2]) #y
  col2 = str(raw_data.columns[1]) #duration
  yes = 'yes'
  no = 'no'
print('The Data:\n', raw_data.head(), '\n')

# convert to dummies
data = raw_data.copy()
data[col1] = data[col1].map({yes:1, no:0})

# Usefull statastics from the data frame
print('The Data Described:\n', data.describe(), '\n')

# Declare the dependent and independent variables
y = data[col1] # target (output)
x1 = data[col2] # feature (input)

# need a constant
x = sm.add_constant(x1)

# LINEAR REGRESSION
# this is data is not linear and not a good fit
reg_lin = sm.OLS(y,x)
results_lin = reg_lin.fit()
plt.scatter(x1,y, color='C0')
y_hat = x1*results_lin.params[1]+results_lin.params[0]
plt.plot(x1,y_hat,lw=2.5,color='C8')
plt.ylabel(col1,fontsize='20')
plt.xlabel(col2,fontsize='20')
plt.show()
plt.clf()
plt.cla()
plt.close()


# LOGISTIC REGRESSION
def f(x,b0,b1):
  return np.array(np.exp(b0+x*b1) / (1 + np.exp(b0+x*b1)))

# Create Regression
# SM used ML algorithms and stops after 35 iterations
reg_log = sm.Logit(y,x)
results_log = reg_log.fit()
print(results_log.summary())

f_sorted = np.sort(f(x1,results_log.params[0], results_log.params[1]))
x_sorted = np.sort(np.array(x1))

plt.scatter(x1,y, color='C0')
plt.plot(x_sorted,f_sorted,color='C8')
plt.ylabel(col1,fontsize='20')
plt.xlabel(col2,fontsize='20')
plt.show()
plt.clf()
plt.cla()
plt.close()