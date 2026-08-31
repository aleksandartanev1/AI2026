from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    number = int(input())

    domain = []
    for i in range(number):
        for j in range(number):
            domain.append((i,j))

    variables = list(range(1, number + 1))

    problem.addVariables(variables, domain)

    def peace(q1, q2):
        x1, y1 = q1
        x2, y2 = q2

        return x1 != x2 and y1 != y2 and (abs(x1 - x2) != abs(y1 - y2))

    for i in range(number):
        for j in range(number):
            if i == j:
                continue
            problem.addConstraint(peace, [variables[i], variables[j]])


    if number <= 6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())