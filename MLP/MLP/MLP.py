#imports
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import optimizers
from keras import backend as K
from keras.utils import np_utils
import matplotlib.pyplot as plt
import numpy as np
import os

# Global Parameters
# random seed
np.random.seed(1234)
# mlp model 
model = 'mlp'
# batch size and number of training epochs
batch_size = 100
nb_epoch = 500

  # mlp model
def mlp_model():
  model = Sequential()
  model.add(Dense(3, input_dim=8))
  model.add(Activation('sigmoid'))
  model.add(Dense(2))
  model.add(Activation('softmax'))
  return model
 
  # load mnist data, format for mlp model 
def load_data():
  data_dir =  os.path.dirname(os.path.realpath(__file__))
  train = np.genfromtxt(data_dir+"\\fit.csv", delimiter=',')
  test = np.genfromtxt(data_dir+"\\test.csv", delimiter=',')
  X_train, y_train = train[:,:8], train[:,8:]
  X_test, y_test = test[:,:8], test[:,8:]
  X_train = X_train.astype('float32')
  X_test = X_test.astype('float32')
  Y_train = np_utils.to_categorical(y_train, 2)
  Y_test = np_utils.to_categorical(y_test, 2)
  return X_train, Y_train, X_test, Y_test

  # plots training and validation loss
def plot_losses(history):
  plt.plot(history.history['loss'])
  plt.plot(history.history['val_loss'])
  plt.title('model loss')
  plt.ylabel('loss')
  plt.xlabel('epoch')
  plt.legend(['train', 'val'], loc='upper left')
  plt.savefig('plot.png')
  plt.show() 
  
# make mlp model  
x_train, y_train, x_test, y_test = load_data()
model = mlp_model()

# define optimizer
sgd = optimizers.SGD(lr=0.3, momentum=0.2, decay=0.0, nesterov=False)

# compile model and specifications
model.compile(loss='binary_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])
              
# train model on training data
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=nb_epoch,
          verbose=1, validation_split=0.1)
          
# scores model on test data for chosen metric (accuracy)          
score = model.evaluate(x_test, y_test, verbose=0)

# print accuracy 
print(score[1])

# plots loss for training and validation data
plot_losses(history)

# ends session, avoids potential error on program exit
K.clear_session()