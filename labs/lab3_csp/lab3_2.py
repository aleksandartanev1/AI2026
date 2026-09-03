from operator import truediv

from constraint import Problem, BacktrackingSolver


def read_input():
    num_families = int(input())
    families = {}
    for _ in range(num_families):
        name, size, reqs_string = input().split()
        reqs = reqs_string.split('-')
        families[name] = {'size': int(size), 'requirements': reqs}

    num_rooms = int(input())
    rooms = {}
    for _ in range(num_rooms):
        room_id, capacity, amenities_string = input().split()
        floor = room_id[0]
        amenities = amenities_string.split('-')
        rooms[int(room_id)] = {'floor': int(floor), 'capacity': int(capacity), 'amenities': amenities}

    return families, rooms


if __name__ == '__main__':
    problem = Problem(solver=BacktrackingSolver())

    families, rooms = read_input()

    family_names = list(families.keys())

    for f in family_names:
        valid_rooms = []

        for r_id, r in rooms.items():
            if r['capacity'] >= families[f]['size'] and \
                    all(req in r['amenities'] for req in families[f]['requirements']):
                valid_rooms.append(r_id)
        valid_rooms.append(None)
        problem.addVariable(f, valid_rooms)


    def all_diff(*vals):
        used = []
        for v in vals:
            if isinstance(v, dict):
                return True
            if v is not None:
                if v in used:
                    return False
                used.append(v)
        return True


    problem.addConstraint(all_diff, family_names)


    def fairness(*vals):
        if any(isinstance(v, dict) for v in vals):
            return True

        assignment = dict(zip(family_names, vals))
        used_rooms = set(v for v in vals if v is not None)

        for f in family_names:
            if assignment[f] is None:
                for r_id, r in rooms.items():
                    if r_id not in used_rooms:
                        if r['capacity'] >= families[f]['size'] and \
                                all(req in r['amenities'] for req in families[f]['requirements']):
                            return False

                if f.startswith('VIP_'):
                    for other_f, other_room in assignment.items():
                        if other_room is None:
                            continue
                        if other_room.startswith("VIP_"):
                            continue
                        r = rooms[other_room]
                        if r['capacity'] >= families[f]['size'] and \
                                all(req in r['amenities'] for req in families[f]['requirements']):
                            return False
        return True


    problem.addConstraint(fairness, family_names)

    solutions = problem.getSolutions()

    if not solutions:
        print("No solution")
        exit()

    best = None
    best_score = -1
    for sol in solutions:
        total = 0

        for f in family_names:
            if sol[f] is not None:
                total += families[f]['size']
        if total > best_score:
            best_score = total
            best = sol
    print("Best assignment:")
    for f in family_names:


        if best[f] is not None:
            print(f"{f}->{best[f]} ")