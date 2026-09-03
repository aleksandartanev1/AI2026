"""
Двајца пријатели планираат да истражуваат мрежа од N градови. Тие започнуваат од истиот почетен град S и сакаат да ги
посетат сите останати градови што е можно поефикасно. По посетата на градовите, двајцата мора да ја завршат својата
рута во одреден заеднички град E, каде повторно ќе се сретнат. Пријателите можат да ја поделат работата меѓу себе на
било кој начин. Секој град (освен почетниот и крајниот) мора да биде посетен точно еднаш од еден од пријателите,
односно сите градови мора да бидат посетени, и ниту еден град не смее да биде посетен и од едниот, и од другиот
(освен S и E). Целта е да се организираат нивните рути така што вкупното време потребно за двајцата да завршат ќе
биде минимизирано. Од влезот ви се дадени N, бројот на градови означени со вредности од 0 до N-1. Во следниот ред ви
се дадени почетниот град S и крајниот град E. Дополнително, дадена е матрица dist со димензии N x N, каде dist[i][j]
го претставува времето потребно да се патува од град i до град j. Секој пријател започнува од градот S, посетува
подмножество од градовите, и потоа продолжува кон градот E. Рутата е дефинирана како низа од градови која започнува
со S и завршува со E. Целта е да се распределат градовите меѓу двајцата пријатели и да се одреди редоследот во кој ќе
ги посетуваат така што сите градови (освен S и E) ќе бидат посетени точно еднаш, и времето потребно за двајцата да
завршат ќе биде минимизирано. Вкупното време на еден пријател се дефинира како збир од времињата на патување помеѓу
паровите соседни градови во неговата рута. Бидејќи пријателите се движат паралелно, целта е да се минимизира
максималното време помеѓу двете рути. Користејќи генетски алгоритми, дополнете делови од дадениот почетен код за
алгоритмот да функционира правилно. Менувајте параметри на сопствен ризик. Дефинирајте соодветен gene space за овој
проблем. Размислете како да го енкодирате редоследот на посетување на градовите, како и кој пријател е одговорен за
секој град. Дизајнирајте decode функција која како влез прима решение/хромозом, а како излез враќа две рути, по една
за секој пријател. Секоја рута мора да започнува со S и да завршува со E. Decode функцијата мора да осигура дека секој
град (освен S и E) се појавува точно еднаш во двете рути. Пример излез: [[S, A, B, C, E], [S, D, E]] каде сите градови
се цели броеви. Дизајнирајте fitness функција која ги следи следниве принципи:
    Целта е да се минимизира максималното време на патување помеѓу двајцата пријатели.
    Доколку еден пријател има значително подолго време од другиот (значи повеќе од двојно), треба да се додели голема
    казна.
    Доколку бројот на градови распределени меѓу двајцата пријатели е нерамномерен, треба да се додели помала казна
    за да се поттикнат побалансирани решенија.
Направете submit на fitness функцијата, decode функцијата и најдобрите хромозоми од секоја генерација до grader-от.
"""
import pygad

N = int(input())  # број на градови
S, E = map(int, input().split())  # start и goal
dist = [list(map(float, input().split())) for _ in range(N)]  # матрица од растојанија X<->Y


def decode(solution):
    # solution = [S, A, B, S, C, G, S, D, E, F, G]
    route1 = [S]
    route2 = [S]

    poseteniGradovi = []

    counter = 0
    for val in solution:
        if val == S:
            continue
        if val == E:
            counter = 1
            continue
        else:
            if val in poseteniGradovi:
                continue
            if counter == 0:
                route1.append(val)
            else:
                route2.append(val)
            poseteniGradovi.append(val)

    # додавам сега градови кои воопшто не се во хромозомот
    for i in range(N):
        if i != S and i != E and i not in poseteniGradovi:
            route2.append(i)

    route1.append(E)
    route2.append(E)

    return route1, route2


def fitness_func(ga, solution, idx):
    route1, route2 = decode(solution)
    # route1 = [S, A, B, C, G];  route2 = [S, D, E, F, G]

    fitnessValue = 0

    time1 = 0
    time2 = 0

    for i in range(0, len(route1) - 1):
        fitnessValue += dist[int(route1[i])][int(route1[i + 1])]

    time1 = fitnessValue

    for i in range(0, len(route2) - 1):
        fitnessValue += dist[int(route2[i])][int(route2[i + 1])]

    time2 = fitnessValue - time1

    if time1 > time2 * 2:
        fitnessValue -= 10000
    if time2 > time1 * 2:
        fitnessValue -= 10000

    if len(route1) != len(route2):
        fitnessValue -= 10000

    return fitnessValue*-1


gene_space = [i for i in range(0, N)]

params = {
    'num_generations': 500,
    'sol_per_pop': 100,
    'num_parents_mating': 50,

    'num_genes': N + 2,
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

# submit_data(fitness_func, decode, best_solutions)
