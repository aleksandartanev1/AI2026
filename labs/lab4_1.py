import pygad
import math

N, M, R = map(float, input().split())
N = int(N)
M = int(M)
points = [tuple(map(float, input().split())) for _ in range(N)]


def decode(solution):
    umbrellas = []
    for i in range(0, len(solution), 2):
        x = solution[i]
        y = solution[i + 1]
        if 0 <= x <= 10 and 0 <= y <= 10:
            umbrellas.append((x, y))
    return umbrellas


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def fitness_func(ga, solution, idx):
    umbrellas = decode(solution)
    penalty = 0

    for p in points:
        covered = any(distance(p, u) <= R for u in umbrellas)
        if not covered:
            penalty += 10000

    for i in range(len(umbrellas)):
        for j in range(i + 1, len(umbrellas)):
            d = distance(umbrellas[i], umbrellas[j])
            if d < 8 * R / 5:
                penalty += 1000
            elif d < 2 * R:
                penalty += 100

    penalty += len(umbrellas) * 1

    return -penalty


gene_space = [{'low': 0, 'high': 10} for _ in range(2 * M)]

params = {
    'num_generations': 500,
    'sol_per_pop': 100,
    'num_parents_mating': 50,
    'num_genes': 2 * M,
    'gene_space': gene_space,
    'fitness_func': fitness_func,
    'mutation_num_genes': 1,
    'save_best_solutions': True
}

ga = pygad.GA(**params)
ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)
best_solutions = ga.best_solutions

print(solution)
print(fitness)

chromosomes = [
    [9, 9, 9, 9, 9, 9],
    [1, 1, 1.1, 1, 9, 9],
    [1, 1, 1.1, 1, 5, 5],
    [1, 1, 1.9, 1, 5, 5],
    [1, 1, 5, 5, 9, 9],
]
"""

chromosomes = [
    #tochkite se (1,1) (1.1, 1) (5,5)
    [9, 9, 9, 9, 9, 9], #site cadori na isto mesto ogromno preklopuvanje, nishto ne se pokriva
    [1, 1, 1.1, 1, 9, 9], #dve cadori pokrieni, (5,5) ne pokrien
    [1, 1, 1.1, 1, 5, 5], #eden cador pokriva (1,1) i (1.1, 1), drug go pokriva (5,5), ama ima poklopuvanje
    [1, 1, 2, 1, 5, 5], #slichno na prethodno no pomalo preklopuvanje
    [1, 1, 5, 5, 9, 9], #optimalno 
]
"""



submit_data(fitness_func, decode, chromosomes, best_solutions)