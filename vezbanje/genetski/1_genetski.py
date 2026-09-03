"""
Задача за вежба: Пожарникарски кули во шума

Шумата е претставена како грид со димензии M × N.
Секое поле има одредена вредност на дрвја (колку е важно да се заштити тоа поле).
Треба да поставиш најмногу K пожарникарски набљудувачки кули.
Секоја кула, ако е поставена на поле (x, y), гаси/штити само тоа поле и неговите 4 директни соседи (горе, долу, лево, десно — БЕЗ дијагонали).
Ако поле е покриено од повеќе кули, тоа сепак се брои само еднаш (не се дуплира вредноста).
Не мора да ги искористиш сите K кули.
Целта е да се максимизира вкупната заштитена вредност на шумата.

Од влез се читаат M, N, K, потоа матрицата на вредности (M реда по N броеви).
"""

import pygad

M, N = map(int, input().split())
K = int(input())

grid = []
for _ in range(M):
    grid.append(list(map(int, input().split())))


def decode(solution):
    # solution = [used, x, y, used, x, y, ...]  -> [(x1,y1), (x2,y2), ...] само за used == 1
    # TODO: напиши ја оваа функција (слична на онаа кај чадорите/прскалките)
    outlista = []
    for i in range(0, len(solution), 3):
        if solution[i] == 1:
            outlista.append((int(solution[i + 1]), int(solution[i + 2])))
    return outlista

def fitness_func(ga_instance, solution, solution_idx):
    kuli = decode(solution)
    # TODO:
    # 1. Направи празно множество "zastiteni" (х,y) координати
    # 2. За секоја кула, додади го нејзиното поле + 4-те директни соседи (внимавај на границите на гридот!)
    # 3. Собери ја вредноста од grid[x][y] за секое поле во "zastiteni" (без дуплирање)
    # 4. врати ја вкупната вредност
    zastiteni = []
    fitnessvalue = 0

    for kula in kuli:
        kx, ky = kula
        if kula not in zastiteni:
            zastiteni.append(kula)

        sosedi = []
        if kx + 1 < M:
            sosedi.append((kx+1, ky))
        if kx - 1 >= 0:
            sosedi.append((kx-1, ky))
        if ky + 1 < N:
            sosedi.append((kx, ky+1))
        if ky - 1 >= 0:
            sosedi.append((kx, ky-1))

        for sosed in sosedi:
            if sosed not in zastiteni:
                zastiteni.append(sosed)

    for value in zastiteni:
        i, j = value
        i = int(i)
        j = int(j)
        fitnessvalue += grid[i][j]

    return fitnessvalue

gene_space = []
for i in range(K):
    # TODO: додади gene_space за used (0/1), x (0 до M-1), y (0 до N-1)
    gene_space.append([0, 1])
    gene_space.append([i for i in range(0, M)])
    gene_space.append([i for i in range(0, N)])

    pass

params = {
    'num_generations': 200,
    'sol_per_pop': 100,
    'num_parents_mating': 40,
    'num_genes': K * 3,
    'gene_space': gene_space,
    'fitness_func': fitness_func,
    'mutation_num_genes': 1
}

ga = pygad.GA(**params)
ga.run()

best_solution, best_fitness, _ = ga.best_solution()
print(f"Najdobra zastitena vrednost: {best_fitness}")
print(f"Pozicii na kulite: {decode(best_solution)}")