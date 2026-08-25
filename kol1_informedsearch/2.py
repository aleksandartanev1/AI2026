from searching_framework import Problem, astar_search

class Climber(Problem):
    def __init__(self, man, house, facing):
        initial = (man, house, facing)
        super().__init__(initial)

    def result(self, state, action):
        return self.successor(state)[action]

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        man, house, facing = state
        return man == house

    def h(self, node):
        man, house, facing = node.state
        x1, y1 = man
        x2, y2 = house
        return (abs(x1 - x2) + abs(y1 - y2)) / 2

    def successor(self, state):
        succ = {}
        man, house, facing = state

        directions = {
            "Wait": (0, 0),
            "Up 1": (0, 1),
            "Up 2": (0, 2),
            "Up-right 1": (1, 1),
            "Up-right 2": (2, 2),
            "Up-left 1": (-1, 1),
            "Up-left 2": (-2, 2)
        }

        for action, (nx, ny) in directions.items():
            x, y = man
            dx = x + nx
            dy = y + ny


            if 0 <= dx < 5 and 0 <= dy < 9:
                gx, gy = house

                if facing == 'right':
                    new_gx = gx + 1
                else:
                    new_gx = gx - 1

                if new_gx == 4:
                    new_facing = 'left'
                elif new_gx == 0:
                    new_facing = 'right'
                else:
                    new_facing = facing

                new_house = (new_gx, gy)

                if dy == 8:
                    if (dx, dy) == new_house:
                        succ[action] = ((dx, dy), new_house, new_facing)
                elif (dx, dy) in allowed:
                    succ[action] = ((dx, dy), new_house, new_facing)

        return succ


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    man = tuple(map(int, input().split(',')))
    house = tuple(map(int, input().split(',')))
    facing = input().strip()

    problem = Climber(man, house, facing)

    result = astar_search(problem, problem.h)

    if result is not None:
        print(result.solution())