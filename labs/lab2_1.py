from searching_framework import Problem, astar_search

dvizhenje = {
    "Desno 2": (2, 0),
    "Desno 3": (3, 0),
    "Gore": (0, 1),
    "Dolu": (0, -1),
    "Levo": (-1, 0)
}


class MazeSolver(Problem):
    def __init__(self, initial, goal, n, walls):
        super().__init__(initial, goal)
        self.n = n
        self.walls = set(walls)

    def is_valid(self, pos):
        x, y = pos
        return 0 <= x < self.n and 0 <= y < self.n and pos not in self.walls

    def is_valid_move(self, action, x, y):
        if action.startswith("Desno"):
            step = 1 if action == "Desno 2" else 2
            intermediate_positions = [(x + i, y) for i in range(1, step + 1)]
            if any(pos in self.walls for pos in intermediate_positions):
                return False
        return True

    def successor(self, state):
        successors = {}
        x, y = state

        for action, move in dvizhenje.items():
            new_x, new_y = x + move[0], y + move[1]

            if self.is_valid_move(action, x, y):
                if self.is_valid((new_x, new_y)):
                    successors[action] = (new_x, new_y)

        return successors

    def actions(self, state):
        return list(self.successor(state).keys())

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        x1, y1 = node.state
        x2, y2 = self.goal
        return (abs(x1 - x2) / 2 + abs(y1 - y2) / 2) / 2


if __name__ == '__main__':
    n = int(input())


    wall_count = int(input())
    walls = [tuple(map(int, input().split(","))) for _ in range(wall_count)]

    covek_x, covek_y = map(int, input().split(","))

    kukja_x, kukja_y = map(int, input().split(","))

    initial_state = (covek_x, covek_y)

    goal_state = (kukja_x, kukja_y)

    problem = MazeSolver(initial_state, goal_state, n, walls)
    solution = astar_search(problem)

    if solution:
        print(solution.solution())
    else:
        print("[]")
