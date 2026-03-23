from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf_features(text_data):
    vectorizer = TfidfVectorizer(max_features=10000)
    X = vectorizer.fit_transform(text_data)
    return X, vectorizer