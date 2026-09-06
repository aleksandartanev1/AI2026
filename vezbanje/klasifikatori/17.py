import os



os.environ['OPENBLAS_NUM_THREADS'] = '1'
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler


if __name__ == '__main__':
    C = int(input())
    P = int(input())


    X_unmodified = [row[:-1] for row in dataset]
    Y = [row[-1] for row in dataset]
    X_modified = [[row[0] + row[-1]] + row[1:-1] for row in X_unmodified]

    newdataset = [f + [l] for f, l in zip(X_modified, Y)]

    goodclass = [row for row in newdataset if row[-1] == "good"]
    badclass = [row for row in newdataset if row [-1] == "bad"]



    if C == 0:
        goodsplit = len(goodclass) * P // 100
        badsplit = len(badclass) * P // 100
        good_train = goodclass[:goodsplit]
        good_test = goodclass[goodsplit:]
        bad_train = badclass[:badsplit]
        bad_test = badclass[badsplit:]
    elif C == 1:
        goodsplit = len(goodclass) * (100 - P) // 100
        badsplit = len(badclass) * (100 - P) // 100
        good_train = goodclass[goodsplit:]
        good_test = goodclass[:goodsplit]
        bad_train = badclass[badsplit:]
        bad_test = badclass[:badsplit]

    traindata = good_train + bad_train
    testdata = good_test + bad_test

    X_train = [row[:-1] for row in traindata]
    Y_train = [row[-1] for row in traindata]
    X_test = [row[:-1] for row in testdata]
    Y_test = [row[-1] for row in testdata]


    #unscaled
    unscaledclassifier = GaussianNB()
    unscaledclassifier.fit(X_train, Y_train)
    unscaledscore = unscaledclassifier.score(X_test, Y_test)


    #scaled

    scaler = MinMaxScaler(feature_range=(-1, 1))
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    scaledclassifier = GaussianNB()
    scaledclassifier.fit(X_train_scaled, Y_train)
    scaledscore = scaledclassifier.score(X_test_scaled, Y_test)




    print(f"Tochnost so zbir na koloni: {unscaledscore}")
    print(f"Tochnost so zbir na koloni i skaliranje: {scaledscore}")