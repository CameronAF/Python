import numpy as np
from sklearn.model_selection import train_test_split


a = np.arange(1,101)
b = np.arange(501,601)

a_train, a_test = train_test_split(a) #75/25 shuffled
a_train, a_test = train_test_split(a, test_size=0.2) #80/20 shuffled
a_train, a_test = train_test_split(a, test_size=0.2, shuffle = False) #80(1-80)/20(81-100) 
a_train, a_test = train_test_split(a, test_size=0.2, random_state=42) #80/20 shuffled the same way every time
a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.2) #80/20 shuffle of 2 data sets