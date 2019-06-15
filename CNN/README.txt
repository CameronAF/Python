Convolutional Neural Network Models from Keras using Tensorflow Backend

REQUIRMENTS:
 - Python3 environment with Keras using Tensorflow
 
SETUP:
Follow the 'Install Keras.pdf' in the repo or one of the many online tutorials to create a python environment that uses keras 

HOW TO USE:
 1) Modify Neural Network
     1) Model: Choose CNN or MLP by modifying the global variable model
	 2) Batch Size: Change batch size but modifying global variable batch_size
	 3) epochs: Change the number of epochs by modifying global variable nb_epoch
     4) input dimentions: input dementions can be cahnged by modifying img_rows, img_cols, and img_channels
 1) run the program
	 -  output loss and accuracy (Training data) and val_loss and val_acc (cross-validation) for each epoch
	 -  creates a plot of loss and val_loss over epoch

	 
ABOUT THE PROGRAM:
This program runs a Multi-Layer Perceptron Neural Network

This project will evaluate a MLP and a CNN network in Keras using the Fashion MNIST dataset. Fashion MNIST consists of images of clothing belonging to one of 10 categories: T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle boot. Images are 28x28 pixels and grey scale, so there is 1 color channel with values between 0 and 255. Networks trained on this data will learn to recognize what category of clothing each image belongs to.