from searching_framework import Problem, breadth_first_graph_search #, just an example, import whatever you actually need from the searching framework
# note that your program won't work if you copy paste classes instead of import them via the above statement

# define your Problem class here
opponents = {(3, 3),(5, 4)}
goal = {(7, 2), (7, 3)}

def is_valid_ball(bx, by):
    if bx < 0 or bx > 7 or by < 0 or by > 5:
        return False
    for ox, oy in opponents:
        if abs(bx - ox) <= 1 and abs(by - oy) <= 1:
            return False
    return True


def is_valid_man(mx, my, bx, by):
    if mx < 0 or mx > 7 or my < 0 or my > 5:
        return False
    if (mx, my) == (bx, by):
        return False
    for ox, oy in opponents:
        if (mx, my) == (ox, oy):
            return False
    return True


class Person(Problem):
    def __init__(self, initial):
        super().__init__(initial)


    def goal_test(self, state):
        man_x, man_y, ball_x, ball_y = state
        return (ball_x, ball_y) in goal

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def successor(self, state):
        successors = {}
        man_x, man_y, ball_x, ball_y = state
        dir = {"up-right": (1, 1), "down-right": (1, -1), "right": (1, 0), "up": (0, 1), "down": (0, -1), }

        for action, (dx, dy) in dir.items():
            nx, ny = man_x + dx, man_y + dy

            if (nx, ny) == (ball_x, ball_y):
                nbx, nby = ball_x + dx, ball_y + dy
                if is_valid_ball(nbx, nby) and  is_valid_man(nx, ny, nbx, nby):
                    successors[f"Push ball {action}"] = (nx, ny, nbx, nby)

            else:
                if is_valid_man(nx, ny, ball_x, ball_y):
                    successors[f"Move man {action}"] = (nx, ny, ball_x, ball_y)

        return successors


if __name__ == '__main__':
    man_start = tuple(map(int, input().split(',')))
    ball_start = tuple(map(int, input().split(',')))
    initial = (man_start[0], man_start[1], ball_start[0], ball_start[1])
    problem = Person(initial)
    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")