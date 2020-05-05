import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
import pickle


df = pd.read_csv('Data/emails.csv')
svc = pickle.load(open('Model/finalized_model.sav', 'rb'))



class TextClean(BaseEstimator, TransformerMixin):

    def fit(self, x, y=None):
        return self

    def transform(self, x, y=None):
        x['text'] = x['text'].apply(lambda x: re.sub('[0-9]+', 'Number', x))
        x['text'] = x['text'].apply(lambda x: re.sub('http : / /[\w\W]+. com /', 'URL', x))
        x['text'] = x['text'].apply(lambda x: re.sub(r'[.,;$%&*@!#-=?"]', '', x))
        x['text'] = x['text'].apply(lambda x: re.sub(r'Subject', '', x))
        x['text'] = x['text'].apply(lambda x: x.lower())

        return x


class TextVectorization(BaseEstimator, TransformerMixin):

    def __init__(self, vect):
        self.vectorizer = vect

    def fit(self, x, y=None):
        return self

    def transform(self, x, y=None):
        self.vectorizer.fit(df['text'])
        X = self.vectorizer.transform(x['text'])
        return X

vectorizer = TfidfVectorizer(stop_words='english')


pipeline = Pipeline([('TextClean',TextClean()),
                     ('TextVectorization', TextVectorization(vectorizer))])


def PredictEmail(text):
    aux = pd.DataFrame([text], columns=['text'])
    X = pipeline.fit_transform(df)

    processed = pipeline.transform(aux)

    pred = svc.predict(processed)
    perc = svc.predict_proba(processed)
    return(pred, perc)


