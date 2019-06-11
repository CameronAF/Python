#Cosine Similarities of document-term matrices 
import nltk
import sklearn
import string
import os

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#path of the documents to be compared
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\datasets"

stemmer =  PorterStemmer()
stop_words = set(stopwords.words("english"))
token_dict = {}

def tokenize(text):
    lower = text.lower()
    exclude = set(string.punctuation)
    s = ''.join(ch for ch in lower if ch not in exclude)
    token = nltk.word_tokenize(s)
    pure_text= stem_tokens(token, stemmer)
    return pure_text

def stem_tokens(text, stemmer):
    stemmed = []
    for word in text:
        stemmed.append(stemmer.stem(word))
    pure_text = remove_stop(stemmed)
    return pure_text

def remove_stop(text):
    filtered_text = []
    for word in text:
        if word not in stop_words:
            filtered_text.append(word)
    return filtered_text
  
#get and tokenize each document
n = 0
for root, dirs, files in os.walk(path):
    for file in files:
        file_path = root + os.path.sep + file
        print ("File Name:", end=' ')
        print (file, end='\n')
        doc_web = open(file_path, 'r')
        doc_n = doc_web.read()
        token_dict[n] = doc_n
        token = tokenize(doc_n)
        print ("Proccessed Text:", end='\n')
        print(token, end='\n\n')
        n = n + 1

#Convert collection to a matrix of TF-IDF features.
vectorizer = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = vectorizer.fit_transform(token_dict.values())
print("tf-idf Word Matrix:")
print(tfs, end='\n\n')

#calculate the Cosine Similarity between each document
print("Cosine Similarity Calculation:")
for i in range(0,n):
    for j in range(i,n):
        print("Similarity of document %d to document %d is equal to %.2f%%" % (i, j, cosine_similarity(tfs[i,:], tfs [j,:])*100))