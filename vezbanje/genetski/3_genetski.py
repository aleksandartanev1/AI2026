"""
Задача за вежба: Распоред на смени во кафуле

Кафуле работи D дена.
Секој ден има S смени (пр. утро, попladne, вечер — бројот на смени S е даден во влезот, ист за секој ден).
Кафулето има E вработени.
Секој вработен има свој хонорар по смена (различен за секој вработен, даден во влезот).

Правила:
За секоја смена (од вкупно D * S смени) мора да биде распореден точно еден вработен.
Ниту еден вработен не смее да работи повеќе од MAX_SMENI смени вкупно во целиот период (MAX_SMENI се чита од влез).
Целта е да се минимизира вкупниот трошок (сума од хонорарите на сите распоредени смени).
Ако две решенија имаат ист вкупен трошок, преферирај го она кое порамномерно ги распределува смените меѓу вработените (помала разлика помеѓу вработен со најмногу и вработен со најмалку доделени смени).

Од влез: D S E MAX_SMENI, потоа E броеви (хонорар по смена за секој вработен).

2 2 3 2
10 15 8

Хонорари: вработен0=10, вработен1=15, вработен2=8.
Очекуван вкупен трошок: 36.
"""
import pygad

D, S, E, MAX_SMENI = map(int, input().split())
honorari = []
h = input().split()
for i in range(E):
    honorari.append(int(h[i]))

def decode(solution):
    listasmeni = [[] for _ in range(E)]
    vkupnosmeni = D * S
    for i in range(vkupnosmeni):
        j = int(solution[i])
        listasmeni[j].append(1)
    return listasmeni

def fitness_func(ga_instance, solution, idx):
    listasmeni = decode(solution)
    fitnessvalue = 0
    totalCost = 0

    for id, vraboten in enumerate(listasmeni):
        totalcost = 0
        for smena in vraboten:
            totalcost += smena * honorari[id]
        totalCost += totalcost

        if len(vraboten) > MAX_SMENI:
            fitnessvalue -= 100000 * (len(vraboten) - MAX_SMENI)

    fitnessvalue -= totalCost * 100   # главна цел, скалирана да доминира

    brojSmeni = [len(vraboten) for vraboten in listasmeni]
    razlika = max(brojSmeni) - min(brojSmeni)
    fitnessvalue -= razlika          # tie-breaker

    return fitnessvalue


gene_space = [i for i in range(E)]

params = {
    "num_generations": 200,
    "sol_per_pop": 100,
    "num_parents_mating": 40,
    "num_genes": S * D,
    "fitness_func": fitness_func,
    "gene_space": gene_space,
    "mutation_num_genes": 1
}

ga = pygad.GA(**params)
ga.run()

best_solution, best_fitness, _ = ga.best_solution()
listasmeni_final = decode(best_solution)
totalCost = sum(len(v) * honorari[i] for i, v in enumerate(listasmeni_final))

print(f"najdobro reshenie:{best_solution}")
print(f"Najdobar vkupen troshok:{totalCost}")