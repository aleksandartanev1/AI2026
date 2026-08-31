from constraint import *

if __name__ == '__main__':

    bands = dict()
    variables = []
    band_info = input()
    durations = {}
    genres = {
        "rock":[],
        "punk":[],
        "metal":[]
    }

    genre_times = {
        "rock":0,
        "punk":0,
        "metal":0,
    }

    while band_info != 'end':
        band, genre, time = band_info.split(' ')
        bands[band] = (genre, time)
        band_info = input()
        details = f"{band} (('{genre}', '{time}'))"
        variables.append(details)
        genres[genre].append(details)
        genre_times[genre] += int(time)
        durations[details] = int(time)


    domain = ["S1", "S2", "S3"]

    problem = Problem(BacktrackingSolver())

    # Change this section if necessary
    problem.addVariables(variables, domain)

    # Add the constraints here
    bands_120 = [v for v in variables if durations[v] == 120]

    problem.addConstraint(AllDifferentConstraint(), bands_120)

    bands_80 = [v for v in variables if durations[v] < 80]

    def max_5(*ba):
        stages = {"S1":0, "S2":0, "S3":0}
        for b in ba:
            stages[b] += 1
            if stages[b] > 5:
                return False
        return True

    problem.addConstraint(max_5, bands_80)

    for g, g_items in genres.items():
        if len(g_items) > 1 and genre_times[g] <= 300:
            problem.addConstraint(AllEqualConstraint(), g_items)

    result = problem.getSolution()

    # Add the printing section here
    for var in variables:
        print(f"{var}: {result[var]}")
