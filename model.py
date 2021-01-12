""" Abstract model class """


class AbstractModel:
    """ Abstract class for ML models - please subclass"""
    def __init__(self):
        pass

    def fit(self, x_train, y_train):
        """ Fit a model """
        raise NotImplementedError('Abstract method; please subclass')

    def predict(self, x_test):
        """ Make predictions """
        raise NotImplementedError('Abstract method; please subclass')
