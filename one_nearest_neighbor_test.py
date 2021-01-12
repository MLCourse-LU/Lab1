# DO NOT CHANGE ANYTHING IN THIS FILE
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

from one_nearest_neighbor import OneNearestNeighborClassifier
from util import generate_data


np.random.seed(42)


def test_one_nearest_neighbor():
    X, y = generate_data()
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    clf = OneNearestNeighborClassifier()
    clf.fit(x_train, y_train)
    pred_test = clf.predict(x_test)
    score = accuracy_score(y_true=y_test, y_pred=pred_test)
    assert score > 0.9
