""" Majority classifier """
import numpy as np
from model import AbstractModel


class MajorityClassifier(AbstractModel):
    """ Majority classifier: classifies everything with the majority label from the training set. """
    def __init__(self):
        super().__init__()
        self.majority_label = None

    def fit(self, x_train, y_train):
        """ Determine which is the majority label in the training set. """
        majority = 0
        majority_label = None
        for label in np.unique(y_train):
            if np.sum(y_train[y_train == label]) > majority:
                majority = np.sum(y_train[y_train == label])
                majority_label = label
        self.majority_label = majority_label

    def predict(self, x_test):
        """ Predict the trained majority label in all cases. """
        return np.full(x_test.shape[0], self.majority_label)
