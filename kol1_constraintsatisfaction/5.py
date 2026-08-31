from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    domain = [0, 1]
    meetingtime = [12, 13, 14, 15, 16, 17, 18, 19, 20]
    # Add the domains
    problem.addVariable("Simona_attendance", domain)
    problem.addVariable("Marija_attendance", domain)
    problem.addVariable("Petar_attendance", domain)
    problem.addVariable("time_meeting", meetingtime)
    # ----------------------------------------------------

    # ---Add the constraints----------------

    problem.addConstraint(lambda m, s, p: m + s + p >= 2, ["Marija_attendance", "Simona_attendance", "Petar_attendance"])
    problem.addConstraint(lambda s: s == 1, ["Simona_attendance"])

    # ----------------------------------------------------

    def simona(s, t):
        if s == 0:
            return True
        return t in (13, 14, 16, 19)

    problem.addConstraint(simona, ["Simona_attendance", "time_meeting"])

    def maria(m, t):
        if m == 0:
            return True
        return t in (14, 15, 18)

    problem.addConstraint(maria, ["Marija_attendance", "time_meeting"])

    def petar(p, t):
        if p == 0:
            return True
        return t in (12, 13, 16, 17, 18, 19)

    problem.addConstraint(petar, ["Petar_attendance", "time_meeting"])

    solutions = problem.getSolutions()


    sortproblem = sorted(solutions, key=lambda x: x["Marija_attendance"], reverse=True)
    for solution in sortproblem:
        print({k: solution[k] for k in ["Simona_attendance", "Marija_attendance", "Petar_attendance", "time_meeting"]})
