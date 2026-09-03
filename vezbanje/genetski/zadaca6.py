"""
Во оваа задача, треба да користиш Генетски алгоритам за да ги оптимизираш параметрите на DecisionTreeClassifier.
Во даденото податочно множество, класата се наоѓа на последната позиција во секој ред.
Податочното множество треба да се подели на тренирачко и тестирачко подмножества така што:
    - првите 75% од податоците ќе бидат за тренирање
    - останатите 25% ќе бидат за тестирање
Генетскиот алгоритам треба да ги оптимизира следните параметри со нивните соодветни можни вредности:
    1. criterion: 'gini', 'entropy'
    2. max_depth: 5, 10, 15, 20, 25
    3. min_samples_split: 2, 3, 4, 5, 10
    4. max_leaf_nodes: 5, 10, 15, 20, 25
Fitness функцијата треба да ја максимизира точноста на класификацијата на тестирачкото множество. Сепак, кога два
модели постигнуваат слична точност, треба да се преферираат помали дрва. Поради тоа, fitness функцијата треба малку
да ги казнува поголемите вредности на max_depth и max_leaf_nodes. Пополнете ги деловите што недостасуваат во почетниот
код. Откако ќе заврши Генетскиот алгоритам:
    1. Извлечете го најдоброто решение.
    2. Испечатете ги најдобрите параметри за decision tree.
Потоа:
    1. Креирајте го најдобриот модел на decision tree.
    2. Истренирајте го моделот.
    3. Испечатете ја неговата конечна точност на тестирачкото множество.
"""
import pygad
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

dataset = [
    [2, 3, 1, 7, 0],
    [5, 6, 4, 3, 1],
    [1, 1, 2, 8, 1],
    [7, 8, 6, 4, 1],
    [3, 2, 1, 9, 0],
    [8, 7, 5, 2, 1],
    [4, 5, 2, 6, 1],
    [1, 3, 1, 9, 0],
    [9, 8, 7, 2, 1],
    [2, 2, 3, 8, 0],
    [6, 5, 4, 3, 1],
    [1, 0, 2, 9, 0],
    [7, 7, 6, 5, 1],
    [2, 1, 1, 8, 0],
    [8, 9, 5, 3, 1],
    [3, 4, 2, 7, 0],
    [5, 5, 5, 4, 0],
    [0, 1, 1, 9, 0],
    [9, 9, 8, 1, 1],
    [2, 3, 2, 7, 0],
    [6, 7, 5, 3, 1],
    [1, 2, 0, 8, 0],
    [8, 6, 7, 2, 0],
    [3, 1, 2, 9, 0],
    [7, 5, 6, 4, 1],
    [2, 0, 1, 8, 0],
    [9, 7, 8, 2, 1],
    [4, 3, 2, 7, 0],
    [6, 6, 5, 4, 1],
    [1, 1, 0, 9, 0],
    [8, 8, 6, 3, 1],
    [2, 2, 1, 8, 0],
    [7, 9, 5, 2, 1],
    [3, 2, 2, 7, 0],
    [5, 7, 4, 3, 1],
    [0, 1, 2, 9, 0],
    [9, 8, 6, 2, 0],
    [2, 3, 1, 8, 0],
    [6, 5, 5, 4, 1],
    [1, 0, 1, 9, 0],
    [8, 7, 7, 2, 1],
    [3, 1, 1, 8, 0],
    [7, 6, 5, 3, 0],
    [2, 2, 0, 9, 0],
    [9, 9, 7, 1, 1],
    [4, 2, 2, 7, 0],
    [6, 8, 5, 2, 1],
    [1, 1, 1, 8, 1],
    [8, 6, 6, 3, 1],
    [2, 0, 2, 9, 1],
    [7, 7, 5, 4, 1],
    [3, 2, 1, 8, 0],
    [9, 8, 8, 2, 1],
    [1, 0, 0, 9, 0],
    [6, 6, 4, 3, 1],
    [2, 1, 2, 8, 0],
    [8, 9, 6, 2, 1],
    [4, 3, 1, 7, 0],
    [7, 5, 5, 4, 1],
    [1, 2, 1, 9, 0],
    [9, 7, 6, 1, 1],
    [2, 2, 2, 8, 0],
    [6, 8, 7, 3, 1],
    [0, 1, 1, 8, 0],
    [8, 8, 5, 2, 1],
    [3, 2, 0, 9, 0],
    [7, 6, 6, 4, 1],
    [1, 1, 2, 8, 0],
    [9, 9, 5, 1, 1],
    [2, 3, 0, 9, 0],
    [6, 7, 6, 3, 1],
    [1, 0, 1, 8, 0],
    [8, 7, 5, 3, 1],
    [3, 1, 0, 9, 0],
    [7, 8, 7, 2, 1],
    [2, 2, 1, 9, 0],
    [9, 6, 8, 1, 1],
    [4, 2, 1, 8, 0],
    [6, 5, 6, 4, 1],
    [1, 1, 0, 8, 0]
]

train_set = [dataset[i] for i in range(0, int(0.75 * len(dataset)))]
train_set_x = [train_set[i][0:-1] for i in range(0, len(train_set))]
train_set_y = [train_set[i][-1] for i in range(0, len(train_set))]

test_set = [dataset[i] for i in range(int(0.75 * len(dataset)), len(dataset))]
test_set_x = [test_set[i][0:-1] for i in range(0, len(test_set))]
test_set_y = [test_set[i][-1] for i in range(0, len(test_set))]


def pomosnaFunkcijaZaPecatenje(solution):
    criterionS = " "
    if solution[0] == 0:
        criterionS = "gini"
    else:
        criterionS = "entropy"

    max_depthS = int(solution[1])
    min_samples_splitS = int(solution[2])
    max_leaf_nodesS = int(solution[3])

    return criterionS, max_depthS, min_samples_splitS, max_leaf_nodesS


def fitness_func(ga_instance, solution, solution_idx):
    # solution = [1, 5, 4, 15]  -> 0 == gini;  1 == entropy
    fitnessValue = 0
    criterionS = " "
    if solution[0] == 0:
        criterionS = "gini"
    else:
        criterionS = "entropy"

    max_depthS = int(solution[1])
    min_samples_splitS = int(solution[2])
    max_leaf_nodesS = int(solution[3])
    clf = DecisionTreeClassifier(criterion=criterionS, max_depth=max_depthS, min_samples_split=min_samples_splitS,
                                 max_leaf_nodes=max_leaf_nodesS, random_state=0)
    clf.fit(train_set_x, train_set_y)
    accuracy = accuracy_score(test_set_y, clf.predict(test_set_x))

    fitnessValue = accuracy - max_depthS * 0.001 - max_leaf_nodesS * 0.001
    return fitnessValue


gene_space = []
gene_space.append([0, 1])
gene_space.append([5, 10, 15, 20, 25])
gene_space.append([2, 3, 4, 5, 10])
gene_space.append([5, 10, 15, 20, 25])

ga_instance = pygad.GA(
    num_generations=40,
    sol_per_pop=50,
    num_parents_mating=25,
    fitness_func=fitness_func,
    num_genes=4,
    gene_space=gene_space,
    mutation_num_genes=1
)

ga_instance.run()
best_solution, _, _ = ga_instance.best_solution()

criterion, max_depth, min_sample_split, max_leaf_nodes = pomosnaFunkcijaZaPecatenje(best_solution)
print(f'Najdobrite parametri za decision tree se: ')
print(f'    Kriterium za izbor na najdobar atribut: {criterion}')
print(f'    Maksimalna dlabocina na drvoto: {max_depth}')
print(f'    Minimalna podelba na primerokot: {min_sample_split}')
print(f'    Maksimalen broj na listovi: {max_leaf_nodes}')

clf_best = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth, min_samples_split=min_sample_split,
                                  max_leaf_nodes=max_leaf_nodes, random_state=0)
clf_best.fit(train_set_x, train_set_y)
accuracy_best = accuracy_score(test_set_y, clf_best.predict(test_set_x))
print(f'Konecnata tocnost na klasfikatorot so najdobrite parametri: {accuracy_best}')