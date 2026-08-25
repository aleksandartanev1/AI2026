import csv
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

def read_file(path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')

        lines = list(csv_reader)[1:]

    lines = [list(map(float, line[:-1])) + [line[-1]] for line in lines]

    return lines


dataset = read_file('data/winequality.csv')

dataset_bad = [row for row in dataset if row[-1] == 'bad']
split_train_idx = int(0.7 * len(dataset_bad))
split_val_idx  =  int(0.8 * len(dataset_bad))
train_set_bad = dataset_bad[:split_train_idx]
val_set_bad   = dataset_bad[split_train_idx:split_val_idx]
test_set_bad  = dataset_bad[split_val_idx:]
del split_train_idx, split_val_idx

dataset_good = [row for row in dataset if row[-1] == 'good']
split_train_idx = int(0.7 * len(dataset_good))
split_val_idx  =  int(0.8 * len(dataset_good))
train_set_good = dataset_good[:split_train_idx]
val_set_good   = dataset_good[split_train_idx:split_val_idx]
test_set_good  = dataset_good[split_val_idx:]

train_set = train_set_bad + train_set_good
val_set   = val_set_bad + val_set_good
test_set  = test_set_bad + test_set_good

train_X, train_y = [row[:-1] for row in train_set], [row[-1] for row in train_set]
val_X, val_y = [row[:-1] for row in val_set], [row[-1] for row in val_set]
test_X, test_y = [row[:-1] for row in test_set], [row[-1] for row in test_set]

params = {
    'hidden_layer_sizes': (100,),
    'activation': 'relu',
    'solver': 'sgd',
    'batch_size': 'auto',
    'learning_rate': 'constant',
    'learning_rate_init': 1e-3,
    'max_iter': 500,
    'random_state': 0,
    # 'early_stopping': True,
    # 'validation_fraction': 0.1,
    # 'verbose': True
}

model_1 = MLPClassifier(**params)
model_2 = MLPClassifier(**params)
model_3 = MLPClassifier(**params)


model_1.fit(train_X, train_y)

standard_scaler = StandardScaler()
model_2.fit(standard_scaler.fit_transform(train_X), train_y)

minmax_scaler = MinMaxScaler(feature_range=(-1, 1))
model_3.fit(minmax_scaler.fit_transform(train_X), train_y)

models_and_sets = [(model_1, val_X), (model_2, standard_scaler.transform(val_X)), (model_3, minmax_scaler.transform(val_X))]
accs = []

for i, (model, set) in enumerate(models_and_sets):
    acc = model.score(set, val_y)
    accs.append(acc)

best_model_idx = accs.index(max(accs))
best_model = models_and_sets[best_model_idx][0]

# print(best_model_idx, best_model)

test_scaled_sets = [test_X, standard_scaler.transform(test_X), minmax_scaler.transform(test_X)]
preds = best_model.predict(test_scaled_sets[best_model_idx])

# Accuracy is a symmetric metric, doesn't matter in which order you provide params
print('Accuracy:', accuracy_score(test_y, preds))

# Precision and recall are NOT symmetric:
#   - You must provide test_y first, then preds second
#   - (Optional) If target contains strings, you must provide which label is positive via 'pos_label' param
print('Precision:', precision_score(test_y, preds, pos_label='good'))
print('Recall:', recall_score(test_y, preds, pos_label='good'))


# Manual calculation of accuracy, precision and recall

# TP, TN, FP, FN = [0] * 4
# for pred, gt_label in zip(preds, test_y):
#     if pred == 'good' and pred == gt_label:
#         TP += 1
#     elif pred == 'good' and pred != gt_label:
#         FP += 1
#     elif pred == 'bad' and pred == gt_label:
#         TN += 1
#     else:
#         FN += 1
#
# accuracy = (TP + TN) / (TP + TN + FP + FN)
# precision = TP / (TP + FP) if (TP + FP) != 0 else 0
# recall = TP / (TP + FN) if (TP + FN) != 0 else 0
#
# print(accuracy, precision, recall)






