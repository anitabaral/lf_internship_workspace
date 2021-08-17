import itertools
from collections import Counter

import genism
import numpy as np

from .

class Embeddings:
    def __init__(self):
        pass

    def map_word_frequency(document):
        return Counter(itertools.chain(*document))

    def get_sif_feature_vectors(sentence1, sentence2, word_emb_model=model_w2v):
    sentence1 = [token for token in sentence1.split() if token in word_emb_model.wv.vocab]
    sentence2 = [token for token in sentence2.split() if token in word_emb_model.wv.vocab]
    word_counts = map_word_frequency((sentence1 + sentence2))
    embedding_size = 300
    a = 0.001
    sentence_embeddings=[]
    for sentence in [sentence1, sentence2]:
        vs = np.zeros(embedding_size)
        sentence_length = len(sentence)
        for word in sentence:
            a_value = a / (a + word_counts[word])
            vs = np.add(vs, np.multiply(a_value, word_emb_model.wv[word]))
        vs = np.divide(vs, sentence_length)
        sentence_embeddings.append(vs)

    return sentence_embeddings
