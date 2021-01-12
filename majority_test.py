"""Unit tests for the majority classifier. Do not change anything in this file!"""
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

from majority import MajorityClassifier
from util import generate_data


np.random.seed(42)


def test_majority():
    """ Test the majority classifier"""
    x, y = generate_data()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    clf = MajorityClassifier()
    assert clf.majority_label is None
    clf.fit(x_train, y_train)
    assert clf.majority_label is not None
    pred_test = clf.predict(x_test)
    score = accuracy_score(y_true=y_test, y_pred=pred_test)
    assert score > 0.5
