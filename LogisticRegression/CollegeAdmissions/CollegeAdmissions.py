import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Confusion matrix:
# Parameters
  # data: data frame or array
    # data is a data frame formatted in the same way as your input data (without the actual values)
    # e.g. const, var1, var2, etc. Order is very important!
  # actual_values: data frame or array
    # These are the actual values from the test data
    # In the case of a logistic regression, it should be a single column with 0s and 1s                
# model: a LogitResults object
    # this is the variable where you have the fitted model 
# ----------
def confusion_matrix(data,actual_values,model):            
  #Predict the values using the Logit model
  pred_values = model.predict(data)
  # Specify the bins 
  bins=np.array([0,0.5,1])
  # Create a histogram, where if values are between 0 and 0.5 tell will be considered 0
  # if they are between 0.5 and 1, they will be considered 1
  cm = np.histogram2d(actual_values, pred_values, bins=bins)[0]
  # Calculate the accuracy
  accuracy = (cm[0,0]+cm[1,1])/cm.sum()
  # Return the confusion matrix and the accuracy
  return cm, accuracy

# Allways create meaningfull regressions 
# Predict if a student will attend this university based on SAT scores
# Predict if the client will subscribe a term deposit (variable y)

# Load the data (Admitted, SAT) or (y, duration) by changing the if statment
raw_data = pd.read_csv('Binary Predictors.csv')
print('The Data:\n', raw_data.head(), '\n')

# convert to dummies
data = raw_data.copy()
data['Admitted'] = data['Admitted'].map({'Yes':1, 'No':0})
data['Gender'] = data['Gender'].map({'Female':1, 'Male':0})

# Usefull statastics from the data frame
print('The Data Described:\n', data.describe(), '\n')

# Declare the dependent and independent variables
y = data['Admitted'] # target (output)
x1 = data[['SAT','Gender']] # feature (input)

# LOGISTIC REGRESSION
def f(x,b0,b1):
  return np.array(np.exp(b0+x*b1) / (1 + np.exp(b0+x*b1)))

# Create Regression
# SM used ML algorithms and stops after 35 iterations
x = sm.add_constant(x1)
reg_log = sm.Logit(y,x)
results_log = reg_log.fit()
print(results_log.summary(), '\n')

# Confusion Matrix
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
cm_df = pd.DataFrame(results_log.pred_table())
cm_df.columns = ['Predicted 0','Predicted 1']
cm_df = cm_df.rename(index={0:'Actual 0', 1:'Actual 1'})
print('Confusion Matrix:\n', cm_df, '\n')

# Accuracy
cm = np.array(cm_df)
accuracy_train = (cm[0,0]+cm[1,1])/cm.sum()
print('Accuracy:\n', accuracy_train, '\n\n')

# Testing 
# Pull test data
print('Testing Data:')
test = pd.read_csv('Test Dataset.csv')
test['Admitted'] = test['Admitted'].map({'Yes':1, 'No':0})
test['Gender'] = test['Gender'].map({'Female':1, 'Male':0})

# match and rerder the columns of the input data with those used to train the model
test_actual = test['Admitted']
test_data = test.drop(['Admitted'], axis=1)
test_data = sm.add_constant(test_data)
test_data = test_data[x.columns.values]

# Confusion Matrix
cm = confusion_matrix(test_data, test_actual, results_log)
cm_df = pd.DataFrame(cm[0])
cm_df.columns = ['Predicted 0','Predicted 1']
cm_df = cm_df.rename(index={0:'Actual 0', 1:'Actual 1'})
print('Confusion Matrix:\n', cm_df, '\n')

# Accuracy
print('Accuracy:\n', cm[1], '\n')

# Missclassification rate
print('Missclassification rate:\n', ((cm[0][0,1]+cm[0][0,1])/cm[0].sum()), '\n')
