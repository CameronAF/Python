Multi-Layer Perceptron Neural Network Models from Keras using Tensorflow Backend

REQUIRMENTS:
 - Python3 environment with Keras using Tensorflow
 
SETUP:
Follow the 'Install Keras.pdf' in the repo or one of the many online tutorials to create a python environment that uses keras 

HOW TO USE:
 1) run the program
	 -  output loss and accuracy (Training data) and val_loss and val_acc (cross-validation) for each epoch
	 -  creates a plot of loss and val_loss over epoch
	 
ABOUT THE PROGRAM:
This program runs a Multi-Layer Perceptron Neural Network

This project will predict a class (0, 1) using multi-layer perceptron’s built in python using Keras. A multilayer perceptron (MLP) is a type of feedforward neural network that consist of at least three layers of nodes and uses supervised learning techniques for training. Eleven MLP networks were built using the fit class data set (fit.csv) and tested using a test data set (test.csv)

MODEL SPECIFICATIONS:
 1) Network specifications:        
     - Input dimension of 8
	 - One dense hidden layer with 3 nodes, sigmoid activation function
	 - One dense output layer with 2 nodes, softmax activation function 
 2) Compile specifications:
     - Uses the SGD optimizer: learning rate of 0.3, momentum of 0.2, Set decay to 0.0, nesterov to False
	 - Uses binary cross entropy for loss function
	 - Uses accuracy as a performance metric
 3) Training specifications:
     - Uses 10% of the data for validation
	 - Train for at least 500 epochs
	 - Uses a batch size of 100 asas 
