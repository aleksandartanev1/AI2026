## Task 1 - Wine Quality Classification with a Neural Network

Create a neural network model for wine quality classification. The dataset is provided in the file `data/winequality.csv`. Each instance is represented by 11 chemical features and one class label indicating good (`'good'`) or bad (`'bad'`) wine quality.

The dataset should be divided into training, validation, and testing sets such that the first 70% (in the order they appear in the dataset) of each class are assigned to the training set. The next 10% of each class should be assigned to the validation set, while the remaining 20% should be part of the testing set.

Using the validation set, select the best number of neurons in the hidden layer from the following options: `[5, 10, 100]`. The model with the highest validation accuracy should be used as the final model. The models should be trained using a learning rate of `0.001`, `500` epochs, and the ReLU activation function for the neurons in the hidden layer.

The final model should be evaluated using the testing set, and the model accuracy should be calculated.

---

## Task 2 - Feature Scaling

Investigate how feature scaling contributes to improving the model from the previous task.

Use the same dataset split from the previous task and create the model that performed best previously. The model should be trained using:

* the original data,
* data scaled with `StandardScaler`,
* and data scaled with `MinMaxScaler`.

Using the validation set, determine which technique provides the best representation of the data. Then evaluate the model on the testing set by calculating the accuracy, precision, and recall.

Accuracy:

$$\text{Accuracy} = \frac{TP + TN}{TP + FP + TN + FN}$$

Precision:

$$\text{Precision} = \frac{TP}{TP + FP}$$

Recall:

$$\text{Recall} = \frac{TP}{TP + FN}$$

* `TP` — number of correctly predicted positive classes
* `FP` — number of incorrectly predicted positive classes
* `TN` — number of correctly predicted negative classes
* `FN` — number of incorrectly predicted negative classes
