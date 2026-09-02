from constraint import *


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    movies = dict()

    genres = {
        "children's":[],
        "sci-fi":[],
        "action":[],
        "thriller":[],
        "fantasy":[],
        "drama":[],
        "horror":[],
    }

    variables = []

    n = int(input())
    for _ in range(n):
        film_info = input()
        film, genre, time = film_info.split(' ')
        variables.append(film)
        movies[film] = (float(time), genre)
        genres[genre].append(film)


    l_days = int(input())

    # Tuka definirajte gi promenlivite i domenite
    cinemas = ["Cinema 1", "Cinema 2"]
    filmtime = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    days = [f"Day {i + 1}" for i in range(l_days)]

    domain = []
    for d in days:
        for t in filmtime:
            for c in cinemas:
                domain.append(f"{d}_{t}_{c}")



    problem.addVariables(variables, domain)
    # Tuka dodadete gi ogranichuvanjata

    problem.addConstraint(AllDifferentConstraint(), variables)


    def childrens(*args):
        for slot in args:
            time = int(slot.split("_")[1])
            if time > 18:
                return False
        return True

    problem.addConstraint(childrens, genres["children's"])


    def make_overlap(film1, film2):
        def overlap(slot1, slot2):
            day1, time1, cinema1 = slot1.split("_")
            day2, time2, cinema2 = slot2.split("_")
            if day1 != day2 or cinema1 != cinema2:
                return True
            length1, genre1 = movies[film1]
            length2, genre2 = movies[film2]
            time1 = float(time1)
            time2 = float(time2)
            if time1 <= time2:
                return time1 + length1 <= time2
            else:
                return time2 + length2 <= time1

        return overlap


    for i in range(n):
        for j in range(i + 1, n):
            f1, f2 = variables[i], variables[j]
            problem.addConstraint(make_overlap(f1, f2), [f1, f2])


    def same_cinema(film1, film2):
        day1, time1, cinema1 = film1.split("_")
        day2, time1, cinema2 = film2.split("_")

        return cinema1 == cinema2

    for gen, films in genres.items():
        if gen == "sci-fi" or gen == "horror" or gen == "action":
            for i in range(len(films)):
                for j in range(i + 1, len(films)):
                    problem.addConstraint(same_cinema, [films[i], films[j]])





    # Tuka dodadete go kodot za pechatenje
    solution = problem.getSolution()
    if solution:
        for var in variables:
            parts = solution[var].split("_")
            print(f"{var}: {parts[0]} {parts[1]}:00 - {parts[2]}")
    else:
        print("No Solution!")