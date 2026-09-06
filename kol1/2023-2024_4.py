
from constraint import *

# potsetuvanje
# def count_in_col_i(*args):
#     # ovaa funkcija mozhe da se povika so bilo kolku argumenti, koi kje se dostapni vo nizata args

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot
    M = int(input())
    tents = [f"Tents{i}" for i in range(1, M + 1)]
    domain = [(i,j) for i in range(6) for j in range(6)]
    trees = []
    for _ in range(M):
        x, y = map(int, input().split())
        trees.append((x,y))
    line = input().split()
    columntents = [int(l) for l in line]

    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----

    for i, tree in enumerate(trees):
        availabledomain = []
        for d in domain:
            if d not in trees:
                dx, dy = d
                treex, treey = tree
                if dx == treex or dy == treey:
                    if (abs(dx - treex) <=1 and abs(dy - treey) <= 1):
                        availabledomain.append(d)
        problem.addVariable(tents[i], availabledomain)

    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------

    problem.addConstraint(AllDifferentConstraint(), tents)




    def columntentsconstraint(*args):
        counts = [0] * 6
        for tx, ty in args:
            counts[tx] += 1

        return counts == columntents


    problem.addConstraint(columntentsconstraint, tents)

    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------

    solution = problem.getSolution()

    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----
    if solution:
        for tent in tents:
            print(f"{solution[tent][0]} {solution[tent][1]}")
    else:
        print("No Solution")

