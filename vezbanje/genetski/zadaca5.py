"""
Една фабрика треба да закаже задачи за поправка на своите машини користејќи тимови за поправка.
Фабриката има N машини. Секоја машина има: времетраење на поправката 't' и тип на машина 'c'. Информациите за сите
машини, се дадени во влезот. Машините треба да се поделат во тимови од точно 4 машини. Секоја машина мора да припаѓа
точно на еден тим. Вообичаено, времетраењето на работа на еден тим е еднакво на најдолгото време на поправка помеѓу
4-те доделени машини. Односно, време на тим = max(t1, t2, t3, t4). Но, пред да започне одржувањето, менаџментот на
фабриката избира еден префериран тип на машина P. Ако сите 4 машини во еден тим се од преферираниот тип P, техничарите
можат поефикасно да работат бидејќи повторно ги користат истите алатки и калибрации. Во тој случај, времетраењето на
тој тим станува: време на тим = min(t1, t2, t3, t4), наместо максимумот. Сите останати тимови продолжуваат да го
користат нормалното правило (максимално време). Со користење на генетски алгоритам, треба да се одреди:
како да се поделат машините во тимови од по 4 и кој тип на машина да се избере како префериран (P), така што вкупното
време за одржување на сите тимови да биде минимално. На крај, испечатете: минимално вкупно време за одржување,
избраниот префериран тип на машина, тимовите и машините доделени во секој тим.
"""
import pygad


def pomosnaFunkcijaZaPecatenje(solution):
    listaTimovi = []  # [[1, 2, 0, 4], [1, 2, 0, 4], [1, 2, 0, 4], ...]
    vremeTotal = 0
    izbranPreferiranTip = solution[0]
    for i in range(1, len(solution), 4):
        listaTim = []
        listaTim.append(solution[i])
        listaTim.append(solution[i + 1])
        listaTim.append(solution[i + 2])
        listaTim.append(solution[i + 3])
        # listaTim = [1, 2, 0, 4]
        listaTimovi.append(listaTim)
        listaVreminja = []
        listaVreminja.append(listaMasini[int(listaTim[0])][0])
        listaVreminja.append(listaMasini[int(listaTim[1])][0])
        listaVreminja.append(listaMasini[int(listaTim[2])][0])
        listaVreminja.append(listaMasini[int(listaTim[3])][0])
        # listaVreminja = [10, 11, 12, 18]
        listaTipovi = []
        listaTipovi.append(listaMasini[int(listaTim[0])][1])
        listaTipovi.append(listaMasini[int(listaTim[1])][1])
        listaTipovi.append(listaMasini[int(listaTim[2])][1])
        listaTipovi.append(listaMasini[int(listaTim[3])][1])
        # listaTipovi = ['A', 'B', 'A', 'D']
        preferiranTip = chr(int(solution[0]))
        vremeTim = 0
        if preferiranTip == listaTipovi[0] == listaTipovi[1] == listaTipovi[2] == listaTipovi[3]:
            vremeTim = min(listaVreminja)
            vremeTotal += vremeTim
        else:
            vremeTim = max(listaVreminja)
            vremeTotal += vremeTim

        fitnessValue = vremeTim

    return vremeTotal, izbranPreferiranTip, listaTimovi


def fitness_func(ga_instance, solution, solution_idx):
    # solution = [P, 1, 2, 0, 4, 3, 5, 6, 7,...]  -> префериран тип + индекси од машините во листата со машини
    fitnessValue = 0
    for i in range(1, len(solution), 4):
        listaTim = []
        listaTim.append(solution[i])
        listaTim.append(solution[i + 1])
        listaTim.append(solution[i + 2])
        listaTim.append(solution[i + 3])
        # listaTim = [1, 2, 0, 4]
        listaVreminja = []
        listaVreminja.append(listaMasini[int(listaTim[0])][0])
        listaVreminja.append(listaMasini[int(listaTim[1])][0])
        listaVreminja.append(listaMasini[int(listaTim[2])][0])
        listaVreminja.append(listaMasini[int(listaTim[3])][0])
        # listaVreminja = [10, 11, 12, 18]
        listaTipovi = []
        listaTipovi.append(listaMasini[int(listaTim[0])][1])
        listaTipovi.append(listaMasini[int(listaTim[1])][1])
        listaTipovi.append(listaMasini[int(listaTim[2])][1])
        listaTipovi.append(listaMasini[int(listaTim[3])][1])
        # listaTipovi = ['A', 'B', 'A', 'D']
        preferiranTip = chr(int(solution[0]))
        vremeTim = 0
        if preferiranTip == listaTipovi[0] == listaTipovi[1] == listaTipovi[2] == listaTipovi[3]:
            vremeTim = min(listaVreminja)
        else:
            vremeTim = max(listaVreminja)
        fitnessValue += vremeTim

    return (fitnessValue * -1)


if __name__ == '__main__':
    N = int(input())  # број на машини
    listaMasini = []  # [(10, 'A'), (12, 'A'), (15, 'B'),...]
    for i in range(0, N):
        vlez = input().split(" ")
        vreme = int(vlez[0])
        tip = vlez[1]
        listaMasini.append((vreme, tip))

    tipovi = set()  # {'A', 'B', 'C', 'D', ...}
    for (vreme, tip) in listaMasini:
        tipovi.add(ord(tip))  # За char -> ASCII се користи ord, а не int

    gene_space = []
    gene_space.append(list(tipovi))  # A-Z vo ASCII

    for i in range(0, N):
        gene_space.append([i for i in range(0, N)])

    params = {
        'num_generations': 300,
        'sol_per_pop': 50,
        'num_parents_mating': 20,
        'num_genes': N + 1,
        'gene_space': gene_space,
        'fitness_func': fitness_func,
        'mutation_num_genes': 1,
        'allow_duplicate_genes': False  # МНОГУ ВАЖНО ЗА ДА НЕМА ИСТА МАШИНА ВО ПОВЕЌЕ ТИМОВИ!
    }

    ga = pygad.GA(**params)
    ga.run()

    best_solution, _, _ = ga.best_solution()

    vremeTotal, izbranPreferiranTip, listaTimovi = pomosnaFunkcijaZaPecatenje(best_solution)
    print(f'Vkupnoto vreme na odrzuvanje na najdobrata podelba po timovi: {vremeTotal}')
    print(f'Izbraniot najdobar preferiran tip na masina: {chr(int(izbranPreferiranTip))}')

    listaTimoviTorki = []
    for tim in listaTimovi:
        # listaTimovi = [[1, 2, 0, 4], [1, 2, 0, 4], [1, 2, 0, 4], ...]
        # tim = [1, 2, 0, 4]
        tmpLista = []
        tmpLista.append(listaMasini[int(tim[0])])
        tmpLista.append(listaMasini[int(tim[1])])
        tmpLista.append(listaMasini[int(tim[2])])
        tmpLista.append(listaMasini[int(tim[3])])
        listaTimoviTorki.append(tmpLista)

    print(f'Podelbata po timovi: {listaTimoviTorki}')
