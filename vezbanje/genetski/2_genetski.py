"""
Задача за вежба: Распределба на пратки по комбиња

Логистичка компанија има N пратки за испорака и K комбиња на располагање.
Секоја пратка i има тежина w_i (во кг).
Секое комби има максимален капацитет C кг (ист за сите комбиња).

Правила:

Секоја пратка мора да се додели на точно едно комби (секоја пратка мора да се испорача).
Едно комби може да носи 0, 1 или повеќе пратки, но вкупната тежина на пратките доделени на тоа комби не смее да го надмине капацитетот C.
Ако го надмине — невалидно решение.
Времето за истовар на едно комби се пресметува како: vreme = FIKSNO_VREME + BROJ_PRATKI_VO_KOMBI * VREME_PO_PRATKA (константите FIKSNO_VREME=5 и VREME_PO_PRATKA=2 се фиксни во кодот).
Бидејќи комбијата патуваат паралелно, целта е да се минимизира максималното време на истовар меѓу сите комбиња (класичен "makespan" проблем).
Ако две решенија имаат исто максимално време, преферирај го она што користи помалку активни комбиња (комбиња со барем 1 пратка) — помал број активни комбиња значи поефикасна логистика.

Од влез: N K C, потоа N броеви (тежините на пратките).
"""
import pygad

N, K, C = map(int, input().split())
weights = list(map(int, input().split()))

FIKSNO_VREME = 5
VREME_PO_PRATKA = 2


def decode(solution):
    # solution = [k0, k1, k2, ..., kN-1]  каде ki е бројот на комбито (0..K-1) доделено на пратка i
    listaKombina = [[] for _ in range(K)]   # K празни листи, по една за секое комби
    for i in range(N):                       # оди низ секоја пратка
        j = int(solution[i])                 # во кое комби оди пратка i
        listaKombina[j].append(int(weights[i]))   # додади ЈА ТЕЖИНАТА на пратка i во листата на комби j
    return listaKombina

def fitness_func(ga_instance, solution, solution_idx):
    listaKombina = decode(solution)
    # TODO:
    # 1. За секое комби, пресметај ја вкупната тежина. Ако > C -> голема казна.
    # 2. За секое комби со >=1 пратка, пресметај vreme = FIKSNO_VREME + broj_pratki * VREME_PO_PRATKA
    # 3. Најди го МАКСИМАЛНОТО време меѓу сите активни комбиња (тоа е главната цел за минимизирање)
    # 4. Изброј колку комбиња се активни (>=1 пратка) - тоа е tie-breaker (помалку = подобро)
    # 5. Врати fitness (внимавај на знакот - минимизираме!)
    fitnessvalue = 0
    for kombe in listaKombina:
        totalweight = 0
        for weight in kombe:
            totalweight += weight
        if totalweight > C:
            fitnessvalue -= 10000 * (totalweight - C)

    maxvreme = 0
    for kombe in listaKombina:
        if len(kombe) >= 1:
            vreme = FIKSNO_VREME + len(kombe) * VREME_PO_PRATKA
            if vreme < maxvreme:
                maxvreme = vreme

    aktivnikombina = sum(1 for kombe in listaKombina if len(kombe) >= 1)

    fitnessvalue -= maxvreme * 100  # главна цел, скалирана да доминира
    fitnessvalue -= aktivnikombina  # tie-breaker, мал придонес

    return fitnessvalue


gene_space = [i for i in range(K)]  # секој ген (пратка) може да оди во кое било комби

params = {
    'num_generations': 200,
    'sol_per_pop': 100,
    'num_parents_mating': 40,
    'num_genes': N,
    'gene_space': gene_space,
    'fitness_func': fitness_func,
    'mutation_num_genes': 1
}

ga = pygad.GA(**params)
ga.run()

best_solution, best_fitness, _ = ga.best_solution()
print(f"Fitness: {best_fitness}")
print(f"Dodeluvanje na pratki: {decode(best_solution)}")