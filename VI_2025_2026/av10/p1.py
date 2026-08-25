import csv
from sklearn.neural_network import MLPClassifier

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
    'hidden_layer_sizes': (5,),  # 5 would work too
    'activation': 'relu',
    'solver': 'sgd',
    'batch_size': 'auto',
    'learning_rate': 'constant',
    'learning_rate_init': 1e-3,
    'max_iter': 500,
    'random_state': 0,
    # If using early stopping, target variable mustn't be a string
    # 'early_stopping': True,
    # 'validation_fraction': 0.1,
    # 'verbose': True
}

params_2 = params.copy()
params_2['hidden_layer_sizes'] = (10,)

params_3 = params.copy()
params_3['hidden_layer_sizes'] = (100,)


model_1 = MLPClassifier(**params)
model_2 = MLPClassifier(**params_2)
model_3 = MLPClassifier(**params_3)

model_1.fit(train_X, train_y)
model_2.fit(train_X, train_y)
model_3.fit(train_X, train_y)

names  = ['Nn with 5 neurons', 'Nn with 10 neurons', 'Nn with 100 neurons']
models = [model_1, model_2, model_3]
accs   = []

for model in models:
    acc = model.score(val_X, val_y)
    accs.append(acc)

best_model_idx = accs.index(max(accs))
best_model = models[best_model_idx]
best_model_name = names[best_model_idx]

print(f'The model -{best_model_name}- performed best with validation score {accs[best_model_idx]}')
print(f'The test accuracy for this model is {best_model.score(test_X, test_y)}')








