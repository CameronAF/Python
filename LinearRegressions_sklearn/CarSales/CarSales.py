import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def adj_r2(x,y):
  r2 = reg.score(x,y)
  n = x.shape[0]
  p = x.shape[1]
  adjusted_r2 = 1-(1-r2)*(n-1)/(n-p-1)
  return adjusted_r2

# Allways create meaningfull regressions (y = b0 + b1*x1)
# can we predict the price of a car?

# Load the data (Price, Brand, Body, Mileage, EngineV, Engine Type, Registration, Year, Model)
raw_data = pd.read_csv('Car Sales.csv')
print("The Data:\n", raw_data.head(), '\n')
print("The Data Described:\n", raw_data.describe(include = 'all'), '\n')

# ---CLEAN THE DATA---
# drop useless features Model as this means nothing to us. 312 unique Models
# lots of info from Model could be engineered from Brand, Year, and EngineV
data = raw_data.drop(['Model'], axis=1) 

# MISSING DATA (if removing <5% then remove all that have the missing value)
# sum all missing values
#print(data.isnull().sum())
# Remove rows with missing values
data_no_mv = data.dropna(axis=0)

# EXPLORE PFD 
#sns.distplot(data_no_mv['Price'])
#sns.distplot(data_no_mv['Mileage'])
#sns.distplot(data_no_mv['EngineV'])
#sns.distplot(data_no_mv['Year'])

# DEALING WITH OUTLIERS: Price, Mileage, EngineV, & Year
# get top 1% of prices
q = data_no_mv['Price'].quantile(0.99)
# remove top 1%
data_1 = data_no_mv[data_no_mv['Price']<q]

q = data_1['Mileage'].quantile(0.99)
data_2 = data_1[data_1['Mileage']<q]

data_3 = data_2[data_2['EngineV']<6.5]

q = data_3['Year'].quantile(0.01)
data_4 = data_3[data_3['Year']>q]

# FINISHED CLEANING
# Create a data variable and reset the index for cleaned data
data_cleaned = data_4.reset_index(drop=True)
data_cleaned.describe(include='all')


# ---CHECKING OLS ASSUMPTIONS---
# 1) Linearity
# the following are exponential and not linear and need to be transformed 
f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey = True, figsize = (15, 3))
ax1.scatter(data_cleaned['Year'], data_cleaned['Price'])
ax1.set_title('Price and Year')
ax2.scatter(data_cleaned['EngineV'], data_cleaned['Price'])
ax2.set_title('Price and EngineV')
ax3.scatter(data_cleaned['Mileage'], data_cleaned['Price'])
ax3.set_title('Price and Mileage')
#plt.show()
plt.clf()
plt.cla()
plt.close()

# Relaxing the assumption
log_price = np.log(data_cleaned['Price'])
data_cleaned['log_price'] = log_price
data_cleaned = data_cleaned.drop(['Price'], axis = 1)

# 2) No Endogenity
# assumtion not violated

# 3) Normality, Zero Mean, Equal Variance
# assumed for a big sample following the Central Limit Theorem 
# acomplished by including the intercept in the regreasion, which we already did
# homoscedasticity general holds as we see in the graph, 
#   this is because log transform is method used to fix this, which we already used

# 4) No Autocrrelation
# safe becouse not time series data or panel data

# 5) No Multicollinearity
# check using VIF (variance inflation factor)
# VIF under 5 is ok. 5 though 10 may be unacceptable at the users discretion. Over 10 is unacceptable
variables = data_cleaned[['Mileage', 'Year', 'EngineV']]
vif = pd.DataFrame()
vif["VIF"] = [variance_inflation_factor(variables.values, i ) for i in range(variables.shape[1])]
vif["features"] = variables.columns
#print(vif)
# Year is over 10 VIF, drop it
data_no_multicollinearity = data_cleaned.drop(['Year'], axis = 1)


# ---CREATE DUMMY VARIABLES---
data_with_dummies = pd.get_dummies(data_no_multicollinearity, drop_first = True)
# testing VIF for dummes, all were under 2

# put depending in first column
#print(data_with_dummies.columns.values) 
cols=['log_price', 'Mileage', 'EngineV', 'Brand_BMW', 'Brand_Mercedes-Benz',
 'Brand_Mitsubishi', 'Brand_Renault', 'Brand_Toyota', 'Brand_Volkswagen',
 'Body_hatch', 'Body_other', 'Body_sedan', 'Body_vagon', 'Body_van',
 'Engine Type_Gas', 'Engine Type_Other', 'Engine Type_Petrol',
 'Registration_yes']
data_preprocessed = data_with_dummies[cols]


# ---LINEAR REGRESSION MODEL---
# Declare the inputs and the targets
targets = data_preprocessed['log_price']
inputs = data_preprocessed.drop(['log_price'], axis = 1)

# Scale the data
# not usually recommended to standardize dummy variables but we do it in ML
# a custom scaler which standerdizes only the continuous variables while leaving the dummys unchanged is often used
# subtract the mean and divide by the standard deviation
scaler = StandardScaler()
# calculate and store the mean and sd of each feature
scaler.fit(inputs)
inputs_scales = scaler.transform(inputs)

# split into Test and Train
x_train, x_test, y_train, y_test = train_test_split(inputs_scales, targets, test_size=0.2, random_state=365)

# Create the regression (log-linear since price is log_price)
reg = LinearRegression()
reg.fit(x_train,y_train)

# check model by ploting predicted against observed. 
# should be linear model with slop of 1, or close to it
y_hat = reg.predict(x_train)
plt.scatter(y_train,y_hat)
plt.title("The Model - Train data", size=18)
plt.xlabel('Target (y_train)',fontsize='20')
plt.ylabel('Predicted (y_hat)',fontsize='20')
plt.xlim(6,13)
plt.ylim(6,13)
plt.show()
plt.clf()
plt.cla()
plt.close()

# check Residual plot - The difference between the target and the predictions
# mean is zero and normaly distributed. this is good
# longer negative tail mean some predictions over-estimate the target
# short positive tail means rarely are predictions under-estimated
sns.distplot(y_train - y_hat)
plt.title("Residuals PDF", size=18)

# R-squared
print("R-squared: ", reg.score(x_train,y_train), '\n')

# Weight
# closer to 0 means its not a usefull feature
# the dropped dummy is the bench mark, all other are negative or positive showing order of category value
reg_summery = pd.DataFrame(inputs.columns.values, columns=['Features'])
reg_summery['Weights'] = reg.coef_
print('Weights of each Feature:\n', reg_summery, '\n')

# ---TESTING---
# Find prediction and plot agains test targets
# model is better at predicting higher priced cars then lower prices, but still not bad
y_hat_test = reg.predict(x_test)
plt.title("The Model - Test data heat map", size=18)
plt.scatter(y_test,y_hat_test, alpha = 0.2)
plt.xlabel('Target (y_train)',fontsize='20')
plt.ylabel('Predicted (y_hat_test)',fontsize='20')
plt.xlim(6,13)
plt.ylim(6,13)
plt.show()
plt.clf()
plt.cla()
plt.close()

# how good are these predictions?
# get predictions with original prices
df_pf = pd.DataFrame(np.exp(y_hat_test), columns = ['Prediction'])
# reset index and add y-test to df_pf
y_test = y_test.reset_index(drop = True)
df_pf['Target'] = np.exp(y_test)
# show Residual SSE since OLR tries to minimize SSE 
df_pf['Residual'] = df_pf['Target'] - df_pf['Prediction']
df_pf['Difference%'] = np.absolute(df_pf['Residual']/df_pf['Target']*100)
# 25%, 50%, and 75% are under 40% , this is good
# Max diiffence% is very much off target. we want low diiffence%. What happened?
print('Describing the Predictions:\n', df_pf.describe())

# observed processed are very low for these with high diiffence%
# we could be missing an important facter like one removed or another that wasnt present (e.i. was the car in an accident)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
#print(df_pf.sort_values(by=['Difference%'], ascending=False))

# ---HOW TO IMPROVE--
# 1) use a different set of variables
# 2) Remove a bigger part of the outliers
# 3) Use different kinds of transformations