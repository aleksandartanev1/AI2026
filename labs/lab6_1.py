import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka

    percentage = int(input())
    record = input().split()

    split_index=int(len(dataset) * percentage / 100)
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_x, train_Y)
    train=dataset[:split_index]
    test=dataset[split_index:]

    train_x=[row[:-1] for row in train]
    train_y=[row[-1] for row in train]



    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)
    test_x=[row[:-1] for row in test]
    test_y=[row[-1] for row in test]
    encoder=OrdinalEncoder()
    train_x_enc=encoder.fit_transform(train_x)
    test_x_enc=encoder.transform(test_x)
    record_enc=encoder.transform([record])

    # submit na klasifikatorot
    # submit_classifier(classifier)
    classifier=CategoricalNB()
    classifier.fit(train_x_enc, train_y)

    accuracy = classifier.score(test_x_enc, test_y)
    pred = classifier.predict(record_enc)
    probability = classifier.predict_proba(record_enc)

    print(accuracy)
    print(pred[0])
    print(probability)


    # submit na encoderot
    # submit_encoder(encoder)
    submit_train_data(train_x_enc, train_y)
    submit_test_data(test_x_enc, test_y)
    submit_classifier(classifier)
    submit_encoder(encoder)
