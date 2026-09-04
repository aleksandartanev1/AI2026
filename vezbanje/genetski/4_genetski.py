import pygad

N = int(input())
vestini = []
for _ in range(N):
    line = input().split(" ")
    skill = int(line[0])
    tech = line[1]
    vestini.append((skill, tech))

# сите различни технологии што реално се појавуваат меѓу учесниците
tehnologii = sorted(set(t for (s, t) in vestini))   # пр. ['J', 'P']
print(tehnologii)

brojTimovi = N // 4


def decode(solution):
    # solution[0] = индекс во listaTehnologii (избраниот фокус-јазик F)
    # solution[1..N] = за секој учесник, во кој тим оди (0 до brojTimovi-1)
    F = tehnologii[int(solution[0])]
    listaTimovi = [[] for _ in range(brojTimovi)]
    for i in range(N):
        j = int(solution[i + 1])
        listaTimovi[j].append(i)
    return F, listaTimovi


def fitness_function(ga, solution, idx):
    F, listaTimovi = decode(solution)
    fitnessValue = 0
    totalScore = 0
    rezultatiPoTim = []

    for tim in listaTimovi:
        # казна ако тимот НЕМА точно 4 членови
        if len(tim) != 4:
            fitnessValue -= 100000 * abs(len(tim) - 4)

        skillSum = sum(vestini[idx_uchesnik][0] for idx_uchesnik in tim)
        siteIsti = all(vestini[idx_uchesnik][1] == F for idx_uchesnik in tim) and len(tim) == 4

        if siteIsti:
            rezultatTim = skillSum * 1.5
        else:
            rezultatTim = skillSum

        totalScore += rezultatTim
        rezultatiPoTim.append(rezultatTim)

    fitnessValue += totalScore * 100   # главна цел, скалирана да доминира

    if rezultatiPoTim:
        razlika = max(rezultatiPoTim) - min(rezultatiPoTim)
        fitnessValue -= razlika        # tie-breaker, мал придонес

    return fitnessValue


gene_space = [[i for i in range(len(tehnologii))]]   # ген 0: избор на F
for i in range(N):
    gene_space.append([i for i in range(brojTimovi)])  # гени 1..N: тим по учесник

params = {
    "num_generations": 300,
    "sol_per_pop": 100,
    "num_parents_mating": 40,
    "num_genes": N + 1,
    "fitness_func": fitness_function,
    "gene_space": gene_space,
    "mutation_num_genes": 1,
}

ga = pygad.GA(**params)
ga.run()

best_solution, best_fitness, _ = ga.best_solution()
F, listaTimovi = decode(best_solution)

totalScore = 0
for tim in listaTimovi:
    skillSum = sum(vestini[i][0] for i in tim)
    siteIsti = all(vestini[i][1] == F for i in tim) and len(tim) == 4
    totalScore += skillSum * 1.5 if siteIsti else skillSum

print(f"Izbran fokus-jazik F: {F}")
print(f"Timovi: {listaTimovi}")
print(f"Vkupen rezultat: {totalScore}")