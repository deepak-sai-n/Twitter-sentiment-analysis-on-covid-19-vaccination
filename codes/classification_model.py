import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re
import nltk
import seaborn as sns
import numpy as np
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer, PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier

tweets_data = pd.read_csv('data\\sem_output.csv')

features = tweets_data['text_cleaned']

# Use only the 2500 most frequently occurring terms
# Use only those terms that occur in a maximum of 80% of the documents
# but at least in 7 documents
vectorizer = TfidfVectorizer (max_features=2500, min_df=5, max_df=0.8, stop_words='english')

processed_features = vectorizer.fit_transform(features).toarray()



#==========================================
# Generate a training and testing dataset
#==========================================
labels = tweets_data['stanza_sentiment']

# Test dataset will be 20%
# Results in a training set of 80%
X_train, X_test, y_train, y_test = train_test_split(processed_features, labels, test_size=0.2, random_state=11)

# Train a machine learning model, randomforest, using
# the training dataset
text_classifier = RandomForestClassifier(n_estimators=200, random_state=0)
text_classifier.fit(X_train, y_train)

# Time to test the model using the predict() function
predictions = text_classifier.predict(X_test)


#===================================
# Evaluate the newly trained model
#===================================
cm = confusion_matrix(y_test,predictions)
print(cm)

plot_confusion_matrix(text_classifier, X_test, y_test)
plt.savefig('assets\\confusion_matrix_new.png')

print(classification_report(y_test,predictions))

print(accuracy_score(y_test, predictions))
