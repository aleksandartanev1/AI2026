from constraint import *

if __name__ == '__main__':
    solver = input()
    problem = None
    if solver == "BacktrackingSolver":
        problem = Problem(BacktrackingSolver())
    elif solver == "RecursiveBacktrackingSolver":
        problem = Problem(RecursiveBacktrackingSolver())
    elif solver == "MinConflictsSolver":
        problem = Problem(MinConflictsSolver())

    variables = list(range(0, 81))
    domain = list(range(1, 10))

    problem.addVariables(variables, domain)

    for col in range(9):
        local = [row * 9 + col for row in range(9)]
        problem.addConstraint(AllDifferentConstraint(), local)

    for row in range(9):
        local = [row * 9 + col for col in range(9)]
        problem.addConstraint(AllDifferentConstraint(), local)

    for row in range(3):
        for col in range(3):
            local = []
            for r in range(3):
                for c in range(3):
                    local.append((row * 3 + r) * 9 + (col * 3 + c))
            problem.addConstraint(AllDifferentConstraint(), local)

    print(problem.getSolution())