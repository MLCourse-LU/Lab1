""" Make plots to compare the classifiers. """
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from majority import MajorityClassifier
from one_nearest_neighbor import OneNearestNeighborClassifier
from util import generate_data

X, y = generate_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

true_markers = {1: '+', -1: 'o'}
predicted_colors = {1: 'blue', -1: 'red'}

# Show the ground truth of the datasets
for label in [1, -1]:
    points = X_train[y_train == label, :]
    plt.scatter(points[:, 0], points[:, 1], marker=true_markers[label], label=f'{label} train', color='black')
    points = X_test[y_test == label, :]
    plt.scatter(points[:, 0], points[:, 1], marker=true_markers[label], label=f'{label} test', color='magenta')
plt.legend()
plt.title('Ground truth')
plt.show()


def show_performance(features, true_labels, predicted_labels, classifier_name):
    """ Plot performance of one classifier & show accuracy """
    for index, predicted_label in enumerate(predicted_labels):
        plt.scatter(
                features[index, 0], features[index, 1],  # X/Y coordinates
                marker=true_markers[true_labels[index]], color=predicted_colors[predicted_label],  # shape and color
                label=f'True: {true_labels[index]} / Predicted: {predicted_label}'  # legend
        )
    # Trick to avoid duplicate legend entries in scatter plots,
    # see https://stackoverflow.com/questions/13588920/stop-matplotlib-repeating-labels-in-legend/13589144#answer-13589144
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.title(f'{classifier_name} (accuracy = {accuracy_score(y_true=true_labels, y_pred=predicted_labels)})')
    plt.show()


# Theoretical perfect classification
show_performance(X_test, y_test, y_test, "Theoretical Perfect Classification")


# Evaluate the majority classifier
clf = MajorityClassifier()
clf.fit(x_train=X_train, y_train=y_train)
predicted = clf.predict(x_test=X_test)
show_performance(X_test, y_test, predicted, "Majority Classifier")
