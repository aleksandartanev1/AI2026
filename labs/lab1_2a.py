from searching_framework import Problem, breadth_first_graph_search #, just an example, import whatever you actually need from the searching framework
# note that your program won't work if you copy paste classes instead of import them via the above statement

# define your Problem class here
opponents = {(3, 3),(2,3),(2,2),(2,4),(3,2),(3,4),(4,3),(4,2),(4,4),
             (5, 4),(5,5),(5,3),(4,4),(4,3),(4,5),(6,4),(6,3),(6,5)}
goal = {(7, 2), (7, 3)}


class Igrac(Problem):
    def __init__(self, initial):
        super().__init__(initial)


    def goal_test(self, state):
        manx, many, ballx, bally = state
        return (ballx, bally) in goal

    def successor(self, state):
        dir = {"up-right": (1, 1), "down-right": (1, -1), "right": (1, 0), "up": (0, 1), "down": (0, -1), }
        successors = {}

        manx, many, ballx, bally = state

        for action, (dx, dy) in dir.items():
            nmx = manx + dx
            nmy = many + dy
            if (nmx, nmy) == (ballx, bally):
                nbx, nby = ballx + dx, bally + dy
                if (nbx, nby) not in opponents \
                        and (nmx, nmy) not in {(3, 3), (5, 4)} \
                        and 0 <= nbx <= 7 and 0 <= nby <= 5 and 0 <= nmx <= 7 and 0 <= nmy <= 5:
                    successors[f"Push ball {action}"] = (nmx, nmy, nbx, nby)
            else:
                if (nmx, nmy) not in {(3, 3), (5, 4)} \
                        and 0 <= nmx <= 7 and 0 <= nmy <= 5:
                    successors[f"Move man {action}"] = (nmx, nmy, ballx, bally)

        return successors


    def actions(self, state):
        return self.successor(state).keys()


    def result(self, state, action):
        return self.successor(state)[action]



if __name__ == '__main__':
    manx, many = map(int, input().split(','))
    ballx, bally = map(int, input().split(','))

    initial = (manx, many, ballx, bally)

    problem = Igrac(initial)

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")

