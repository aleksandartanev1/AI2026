import os
import warnings



warnings.filterwarnings("ignore")

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from dataset_script_anomaly import dataset


if __name__ == '__main__':
    classifier = MLPClassifier(hidden_layer_sizes=(50,), activation="relu", learning_rate_init=0.001, random_state=0, max_iter=25)
    X = [row[:-1] for row in dataset]
    Y = [1 if row[-1] > 50 else 0 for row in dataset]

    split = len(dataset) * 70 // 100

    train_x = X[:split]
    train_y = Y[:split]

    test_x = X[split:]
    test_y = Y[split:]

    co2 = float(input()) #3
    no2 = float(input()) #4
    so2 = float(input()) #5

    #original classifier
    originalclassifier = classifier
    originalclassifier.fit(train_x, train_y)
    originalscore = originalclassifier.score(test_x, test_y)


    #anomaly classifier
    removedanomalyclassifier = classifier
    train_x_anomaly = [[co2 if i == 3 and val > co2 else
                        no2 if i == 4 and val > no2 else
                        so2 if i == 5 and val > so2 else val for i, val in enumerate(row)] for row in train_x]
    removedanomalyclassifier.fit(train_x_anomaly, train_y)

    test_x_anomaly = [[co2 if i == 3 and val > co2 else
                       no2 if i == 4 and val > no2 else
                       so2 if i == 5 and val > so2 else val for i, val in enumerate(row)] for row in test_x]

    removedanomalyscore = removedanomalyclassifier.score(test_x_anomaly, test_y)


    #scaled
    scaler = StandardScaler()
    train_x_scaled = scaler.fit_transform(train_x)
    test_x_scaled = scaler.transform(test_x)
    scaledclassifier = classifier
    scaledclassifier.fit(train_x_scaled, train_y)
    scaledscore = scaledclassifier.score(test_x_scaled, test_y)

    #scaled and anomaly
    scaler.fit(train_x_anomaly)
    train_x_anomaly_scaled = scaler.transform(train_x_anomaly)
    test_x_anomaly_scaled = scaler.transform(test_x_anomaly)
    scaledanomalyclassifier = classifier
    scaledanomalyclassifier.fit(train_x_anomaly_scaled, train_y)
    scaledanomalyscore = scaledanomalyclassifier.score(test_x_anomaly_scaled, test_y)



    print(f"Accuracy with:")
    print(f"The original dataset: {originalscore}")
    print(f"Removed anomalies: {removedanomalyscore}")
    print(f"Scaled attributes: {scaledscore}")
    print(f"Removed anomalies and scaled attributes: {scaledanomalyscore}")