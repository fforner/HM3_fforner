import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob 


def find_sent (list_analysis):
    '''IMPUT: list of strings. this function allow you to run a sentiemnt
            analysis in two differnet methods: vaderSentiment or textblob.
            1) it remove every type of punctation and it substitute witha space.
            2) strasform all strings in lower case.
            3) run vaderSentiment: compound score.
            4) run textblob: polarity score.
            '''
    if type(list_analysis) != list:
        raise TypeError('Please input a list.')
    
    elif type(list_analysis) == list:
        if type(list_analysis[0]) != str:
            raise TypeError('Please input a list of strings.')
        
        else:
            def clean(zio):
                ''' String cleaner from punctation'''
                import string
                for i in string.punctuation:
                    zio=zio.replace(i,' ')
                    return zio
                    pass
                
            ls = list()
            for i in list_analysis:
                k = clean(i)
                k = k.lower()
                ls.append(k)
            
            ls = list()
            for i in list_analysis:
                k = clean(i)
                k = k.lower()
                ls.append(k)
            analyser = SentimentIntensityAnalyzer()
            
            score_nltk = list()
            for i in list_analysis:
                score_description = analyser.polarity_scores(i)
                score_comppound = score_description['compound']
                score_nltk.append(score_comppound)
            score_blob = list()
            
            for i in list_analysis:
                blob = TextBlob(i)
                sentiment = blob.sentiment[0]
                score_blob.append(sentiment)
            
            return score_nltk, score_blob
            pass

if __name__ =="__main__":
    find_sent()