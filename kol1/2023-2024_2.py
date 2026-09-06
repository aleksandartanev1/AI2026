from constraint import *


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot
    M = int(input())
    tents = [f"Tent{i}" for i in range(1,M+1)]
    domain = [(i,j) for i in range(6) for j in range (6)]
    trees = []
    for _ in range(M):
        x, y = map(int, input().split())
        trees.append((x,y))

    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----

    for i, tree in enumerate(trees):
        availabledomain = []
        for d in domain:
            if d not in trees:
                treex, treey = tree
                dx, dy = d
                if dx == treex or treey == dy:
                    if abs(dx - treex) <=1 and abs(dy - treey) <= 1:
                        availabledomain.append(d)
        problem.addVariable(tents[i], availabledomain)

    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------

    problem.addConstraint(AllDifferentConstraint(), tents)

    def touchingtents(t1, t2):
        t1x, t1y = t1
        t2x, t2y = t2

        if abs(t1x - t2x) <=1 and abs(t1y - t2y) <= 1:
            return False
        else:
            return True

    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            problem.addConstraint(touchingtents, [tents[i], tents[j]])

    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------
    solution = problem.getSolution()

    for tent in tents:
        print(f"{solution[tent][0]} {solution[tent][1]}")
    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----


