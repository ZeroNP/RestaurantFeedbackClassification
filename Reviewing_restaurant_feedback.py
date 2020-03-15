# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:52:18 2020

@author: Shreyas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#tab-seperated values (so delimiter='\t') and ignore quotes (so quoting =3)
dataset = pd.read_csv('Restaurant_Reviews.tsv',delimiter='\t',quoting = 3)

#Clean the data... remove stopwords, punctuation, stemming, ignore case, etc
import re
import nltk
from nltk.stem.porter import PorterStemmer
#Since nltk.download('stopwords') was giving an error at the time, 
#I compiled my own list of stopwords from the internet:

stop_words_list =  ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", 
                 "you", "your", "yours", "yourself", "yourselves", "he", "him", 
                 "his", "himself", "she", "her", "hers", "herself", "it", "its", 
                 "itself", "they", "them", "their", "theirs", "themselves", "what",
                 "which", "who", "whom", "this", "that", "these", "those", "am", 
                 "is", "are", "was", "were", "be", "been", "being", "have", "has",
                 "had", "having", "do", "does", "did", "doing", "a", "an", "the", 
                 "and", "but", "if", "or", "because", "as", "until", "while", "of",
                 "at", "by", "for", "with", "about", "against", "between", "into", 
                 "through", "during", "before", "after", "above", "below", "to",
                 "from", "up", "down", "in", "out", "on", "off", "over", "under", 
                 "again", "further", "then", "once", "here", "there", "when", "where",
                 "why", "how", "all", "any", "both", "each", "few", "more", "most", 
                 "other", "some", "such", "no", "nor", "only", "own", "same", 
                 "so", "than", "too", "very", "s", "can", "will", "just",
                 "should", "now"]


review_list = []
for i in range(1000):
    ps=PorterStemmer()
    cleaned_review = re.sub("[^A-Za-z]", ' ', dataset['Review'][i]) #remove punctuation
    cleaned_review = cleaned_review.lower()                         #ignore case
    cleaned_review = cleaned_review.split()
    cleaned_review = [ps.stem(word) for word in cleaned_review 
                      if word not in set(stop_words_list)]                #set for faster processing
    cleaned_review = ' '.join(cleaned_review)
    review_list.append(cleaned_review)

#tokenization
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features = 1500)
X = cv.fit_transform(review_list).toarray()                 #create sparse matrix

y=dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/5)


'''
#Naive Bayes Implementation:
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train,y_train)
'''
'''
#Decision Tree Implementation:
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion='entropy',)
classifier.fit(X_train,y_train)
'''

'''
#Random Forest Implementation:
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(criterion='gini',n_estimators=15)
classifier.fit(X_train,y_train)
'''

y_pred=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

print("Classification Report: \n", classification_report(y_test, y_pred))

print('Confusion Matrix: \n', confusion_matrix(y_test, y_pred))

print('Accuracy Score: \n', accuracy_score(y_test, y_pred))
