import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

from sklearn.naive_bayes import GaussianNB

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
# Vashiot kod tuka

    record = list(map(float, input().split()))

    class_0 = [row for row in dataset if row[-1] == '0']
    class_1 = [row for row in dataset if row[-1] == '1']

    split_0 = int(len(class_0) * 0.85)
    split_1 = int(len(class_1) * 0.85)

    train = class_0[:split_0] + class_1[:split_1]
    test = class_0[split_0:] + class_1[split_1:]

    train_x = [[float(x) for x in row[:-1]] for row in train]
    train_y = [int(row[-1]) for row in train]

    test_x = [[float(x) for x in row[:-1]] for row in test]
    test_y = [int(row[-1]) for row in test]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    accuracy = classifier.score(test_x, test_y)
    pred = classifier.predict([record])
    probability = classifier.predict_proba([record])

    print(accuracy)
    print(pred[0])
    print(probability)

    submit_train_data(train_x, train_y)
    submit_test_data(test_x, test_y)
    submit_classifier(classifier)


# povtoren import na kraj / ne ja otstranuvajte ovaa linija
