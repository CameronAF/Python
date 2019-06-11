The Accuracy of Clustering

REQUIRMENTS:
 - Python3 32-bit (not 64-bit)
 - numpy
 
SETUP:
Downloading the proper library
 1) Open Command Prompt
	1. Navigate to the location of the pip folder in command prompt.
        - example: cd C:\Python\Scripts
    2. Enter command to install NLTK: pip3 install numpy

HOW TO USE:
 1) put what cluster file and samples file in the same location as the project
 2) run the program
	 -  output is displayed in the window
	 
ABOUT THE PROGRAM:
This program calculates the accuracy of clustering given clusters and samples.

The program was designed to be used with any number of clusters and any number of samples. The program first opens the files and count the number of clusters and samples in a cluster file and class file. A matrix is created based on the number of clusters and classes in the file. The files are then reopened and traversed to populate the matrix. In a loop of all permutations of class, a sum is calculated, and the maximum sum is saves. The Accuracy is then calculated with the maximum sum from the previous loop and the number of samples.