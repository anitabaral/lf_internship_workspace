
import string

import nltk
from nltk import word_tokenize
from unidecode import unidecode
from nltk.corpus import stopwords


class Preprocessing:
    def __init__(self):
        pass

    def remove_stopwords(self, corpus):
        corpus = corpus.lower()
        stopset = stopwords.words('english') + list(string.punctuation)
        corpus_without_stopword = " ".join([i for i in word_tokenize(corpus) if i not in stopset])

        return corpus_without_stopword

    def remove_nonascii(self, corpus):
        corpus_without_non_ascii_characters = unidecode(corpus)

        return corpus_without_non_ascii_characters
