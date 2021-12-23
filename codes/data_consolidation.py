import pandas as pd
import numpy as np

# collecting the data frames of the pre-preocssing and the location filtering.
df1 = pd.read_csv('data\\reduced_data1.csv')
df2 = pd.read_csv('data\\reduced_data2.csv')
df3 = pd.read_csv('data\\reduced_data3.csv')

full_df = pd.concat([df1,df2,df3])
len(full_df)

# removing duplicates if any
full_df.drop_duplicates(inplace=True)
len(full_df)
full_df.reset_index(drop=True,inplace=True)
# saving to csv
full_df.to_csv('data\\full_reduced_data.csv',index=False)