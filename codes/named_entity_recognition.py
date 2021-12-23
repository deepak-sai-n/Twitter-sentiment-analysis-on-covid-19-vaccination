#Named-Entity_Recognition

#Required Libraries
from pickle import FALSE
import pandas as pd
import numpy as np
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import nltk
from nltk.stem import PorterStemmer

from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

#Read the data data collected in the previous step
tweets_data = pd.read_csv('data\\sem_output.csv')


#===========================================
# Tokenize using POST and use NER chunker;
# this could take a lot of processing, 
# depending on the length of the data
#===========================================

#Defining the dictionary for various topics
ner_dictionary ={'Positive':[], 'Neutral':[], 'Negative':[]} 

for topic_d in ner_dictionary.keys():
    #print(topic_d)
    tweets_data_part = tweets_data[tweets_data['stanza_sentiment']==topic_d]
    tweets_data_part['NN'] = ''
    tweets_data_part['JJ'] = ''
    tweets_data_part['VB'] = ''
    tweets_data_part['GEO'] = ''

    # function to  identify NER
    def tweet_ner(chunker):
        treestruct = ne_chunk(pos_tag(word_tokenize(chunker)))
        entitynn = []
        entityjj = []
        entityg_air = []
        entityvb = []
        for y in str(treestruct).split('\n'):
            if 'GPE' in y or 'GSP' in y:
                entityg_air.append(y)
            elif '/VB' in y:
                entityvb.append(y)
            elif '/NN' in y:
                entitynn.append(y)
            elif '/JJ' in y:
                entityjj.append(y)
        stringnn = ''.join(entitynn)
        stringjj = ''.join(entityjj)
        stringvb = ''.join(entityvb)
        stringg = ''.join(entityg_air)
        return stringnn, stringjj, stringvb, stringg

    # Dividing the tweet tokens to different groups
    i = 0
    for x in tweets_data_part['text_cleaned']:
        entitycontainer = tweet_ner(x)
        tweets_data_part.at[i,'NN'] = entitycontainer[0]
        tweets_data_part.at[i,'JJ'] = entitycontainer[1]
        tweets_data_part.at[i,'VB'] = entitycontainer[2]
        tweets_data_part.at[i,'GEO'] = entitycontainer[3]
        i += 1

    #Create new column for nouns, verbs, adjectives, and geo-location elements
    ner_nouns = tweets_data_part['NN'].unique().tolist()
    #tweets_data_part['JJ'].unique().tolist()
    #tweets_data_part['VB'].unique().tolist()
    #tweets_data_part['GEO'].unique().tolist()
    ner_dictionary[topic_d].append(ner_nouns)

# saving to csv
ner_df = pd.DataFrame(ner_dictionary.values(),index=ner_dictionary.keys(),columns=['Recognized Entities'])
ner_df.to_csv('data\\ner_output.csv')
