import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    col_to_remove = int(input())
    num_neurons = int(input())

    modifieddata = [row[:col_to_remove] + row[col_to_remove + 1:] for row in dataset]

    x = [list(map(float, row[:-1])) for row in modifieddata]
    y = [row[-1] for row in modifieddata]

    train_x, test_x, train_y, test_y = train_test_split(x, y, train_size=0.8, shuffle=False)

    classifier = MLPClassifier((num_neurons,), max_iter=500, random_state=0)
    classifier.fit(train_x, train_y)

    pred_y = classifier.predict(test_x)
    accuracy = accuracy_score(test_y, pred_y)
    new_sample = list(map(float, input().split(' ')))
    new_sample = new_sample[:col_to_remove] if len(new_sample) - 1 == col_to_remove else new_sample[:col_to_remove] + new_sample[col_to_remove + 1:]
    new_sample_pred = classifier.predict([new_sample])[0]


    print(f'Tochnost: {accuracy}')
    print(f'Predvidena klasa: {new_sample_pred}')
    print(f'Verojatnosti: {classifier.predict_proba([new_sample])[0]}')

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_x, train_y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_x, test_y)

    # submit na klasifikatorot
    submit_classifier(classifier)
