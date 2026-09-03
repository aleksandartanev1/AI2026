"""
Еден земјоделец треба да постави прскалки на својата нива за да ги наводнува посевите. Нивата е претставена како мрежа
(грид) со димензии M × N. Нивата се состои од:
    - полиња со посеви кои можат да се наводнуваат;
    - блокирани/неупотребливи полиња.
Бројот на неупотребливи полиња, како и нивните позиции, се дадени во влезот на крајот.
Земјоделецот има K прскалки. Може да постави произволен број прскалки до K (не мора сите), а прскалките може да се
постават на кое било поле. Ако прскалка се постави на поле со посеви, тогаш тие посеви се уништуваат.
Прскалката ги наводнува сите 8 соседни полиња (горе, долу, лево, десно и дијагонално), како и 4 полиња на растојание 2:
т.е. лево на растојание 2, горе, десно и долу на растојание 2 од прскалката.
Со користење на генетски алгоритам, треба да се максимизира бројот на наводнети посеви. Ако има повеќе решенија што
наводнуваат ист број посеви, тогаш треба да се избере решението што користи помал број прскалки.
На крај, испечатете број на наводнети посеви, број на искористени прскалки и позициите на прскалките.
"""
import pygad


def read_input():
    M, N = map(int, input().split())
    K = int(input())
    B = int(input())

    unusable = set()
    for _ in range(B):
        r, c = map(int, input().split())
        unusable.add((r, c))

    return M, N, K, unusable


def count_watered(solution):
    # Помошна функција: За дадено најдобро решение да се пресмета колку наводнети посеви има.
    listaPrskalki = decode(solution)
    navodnetiPolinja = set()
    blocked = unusable.copy()
    for i in range(0, len(listaPrskalki)):
        prskalka = listaPrskalki[i]
        prskalkaX = prskalka[0]
        prskalkaY = prskalka[1]
        if prskalkaX + 1 < M:
            navodnetiPolinja.add((prskalkaX + 1, prskalkaY))
        if prskalkaX - 1 >= 0:
            navodnetiPolinja.add((prskalkaX - 1, prskalkaY))
        if prskalkaY + 1 < N:
            navodnetiPolinja.add((prskalkaX, prskalkaY + 1))
        if prskalkaY - 1 >= 0:
            navodnetiPolinja.add((prskalkaX, prskalkaY - 1))
        if prskalkaX + 1 < M and prskalkaY + 1 < N:
            navodnetiPolinja.add((prskalkaX + 1, prskalkaY + 1))
        if prskalkaX - 1 >= 0 and prskalkaY - 1 >= 0:
            navodnetiPolinja.add((prskalkaX - 1, prskalkaY - 1))
        if prskalkaX - 1 >= 0 and prskalkaY + 1 < N:
            navodnetiPolinja.add((prskalkaX - 1, prskalkaY + 1))
        if prskalkaX + 1 < M and prskalkaY - 1 >= 0:
            navodnetiPolinja.add((prskalkaX + 1, prskalkaY - 1))
        if prskalkaX + 2 < M:
            navodnetiPolinja.add((prskalkaX + 2, prskalkaY))
        if prskalkaX - 2 >= 0:
            navodnetiPolinja.add((prskalkaX - 2, prskalkaY))
        if prskalkaY + 2 < N:
            navodnetiPolinja.add((prskalkaX, prskalkaY + 2))
        if prskalkaY - 2 >= 0:
            navodnetiPolinja.add((prskalkaX, prskalkaY - 2))
        if prskalka not in blocked:
            blocked.add(prskalka)

    fitnessValue = 0
    for el in navodnetiPolinja:
        # el = (X, Y)
        if el not in blocked:
            fitnessValue += 1

    return fitnessValue

def decode(solution):
    # solution = [0, X1, Y1, 1, X2, Y2, 1, X3, Y3,..., 0, Xk, Yk]
    outLista = []
    for i in range(0, len(solution), 3):
        if solution[i] == 1:
            outLista.append((int(solution[i + 1]), int(solution[i + 2])))

    return outLista


def fitness_func(ga_instance, solution, solution_idx):
    # listaPrskalki = [(X2, Y2), (X3, Y3),...]
    # unusable = {(1, 1), (4, 0), (2, 2)}
    listaPrskalki = decode(solution)
    navodnetiPolinja = set()
    blocked = unusable.copy()
    for i in range(0, len(listaPrskalki)):
        prskalka = listaPrskalki[i]
        prskalkaX = prskalka[0]
        prskalkaY = prskalka[1]
        if prskalkaX + 1 < M:
            navodnetiPolinja.add((prskalkaX + 1, prskalkaY))
        if prskalkaX - 1 >= 0:
            navodnetiPolinja.add((prskalkaX - 1, prskalkaY))
        if prskalkaY + 1 < N:
            navodnetiPolinja.add((prskalkaX, prskalkaY + 1))
        if prskalkaY - 1 >= 0:
            navodnetiPolinja.add((prskalkaX, prskalkaY - 1))
        if prskalkaX + 1 < M and prskalkaY + 1 < N:
            navodnetiPolinja.add((prskalkaX + 1, prskalkaY + 1))
        if prskalkaX - 1 >= 0 and prskalkaY - 1 >= 0:
            navodnetiPolinja.add((prskalkaX - 1, prskalkaY - 1))
        if prskalkaX - 1 >= 0 and prskalkaY + 1 < N:
            navodnetiPolinja.add((prskalkaX - 1, prskalkaY + 1))
        if prskalkaX + 1 < M and prskalkaY - 1 >= 0:
            navodnetiPolinja.add((prskalkaX + 1, prskalkaY - 1))
        if prskalkaX + 2 < M:
            navodnetiPolinja.add((prskalkaX + 2, prskalkaY))
        if prskalkaX - 2 >= 0:
            navodnetiPolinja.add((prskalkaX - 2, prskalkaY))
        if prskalkaY + 2 < N:
            navodnetiPolinja.add((prskalkaX, prskalkaY + 2))
        if prskalkaY - 2 >= 0:
            navodnetiPolinja.add((prskalkaX, prskalkaY - 2))
        if prskalka not in blocked:
            blocked.add(prskalka)

    fitnessValue = 0
    for el in navodnetiPolinja:
        # el = (X, Y)
        if el not in blocked:
            fitnessValue += 1

    # Ако има повеќе решенија што наводнуваат ист број посеви, избери решение што користи помал број прскалки.
    # fitnessValue ми враќа број на наводнати посеви. Тоа треба да е приоритет прво, а после бројот на прскалки.
    # fitnessValue -= len(listaPrskalki) * 100  -> НЕ! Пример:
    # 20 navodneti, 2 prskalki → 20 - 200 = -180
    # 19 navodneti, 1 prskalki → 19 - 100 = -81  ->  ова ќе се избере, а треба приоритет да е бројот на наводнети.

    fitnessValue = fitnessValue * 1000 - len(listaPrskalki)

    return fitnessValue


if __name__ == "__main__":
    M, N, K, unusable = read_input()
    # M - sizeX;
    # N - sizeY;
    # K - number of sprinkles

    gene_space = []
    for i in range(0, K):
        gene_space.append([0, 1])
        gene_space.append([i for i in range(0, M)])
        gene_space.append([i for i in range(0, N)])

    params = {
        'num_generations': 100,
        'sol_per_pop': 50,
        'num_parents_mating': 20,
        'num_genes': K * 3,
        'gene_space': gene_space,
        'fitness_func': fitness_func,
        'mutation_num_genes': 1
    }

    ga = pygad.GA(**params)
    ga.run()

    best_solution, solution_fitness, index = ga.best_solution()

    print(f'Broj na navodneti posevi: {count_watered(best_solution)}')
    print(f'Broj na iskoristeni prskalki: {len(decode(best_solution))}')
    print(f'Pozicii na prskalkite: {decode(best_solution)}')
