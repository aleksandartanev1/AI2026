import os
import numpy as np

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
# Vashiot kod tuka
    X = int(input())
    criteria = input()

    data = [row[:-1] for row in dataset]
    labels = [row[-1] for row in dataset]

    encoder = OrdinalEncoder()
    data = encoder.fit_transform(data)

    splitIndex = int(len(dataset)*(100-X)/100)
    train_X = data[splitIndex:]
    train_Y = labels[splitIndex:]

    test_X = data[:splitIndex]
    test_Y = labels[:splitIndex]

    classifier = DecisionTreeClassifier(criterion=criteria,
                                        random_state=0)

    classifier.fit(train_X, train_Y)

    y_prediction = classifier.predict(test_X)
    accurancy = accuracy_score(test_Y, y_prediction)

    depth = classifier.get_depth()
    leaves = classifier.get_n_leaves()

    importance = classifier.feature_importances_
    most_important = np.argmax(importance)
    least_important = np.argmin(importance)
    print(f"Depth: {depth}")
    print(f"Accuracy: {accurancy}")
    print(f"Number of leaves: {leaves}")
    print(f"Most important feature: {most_important}")
    print(f"Least important feature: {least_important}")


    submit_train_data(train_X,train_Y)
    submit_test_data(test_X,test_Y)
    submit_classifier(classifier)
    submit_encoder(encoder)