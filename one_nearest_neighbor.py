from model import AbstractModel


class OneNearestNeighborClassifier(AbstractModel):
    def fit(self, x_train, y_train):
        raise NotImplementedError('Please implement')

    def predict(self, x_test):
        raise NotImplementedError('Please implement')
