import os 
import pandas as pd
os.chdir("C:\\Users\\Srinivas M K\\MSBAnDS Python Workspace\\VaccineSentimentAnalysis\\data")

import pandas as pd
Input_df = pd.read_csv("sem_output.csv")
Input_df.head()

common_terms = ['vaccin','covid19','covid','get','booster']
Input_df['text_cleaned'] = Input_df['text_cleaned'].apply(lambda x: " ".join(x for x in x.split() if x not in common_terms)) 

Input_df_Positive = Input_df[Input_df.stanza_sentiment == "Positive"]
Input_df_Neutral = Input_df[Input_df.stanza_sentiment == "Neutral"]
Input_df_Negative = Input_df[Input_df.stanza_sentiment == "Negative"]

from sklearn.feature_extraction.text import CountVectorizer

# POSITIVE TWEETS

vectorizer = CountVectorizer()
Output_df_Positive = pd.DataFrame(vectorizer.fit_transform(Input_df_Positive['text_cleaned']).toarray(), columns=vectorizer.get_feature_names())
Output_df_Positive.head()

print(Output_df_Positive.columns.tolist())

Sort_Output_Positive = Output_df_Positive.sum()
Sort_Output_Positive.head()

Sort_Output_Positive.sort_values(ascending = False).head(10)
Sort_Output_Positive = pd.DataFrame(Sort_Output_Positive)
Sort_Output_Positive.reset_index(inplace=True)
Sort_Output_Positive.columns = ['Terms','Frequency']

Sort_Output_Positive.sort_values(ascending=False,inplace=True,by='Frequency')
Sort_Output_Positive.head()
Sort_Output_Positive.to_csv("C:\\Users\\Srinivas M K\\MSBAnDS Python Workspace\\VaccineSentimentAnalysis\\data\\WordClouds_Positive.csv")

# NEGATIVE TWEETS 

vectorizer = CountVectorizer()
Output_df_Negative = pd.DataFrame(vectorizer.fit_transform(Input_df_Negative['text_cleaned']).toarray(), columns=vectorizer.get_feature_names())
Output_df_Negative.head()

print(Output_df_Negative.columns.tolist())

Sort_Output_Negative = Output_df_Negative.sum()
Sort_Output_Negative.head()

Sort_Output_Negative.sort_values(ascending = False).head(10)
Sort_Output_Negative = pd.DataFrame(Sort_Output_Negative)
Sort_Output_Negative.reset_index(inplace=True)
Sort_Output_Negative.columns = ['Terms','Frequency']
Sort_Output_Negative.sort_values(ascending=False,inplace=True,by='Frequency')
Sort_Output_Negative.head()

Sort_Output_Negative.to_csv("C:\\Users\\Srinivas M K\\MSBAnDS Python Workspace\\VaccineSentimentAnalysis\\data\\WordClouds_Negative.csv")

# NEUTRAL TWEETS 

vectorizer = CountVectorizer()
Output_df_Neutral = pd.DataFrame(vectorizer.fit_transform(Input_df_Neutral['text_cleaned']).toarray(), columns=vectorizer.get_feature_names())
Output_df_Neutral.head()

print(Output_df_Neutral.columns.tolist())

Sort_Output_Neutral = Output_df_Neutral.sum()
Sort_Output_Neutral.head()

Sort_Output_Neutral.sort_values(ascending = False).head(10)
Sort_Output_Neutral = pd.DataFrame(Sort_Output_Neutral)
type(Sort_Output_Neutral)
Sort_Output_Neutral.reset_index(inplace=True)
Sort_Output_Neutral.columns = ['Terms','Frequency']
Sort_Output_Neutral.head()
Sort_Output_Neutral.sort_values(ascending=False,inplace=True,by='Frequency')
Sort_Output_Neutral.head()

Sort_Output_Neutral.to_csv("C:\\Users\\Srinivas M K\\MSBAnDS Python Workspace\\VaccineSentimentAnalysis\\data\\WordClouds_Neutral.csv")