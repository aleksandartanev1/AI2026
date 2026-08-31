from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot
    treecount = int(input())
    trees = []
    for i in range(treecount):
        line = input().split(" ")
        trees.append((int(line[0]), int(line[1])))

    domain = []
    for i in range(6):
        for j in range(6):
            if (i, j) not in trees:
                domain.append((i,j))

    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----
    variables = [f"Shator {i+1}" for i in range(treecount)]

    def not_sosed(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2

        return abs(x1 - x2) > 1 or abs(y1 - y2) > 1

    def sosed(x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 and (x1 == x2 or y1 == y2)

    for i in range(treecount):
        treex, treey = trees[i]

        available_domain = []
        for cor in domain:
            x, y = cor
            if sosed(x, y, treex, treey):
                available_domain.append(cor)

        problem.addVariable(variables[i], available_domain)




    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------
    problem.addConstraint(AllDifferentConstraint(), variables)

    for i in range(treecount):
        for j in range(treecount):
            if i == j:
                continue
            problem.addConstraint(not_sosed, [variables[i], variables[j]])

    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------

    solution = problem.getSolution()

    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----
    for i in range(treecount):
        tx, ty = solution[f"Shator {i+1}"]
        print(f"{tx} {ty}")


