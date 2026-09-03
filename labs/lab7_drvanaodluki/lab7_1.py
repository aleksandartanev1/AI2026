import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':


    col_index = int(input())
    n_estimators = int(input())
    criterion = input().strip()
    new_sample = list(map(float, input().split()))

    data = [row for row in dataset]
    x = [row[:-1] for row in data]
    y = [row[-1] for row in data]

    x = [row[:col_index] + row[col_index + 1:] for row in x]
    new_sample = new_sample[:col_index] + new_sample[col_index+1:]

    split_index = int(len(data) * 0.85)
    train_X = x[:split_index]
    train_Y = y[:split_index]
    test_X = x[split_index:]
    test_Y = y[split_index:]

    classifier = RandomForestClassifier(n_estimators=n_estimators, criterion=criterion, random_state=0)
    classifier.fit(train_X, train_Y)

    prediction = classifier.predict(test_X)
    accuracy = accuracy_score(test_Y, prediction)

    predicted_class = classifier.predict([new_sample])[0]
    probability = classifier.predict_proba([new_sample])[0]

    print(f"Accuracy: {accuracy}")
    print(predicted_class)
    print(probability)

    submit_train_data(train_X, train_Y)
    submit_test_data(test_X, test_Y)
    submit_classifier(classifier)