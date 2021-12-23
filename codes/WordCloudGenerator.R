install.packages("wordcloud")
install.packages("RColorBrewer")

library(RColorBrewer)
library(wordcloud)

library(devtools)
devtools::install_github("lchiffon/wordcloud2")
library(wordcloud2)

library(tidyverse)


setwd("C:\\Users\\Srinivas M K\\MSBAnDS Python Workspace\\VaccineSentimentAnalysis\\data")
Positive <- read.csv("WordClouds_Positive.csv")
Positive <- subset(Positive,select = c('Terms','Frequency'))


wordcloud(words = Positive$Terms, freq = Positive$Frequency, min.freq = 30,           
          max.words=200, random.order=FALSE, rot.per=0.35,            
          colors=brewer.pal(8, "Dark2"))

wordcloud2(Positive, figPath = "C:\\Users\\Srinivas M K\\MSBAnDS Python Workspace\\VaccineSentimentAnalysis\\assets\\Thumbsup_Positive.png", size = 1, color = "green")

Neutral <- read.csv("WordClouds_Neutral.csv")
Neutral <- subset(Neutral,select = c('Terms','Frequency'))

wordcloud(words = Neutral$Terms, freq = Neutral$Frequency, min.freq = 20,           
          max.words=200, random.order=FALSE, rot.per=0.35,            
          colors=brewer.pal(8, "Dark2"))

wordcloud2(Neutral, figPath = "C:\\Users\\Srinivas M K\\MSBAnDS Python Workspace\\VaccineSentimentAnalysis\\assets\\Thumbsup_Neutral.png", size = 1, color = "Blue")

Negative <- read.csv("WordClouds_Negative.csv")
Negative <- subset(Negative,select = c('Terms','Frequency'))
wordcloud(words = Negative$X, freq = Negative$X0, min.freq = 1,           
          max.words=200, random.order=FALSE, rot.per=0.35,            
          colors=brewer.pal(8, "Dark2"))

wordcloud2(Negative, figPath = "C:\\Users\\Srinivas M K\\MSBAnDS Python Workspace\\VaccineSentimentAnalysis\\assets\\Thumbsup_Negative.png", size = 1, color = "Red")

