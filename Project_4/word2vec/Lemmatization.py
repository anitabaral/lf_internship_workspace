from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

class Lemmatization:
    def __init__(self):
        pass

    def lemmatize_corpus(self, corpus):
        lemmatizer = WordNetLemmatizer()
        tokenized_corpus = word_tokenize(corpus)
        lemmatized_corpus = " ".join([lemmatizer.lemmatize(word) for word in tokenized_corpus])

        return lemmatized_corpus
