from model import AbstractModel


class MajorityClassifier(AbstractModel):
    def fit(self, x_train, y_train):
        raise NotImplementedError  # TODO Lau

    def predict(self, x_test):
        raise NotImplementedError  # TODO Lau
