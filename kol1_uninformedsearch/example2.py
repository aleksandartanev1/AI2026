from searching_framework import Problem, breadth_first_graph_search

grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

class Maze(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)



    def successor(self, state):
        succ = {}

        actions = {
            "up":(0,1),
            "right":(1,0),
            "down":(0,-1),
            "left":(-1, 0)
        }
        x, y = state

        for direction, (nx, ny) in actions.items():
            newx = x + nx
            newy = y + ny

            if 0 <= newx < 5 and 0 <= newy < 5 and grid[newx][newy] == 0:
                succ[direction] = (newx, newy)

        return succ

    def result(self, state, action):
        return self.successor(state)[action]

    def actions(self, state):
        return self.successor(state).keys()


if __name__ == '__main__':
     start = (0, 0)
     goal = (4, 4)

     problem = Maze(start, goal)

     result = breadth_first_graph_search(problem)

     if result:
         print(result.solution())
     else:
         print("no solution")

