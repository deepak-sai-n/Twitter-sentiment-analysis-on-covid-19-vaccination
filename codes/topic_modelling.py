#Topic Modelling

#Required Libraries
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

tweets_data = pd.read_csv('data\\sem_output.csv')
topic_dictionary ={'Positive':[], 'Neutral':[], 'Negative':[]} 


for topic_d in topic_dictionary.keys():
    #print(topic_d)
    try:
        tweets_data_part = tweets_data[tweets_data['stanza_sentiment']==topic_d]
        vectorizer = CountVectorizer(max_df=0.8, min_df=4, stop_words='english')
        doc_term_matrix = vectorizer.fit_transform(tweets_data_part['text_cleaned'].values.astype('U'))

        # Generate the LDA with 3 topics to divide the text into; set the seed to 35 so that we end up with the same result
        LDA = LatentDirichletAllocation(n_components=3, random_state=35)
        LDA.fit(doc_term_matrix)
    except:
        continue
    #Print the 10 words with highest probabilities for all three topics
    for i,topic in enumerate(LDA.components_):
        extracted_topics = [vectorizer.get_feature_names()[i] for i in topic.argsort()[-10:]]
        topic_dictionary[topic_d].append(extracted_topics)

print(topic_dictionary)
# saving to csv
topic_out_df = pd.DataFrame([topic_dictionary.values()],columns=topic_dictionary.keys())
topic_out_df = topic_out_df.transpose()
topic_out_df.columns = ['Topics']
topic_out_df.to_csv('data\\topic_model_output.csv')