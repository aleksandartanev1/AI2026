import pygad

N = int(input())
S, E = map(int, input().split())

dist = [list(map(float, input().split())) for _ in range(N)]

cities = [i for i in range(N) if i != S and i != E]
M = len(cities)

def route_cost(route):
    cost = 0
    for i in range(len(route)-1):
        cost += dist[route[i]][route[i+1]]
    return cost


def decode(solution):
    r1 = [S]
    r2 = [S]

    for i in range(M):
        if solution[i] == 0.0:
            r1.append(cities[i])
        else:
            r2.append(cities[i])

    r1.append(E)
    r2.append(E)

    return r1, r2


def fitness_func(ga, solution, idx):
    r1, r2 = decode(solution)

    t1 = route_cost(r1)
    t2 = route_cost(r2)

    penalty = max(t1, t2)

    if min(t1, t2) > 0 and max(t1, t2) > 2 * min(t1, t2):
        penalty += 1000

    penalty += abs(len(r1) - len(r2)) * 10

    return -penalty


gene_space = [[0, 1] for _ in range(M)]


params = {
    'num_generations': 500,
    'sol_per_pop': 100,
    'num_parents_mating': 50,

    'num_genes': M,
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

route1, route2 = decode(solution)

print("Friend 1 route:", route1)
print("Friend 2 route:", route2)
print("Fitness:", fitness)

submit_data(fitness_func, decode, best_solutions)