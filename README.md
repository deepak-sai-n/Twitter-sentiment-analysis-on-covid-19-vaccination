# VaccineSentimentAnalysis
Sentiment analysis to summarize sentiment towards Covid-19 Vaccine from twitter data

Steps to run the project: Execute the following .py files in the given order.

data_collection.py - Initiate tweepy api, set the search keywords and collect the data, the collected data will be saved in the data folder as collected_tweets_(i).csv (i) = ith file, as these steps are carried out multiple times, and multiple files are generated in the process.

data_preprocessing.py - The collected_tweets_(i).csv is taken as an input and all the text cleaning and preprocessing steps are undertaken, the output processed_tweets_(i).csv is saved in the data file.

location_filtering_n_reduction.py - The processed_tweets_(i).csv is taken and the location country is assigned to the tweet based on the marked geo-tag, origin location of the tweet. Further, only 'United States' location country tweets are taken as the scope of the project is limited to the location 'US'.

data_consilidatation - many reduced_data_(i).csv files could be collected in the above iterative steps upto the step 3. In the step 4 we will merge all the csvs collected until now and remove the redudant rows if any, and the output is saved as full_reduced_data.csv

sentiment_analysis.py - full_reduced_data.csv is the input to this script, and it generates the sentiment for each tweet interms of +ve,-ve and neutral polarities, and also detect the emotion component in each tweet, for ex ( happy:0.25, sad:0.1, anger:0.1, surprise:.3, fear:0.1), additional columns are created in the data frame to assign the labels and the output is saved as sem_output.csv

topic_modelling.py - topic modelling is done on the labelled data set i.e sem output, to understand the summary of the tweets appeared within each section +ve, -ve and neutral. The output file is saved as topic_modelling_output.csv

named_entity_recognition.py - on the labelled data set i.e sem output, entity recognition is also performed to figure out the influential entities, output is saved as ner_output.csv

classification_model.py - on the labelled data set i.e sem output, classification model is built using random forest classifer.

WordCloud.py - on the labelled data set i.e sem output, the tfidf files are generated for each label (+ve,-ve, neutral seperately)

WordCloud.R - word clouds are generated for the visualizations for each label (+ve,-ve, neutral seperately)
