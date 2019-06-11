Cosine Similarities of document-term matrices 

REQUIRMENTS:
 - Python3 32-bit (not 64-bit)
 - sklearn library
 - nltk library
 
SETUP:
Downloading the proper library
 1) Open Command Prompt
	1. Navigate to the location of the pip folder in command prompt.
        - example: cd C:\Python\Scripts
    2. Enter command to install NLTK: pip3 install nltk
    3. Enter command to install sklearn: pip3 install sklearn
 2) Open PythonShell or similarity python environment
	1. Enter commands to open nltk download window
	  >>> import nltk
	  >>> nltk.download()
    2. download 'all-corpora' under Collections tab

HOW TO USE:
 1) put what text files you want to compare in the 'dataset' folder
 2) run the program
	 -  output is displayed in the window
	 
ABOUT THE PROGRAM:
In short, this program calculate similarity between text files.

This program converts a collection of raw documents to a matrix of TF-IDF (term frequency–inverse document frequency) features.
Vocabulary and idf are learned from the set and transformed to a document-term matrix.
The cosine similarity is then calculated between each document-term matrix.
