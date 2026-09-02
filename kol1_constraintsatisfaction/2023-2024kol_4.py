from constraint import *


# potsetuvanje
# def count_in_col_i(*args):
#     # ovaa funkcija mozhe da se povika so bilo kolku argumenti, koi kje se dostapni vo nizata args

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot
    treecount = int(input())
    trees = []
    tents = []
    columntents = []

    for i in range(treecount):
        line = input().split(" ")
        treex, treey = int(line[0]), int(line[1])
        trees.append((treex,treey))
        tents.append(f"Tent{i+1}")

    linec = input().split(" ")
    for i in range(6):
        columntents.append(int(linec[i]))


    domain = []

    for i in range(6):
        for j in range(6):
            if (i, j) not in trees:
                domain.append((i,j))

    def sosed(obj1, obj2):
        x1, y1 = obj1
        x2, y2 = obj2
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 and (x1 == x2 or y1 == y2)

    def sosedtent(obj1, obj2):
        x1, y1 = obj1
        x2, y2 = obj2
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


    for i in range(treecount):
        availabledomain = []
        for d in domain:
            if sosed(d, trees[i]):
                availabledomain.append(d)
        problem.addVariable(tents[i], availabledomain)

    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----



    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------




    def tentcheck(*all_tents):
        for col in range(6):
            count = sum(1 for t in all_tents if t[0] == col)

            if count != columntents[col]:
                return False
        return True


    problem.addConstraint(AllDifferentConstraint(), tents)
    problem.addConstraint(tentcheck, tents)







    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------


    solution = problem.getSolution()
    if solution:
        for t in tents:
            print(f"{solution[t][0]} {solution[t][1]}")

    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----


