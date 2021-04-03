import pandas as pd
import numpy as np
from data_frame_HM3 import df
import find_HM3

df1 = df.copy()
df2 = df.copy()

Purpose = df["Purpose"].values.tolist() #transform column in to list
sentiment = find_HM3.find_sent(Purpose) # find sentiment


##### Two different resutl for the sentyment analysis:

## NLTK
df1["NLTK_Sentiment"] = sentiment[0]
NLFK_top_best = df1.sort_values(by='NLTK_Sentiment', ascending=False).head(10)
NLFK_top_worst = df1.sort_values(by='NLTK_Sentiment', ascending=True).head(10)
print (f'\n\n\nThis is the first analysis using the NLTK sentiment analysis method.\nThe best ten positive result are:\n{NLFK_top_best} \n\n\nThe worst ten result are:\n{NLFK_top_worst} ')


## BlobTEXT
df2["BlobText_sentiment"] = sentiment[1]
BlobTEXT_top_best = df2.sort_values(by='BlobText_sentiment', ascending=False).head(10)
BlobTEXT_top_worst = df2.sort_values(by='BlobText_sentiment', ascending=True).head(10)
print (f'\n\n\nThis is the second analysis using the BlobTEXT sentiment analysis method.\nThe best ten positive result are:\n{BlobTEXT_top_best} \n\n\nThe worst ten result are:\n{BlobTEXT_top_worst} ')