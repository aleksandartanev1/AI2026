from constraint import *


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["A", "B", "C", "D", "E", "F"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(100))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(lambda d, e: d + e == 150, ["D", "E"])
    problem.addConstraint(lambda f: (f % 10) % 4 == 0, ["F"])
    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(lambda a, b, c: a + b + c >= 100, ["A","B","C"])
    problem.addConstraint(lambda b: b % 2 != 0, ["B"])
    problem.addConstraint(lambda b: b % 2 != 0, ["D"])
    problem.addConstraint(lambda b: b % 2 != 0, ["E"])
    # ----------------------------------------------------


    print(problem.getSolution())