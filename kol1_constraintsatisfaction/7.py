from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    lecture_slots_AI = int(input())
    lecture_slots_ML = int(input())
    lecture_slots_R = int(input())
    lecture_slots_BI = int(input())

    AI_lectures_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_lectures_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_lectures_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                         "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_lectures_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_exercises_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_exercises_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_exercises_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Add the variables here--------------------

    variables = []
    ml_exercises = []
    ml_lessons = []

    tempvar = []
    for i in range(lecture_slots_AI):
        variables.append(f"AI_lecture_{i + 1}")
        tempvar.append(f"AI_lecture_{i + 1}")

    problem.addVariables(tempvar, AI_lectures_domain)

    tempvar = []
    for i in range(lecture_slots_ML):
        variables.append(f"ML_lecture_{i + 1}")
        tempvar.append(f"ML_lecture_{i + 1}")
        ml_lessons.append(f"ML_lecture_{i + 1}")

    problem.addVariables(tempvar, ML_lectures_domain)

    tempvar = []
    for i in range(lecture_slots_R):
        variables.append(f"R_lecture_{i + 1}")
        tempvar.append(f"R_lecture_{i + 1}")

    problem.addVariables(tempvar, R_lectures_domain)

    tempvar = []
    for i in range(lecture_slots_BI):
        variables.append(f"BI_lecture_{i + 1}")
        tempvar.append(f"BI_lecture_{i + 1}")

    problem.addVariables(tempvar, BI_lectures_domain)

    problem.addVariable("ML_exercises", ML_exercises_domain)
    problem.addVariable("BI_exercises", BI_exercises_domain)
    problem.addVariable("AI_exercises", AI_exercises_domain)

    variables.append("ML_exercises")
    variables.append("BI_exercises")
    variables.append("AI_exercises")

    ml_exercises.append("ML_exercises")

    # ---Add the constraints here----------------

    def overlap(val1, val2):
        day1, time1 = val1.split("_")
        day2, time2 = val2.split("_")

        if day1 != day2:
            return True
        if abs(int(time1) - int(time2)) >= 2:
            return True


    for i in range(len(variables)):
        for j in range(len(variables)):
            if i == j:
                continue
            problem.addConstraint(overlap, [variables[i], variables[j]])


    def ml_check(val1, val2):
        day1, time1 = val1.split("_")
        day2, time2 = val2.split("_")

        return time1 != time2

    for lesson in ml_lessons:
        for exercise in ml_exercises:
            problem.addConstraint(ml_check, [lesson, exercise])
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)