#Text-Mining

#Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import os
import re
import nltk

import numpy as np
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer, PorterStemmer

import ast


tweets_data = pd.read_csv('data\\collected_tweets3.csv')

# Setup function to extract hashtags text from the raw hashtag dictionaries
def extract_hashtags(hashtag_list):
    hashtag_list = ast.literal_eval(hashtag_list)
    s = "" # Create empty string
    if not hashtag_list: # If list is empty, return empty string
        return s
    else:
        for dictionary in hashtag_list:
            s+= str(dictionary['text'].lower() + ',') # Create string (lowercase) for each hashtag text
        s = s[:-1] # Drop last character ','
        return s

# Extract hashtags to text from the dictionary
#tweets_data['hashtags_extracted'] = tweets_data['hashtags'].apply(lambda x: extract_hashtags(x))
#tweets_data.drop(columns = 'hashtags', inplace = True)

# Keep only tweets that involve the vaccine
tweets_data = tweets_data[(tweets_data['text'].str.contains("vacc")) 
                            | (tweets_data['text'].str.contains("Vacc"))
                            | (tweets_data['hashtags_extracted'].str.contains("vacc"))
                            | (tweets_data['hashtags_extracted'].str.contains("Vacc"))]
#len(tweets_data)

# Function to remove Punctuations in the tweets
punct =['%','/',':','\\','&amp;','&',';']
def remove_punctuations(text):
    for punctuation in punct:
        text = text.replace(punctuation, '')
    return text

tweets_data.reset_index(drop=True,inplace=True)
tweets_data['text_cleaned'] = tweets_data['text']

# Convert text to lower case
tweets_data['text_cleaned'] = tweets_data['text_cleaned'].apply(lambda x: " ".join(x.lower() for x in x.split()))

# remove urls
tweets_data['text_cleaned'] = tweets_data['text_cleaned'].apply(lambda x:re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', x))

# Remove extra whitespaces between words
tweets_data['text_cleaned'] = tweets_data['text_cleaned'].apply(lambda x: " ".join(x.strip() for x in x.split()))

# Remove non-alphanumerics
tweets_data['text_cleaned'] = tweets_data['text_cleaned'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

#Remove pre-defined stop words
stop = stopwords.words('english')
tweets_data['text_cleaned'] = tweets_data['text_cleaned'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

#Remove numerical values
patterndigits = '\\b[0-9]+\\b'
tweets_data['text_cleaned'] = tweets_data['text_cleaned'].str.replace(patterndigits,'')

#Remove punctutations
tweets_data['text_cleaned'] = tweets_data['text_cleaned'].apply(lambda x: remove_punctuations(x))

#Stemming
porstem = PorterStemmer()
tweets_data['text_cleaned'] = tweets_data['text_cleaned'].apply(lambda x: " ".join([porstem.stem(word) for word in x.split()]))

#Lemmatization
lemma = WordNetLemmatizer()
tweets_data['text_cleaned'] = tweets_data['text_cleaned'].apply(lambda x: " ".join([lemma.lemmatize(word) for word in x.split()]))

#Export the pre-processed data to csv file
tweets_data.to_csv('data\\processed_tweets3.csv',index=False)
