class AbstractModel:
    def __init__(self):
        pass

    def fit(self, x_train, y_train):
        raise NotImplementedError('Please subclass')

    def predict(self, x_test):
        raise NotImplementedError('Please subclass')