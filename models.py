from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

def get_models():
    return {
        "logistic": LogisticRegression(max_iter=1000),
        "svm": SVC()
    }