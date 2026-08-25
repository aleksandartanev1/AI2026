from constraint import *

if __name__ == '__main__':
    solver = input()
    problem = None
    if solver == 'BacktrackingSolver':
        problem = Problem(BacktrackingSolver())
    if solver == 'RecursiveBacktrackingSolver':
        problem = Problem(RecursiveBacktrackingSolver())
    if solver == 'MinConflictsSolver':
        problem = Problem(MinConflictsSolver())

    variables = list(range(81))
    domain = list(range(1, 10))

    problem.addVariables(variables, domain)

    for row in range(9):
        local_variables = [row * 9 + col for col in range(9)]
        problem.addConstraint(AllDifferentConstraint(), local_variables)

    for col in range(9):
        local_variables = [row * 9 + col for row in range(9)]
        problem.addConstraint(AllDifferentConstraint(), local_variables)

    for row in range(3):
        for col in range(3):
            local_variables=[]
            for r in range(3):
                for c in range(3):
                    local_variables.append((row * 3 + r) * 9 + (col * 3 + c))
            problem.addConstraint(AllDifferentConstraint(), local_variables)

    print(problem.getSolution())