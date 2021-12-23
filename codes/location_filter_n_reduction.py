#Data Reduction based on the country of the tweets generated
#Required Libraries
import pandas as pd
import numpy as np
from tqdm import tqdm
from geopy.geocoders import Nominatim


df = pd.read_csv('data\\processed_tweets3.csv')
len(df)
# Remove duplicate tweets
df.drop_duplicates(subset='text_cleaned', keep="first", inplace = True)
len(df)
# Drop tweets which have empty text field
df['text_cleaned'].replace(' ', np.nan, inplace=True)
df.dropna(subset=['text_cleaned'], inplace=True)
len(df)
# location filtering
if 'loc_country' in df.columns:
    df_us = df[df['loc_country']=='United States']
    df_nonus = df[df['loc_country']!='United States']
else: 
    df['loc_country'] = 'Unknown'
    df_us = df[df['location']=='United States']
    df_nonus = df[df['location']!='United States']


#Replacing the non United States locations to NA in the data frame
df_nonus['location'].fillna('NA',inplace=True)
df_nonus = df_nonus[df_nonus['location']!='NA']

#API initiation 
geolocator = Nominatim(user_agent = "geo_loc_processing")

df_nonus.reset_index(drop=True,inplace=True)
#checking the progess for each iteration (Progress bar)
for i in tqdm(range(0, len(df_nonus))):
    loc = df_nonus['location'][i]

    try: #Catching errors in checking the location 
        up_loc = str(geolocator.geocode(loc))
        if up_loc != 'None':
            df_nonus['loc_country'][i] = up_loc.split(',')[-1].strip()
        else : 
            df_nonus['loc_country'][i] = 'Enter Manually'
    except:
            df_nonus['loc_country'][i] = 'Enter Manually'
            print(i, loc)

df_nonus_us = df_nonus[df_nonus['loc_country']=='United States']

# combining all the dataframes and saving the csv
final_df = pd.concat([df_us,df_nonus_us])
final_df.reset_index(drop=True,inplace=True)
final_df.to_csv('data\\reduced_data3.csv',index=False)
