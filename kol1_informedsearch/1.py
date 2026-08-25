from searching_framework import Problem, astar_search

class Wayhome(Problem):
    def __init__(self, person, house, walls, gridsize):
        super().__init__(person, house)
        self.walls = tuple(walls)
        self.gridsize = gridsize

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        x1, y1 = node.state
        x2, y2 = self.goal
        return (abs(x1 - x2) + abs(y2 - y2)) / 3

    def goal_test(self, state):
        return state == self.goal

    def successor(self, state):
        succ = {}


        actions = {
            "Up": (0, 1),
            "Right 3":(3, 0),
            "Right 2":(2,0),
            "Down":(0, -1),
            "Left":(-1, 0)
        }
        px, py = state
        for action, (nx, ny) in actions.items():
            npx = px + nx
            npy = py + ny
            if 0 <= npx < self.gridsize and 0 <= npy < self.gridsize:
                if (npx, npy) not in self.walls:
                    if action == "Right 3":
                        if (npx - 1, npy) not in self.walls and (npx - 2, npy) not in self.walls:
                            succ[action] = (npx,npy)
                    elif action == "Right 2":
                        if (npx - 1, npy) not in self.walls:
                            succ[action] = (npx,npy)
                    else:
                        succ[action] = (npx,npy)

        return succ





if __name__ == '__main__':
    gridsize = int(input())
    wallcount = int(input())
    walls = []

    for i in range(wallcount):
        wall = tuple(map(int, input().split(',')))
        walls.append(wall)

    person = tuple(map(int, input().split(',')))
    house = tuple(map(int, input().split(',')))

    problem = Wayhome(person, house, walls, gridsize)

    result = astar_search(problem)
    if result:
        print(result.solution())