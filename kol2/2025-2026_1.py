import pygad
import random
random.seed(0)

rooms = {
    1: {'name': 'Modern & Contemporary Art', 'adjacent': [2, 7], 'value': 110},
    2: {'name': 'European History', 'adjacent': [1, 3, 4, 5, 7], 'value': 130},
    3: {'name': 'Seasonal Exhibitions', 'adjacent': [2], 'value': 100},
    4: {'name': 'Prehistory', 'adjacent': [2, 6, 10], 'value': 140},
    5: {'name': 'Medieval Times', 'adjacent': [2, 6, 9], 'value': 120},
    6: {'name': 'Arms and Armor', 'adjacent': [4, 5], 'value': 150},
    7: {'name': 'Arts of Africa, Oceania and the Americas', 'adjacent': [1, 2, 8], 'value': 90},
    8: {'name': 'Greek and Roman History', 'adjacent': [7, 9], 'value': 180},
    9: {'name': 'The Great Hall', 'adjacent': [5, 8, 10], 'value': 30},
    10: {'name': 'Egyptian History', 'adjacent': [4, 9], 'value': 200}
}

K = int(input())

small_rooms = [1, 3, 4, 5, 6, 7]
big_rooms = [2, 8, 9, 10]


def fitness_func(ga, solution, idx):
    fitnessvalue = 0
    sumakameri = 0
    zastitenost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for _ in range(len(solution)):
        sumakameri+=1
    if sumakameri != K:
        fitnessvalue -= abs(sumakameri - K) * 1000

    for i in range(1, 11):
        room = rooms[i]
        name = room['name']
        neighbors = room['adjacent']
        value = room['value']
        postaveniKameri = solution[i - 1]
        if i in small_rooms:
            if postaveniKameri >= 1:
                zastitenost[i - 1] = 100
                for neighbor in neighbors:
                    zastitenost[neighbor - 1] = min(zastitenost[neighbor - 1] + postaveniKameri * 10, 100)
        if i in big_rooms:
            if postaveniKameri == 1:
                zastitenost[i - 1] = 60
            if postaveniKameri >= 2:
                zastitenost[i - 1] = 100
            for neighbor in neighbors:
                zastitenost[neighbor - 1] = min(zastitenost[neighbor - 1] + postaveniKameri * 10, 100)

    for i in range(10):
        zastitenostSoba = zastitenost[i]  # 80
        vrednostSoba = rooms[i + 1]['value']  # 120
        pridonetaVrednost = vrednostSoba * (zastitenostSoba / 100)
        fitnessvalue += pridonetaVrednost

    return fitnessvalue

gene_space = [i for i in range(K)]

params = {
    'num_generations': 1000,
    'sol_per_pop': 100,
    'num_parents_mating': 40,

    'num_genes': 10,
    'gene_space': gene_space,

    'fitness_func': fitness_func,

    'mutation_num_genes': 1,
    'random_state': 0
}

ga = pygad.GA(**params)

ga.run()

best_solution, _, _ = ga.best_solution()
best_fitness = fitness_func(None, best_solution, 0)

print(f'Optimal protected value: {best_fitness}M$')
