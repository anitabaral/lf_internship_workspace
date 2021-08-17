from sklearn.metrics.pairwise import cosine_similarity

class SimilarityScore:
    def __init__(self):
        pass

    def get_cosine_similarity(self, feature_vectors):
        return cosine_similarity(feature_vectors[0].reshape(1, -1), feature_vectors[1].reshape(1, -1))[0][0]
