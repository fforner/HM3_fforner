
import pandas as pd
import numpy as np
from data_frame_HM3 import df
import find_HM3


Purpose = df[["Purpose"]]
Purpose = df["Purpose"].values.tolist()


sentiment = find_HM3.find_sent(Purpose)

df["NLTK_Sentiment"] = sentiment[0]
df["BlobText_sentiment"] = sentiment[1]

df_blob = df.sort_values(by='BlobText_sentiment', ascending=False)
print (df_blob.head(10))


print(f'\n\n\n\n')
df_NLTK= df.sort_values(by='NLTK_Sentiment', ascending=False)
print (df_NLTK.head(10))
    
