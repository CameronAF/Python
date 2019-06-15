#imports
import matplotlib.pyplot as plt
import gzip
import os
import numpy as np
np.random.seed(1234)

#keras imports
from keras.datasets import mnist
from keras.models import Sequential
import keras
from keras.layers import Dense, Activation, convolutional, MaxPooling2D, Dropout, Flatten
from keras import optimizers
from keras.utils import np_utils
from keras.utils.data_utils import get_file
from keras import backend as K
K.set_image_dim_ordering('th')
np.random.seed(1234)

# Global Parameters
# model choice 'cnn' to select a ConvNet, anything else defaults to mlp
model = 'cnn'
# batch size 
batch_size = 100
# number of training epochs
nb_epoch = 10
# data input dimensions (adjust to use other data such as cifar which would be 32,32,3)
img_rows, img_cols,img_channels = 28,28,1
  
#Loads the Fashion-MNIST dataset.  
def load_data():
  """Loads the Fashion-MNIST dataset.
  # Returns
      Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
  """
  dirname = os.path.join('datasets', 'fashion-mnist')
  base = 'http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/'
  files = ['train-labels-idx1-ubyte.gz', 'train-images-idx3-ubyte.gz',
             't10k-labels-idx1-ubyte.gz', 't10k-images-idx3-ubyte.gz']

  paths = []
  for file in files:
    paths.append(get_file(file, origin=base + file, cache_subdir=dirname))

  with gzip.open(paths[0], 'rb') as lbpath:
    y_train = np.frombuffer(lbpath.read(), np.uint8, offset=8)

  with gzip.open(paths[1], 'rb') as imgpath:
    x_train = np.frombuffer(imgpath.read(), np.uint8,
                                offset=16).reshape(len(y_train), 28, 28)

  with gzip.open(paths[2], 'rb') as lbpath:
    y_test = np.frombuffer(lbpath.read(), np.uint8, offset=8)

  with gzip.open(paths[3], 'rb') as imgpath:
    x_test = np.frombuffer(imgpath.read(), np.uint8,
                               offset=16).reshape(len(y_test), 28, 28)

  return (x_train, y_train), (x_test, y_test)
  
#pass your own data directory prefix as a parameter into this function
#type=string
# returns 4 numpy arrays
# X_train: training set features
# Y_train: training set labels
# X_test: test set features
# Y_test: test set labels
def load_data1():
  data_dir =  os.path.dirname(os.path.realpath(__file__))
  train = np.genfromtxt(data_dir+"fit.csv", delimiter=',')
  test = np.genfromtxt(data_dir+"test.csv", delimiter=',')
  X_train, y_train = train[:,:8], train[:,8:]
  X_test, y_test = test[:,:8], test[:,8:]
  X_train = X_train.astype('float32')
  X_test = X_test.astype('float32')
  Y_train = np_utils.to_categorical(y_train, 2)
  Y_test = np_utils.to_categorical(y_test, 2)
  return X_train, Y_train, X_test, Y_test

# mlp model
def mlp_model():
  model = Sequential()
  model.add(Dense(128, input_dim=(img_rows*img_cols)))
  model.add(Activation('relu'))
  model.add(Dense(128))
  model.add(Activation('relu'))
  model.add(Dense(10))
  model.add(Activation('softmax'))
  return model

# cnn model
def cnn_model():
  model = Sequential()
  model.add(convolutional.Conv2D(16, (3, 3), strides=1,
                        input_shape=(img_channels, img_rows, img_cols)))
  model.add(Activation('relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Flatten())
  model.add(Dense(128))
  model.add(Activation('relu'))
  model.add(Dropout(0.5))
  model.add(Dense(10))
  model.add(Activation('softmax'))
  return model

# load mnist data, format for cnn model
def load_mnist_cnn():
  # load data
  (x_train, y_train), (x_test, y_test) = load_data()
  # reshape data (for cnn)
  x_train = x_train.reshape(x_train.shape[0], img_channels, img_rows, img_cols)
  x_test = x_test.reshape(x_test.shape[0], img_channels, img_rows, img_cols)
  # need categorical classes
  y_train = keras.utils.to_categorical(y_train, 10)
  y_test = keras.utils.to_categorical(y_test, 10)

  return x_train, y_train, x_test, y_test

# load mnist data, format for mlp model
def load_mnist_mlp():
  # load data
  (x_train, y_train), (x_test, y_test) = load_data()
  # flatten data for mlp
  x_train = x_train.reshape(x_train.shape[0], img_rows*img_cols*img_channels)
  x_test = x_test.reshape(x_test.shape[0], img_rows*img_cols*img_channels)
  x_train = x_train.astype('float32')
  x_test = x_test.astype('float32')
  x_train /= 255
  x_test /= 255
  # need categorical classes
  y_train = keras.utils.to_categorical(y_train, 10)
  y_test = keras.utils.to_categorical(y_test, 10)

  return x_train, y_train, x_test, y_test

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

# controls which model is used based on model selection at top of code
if (model == 'cnn'):
  x_train, y_train, x_test, y_test = load_mnist_cnn()
  model = cnn_model()
else:
  x_train, y_train, x_test, y_test = load_mnist_mlp()
  model = mlp_model()

# define optimizer
adam = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)

# compile model
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
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