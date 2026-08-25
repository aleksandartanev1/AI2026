from searching_framework import *

graph = {
    "S": {"A": 1, "B": 4},
    "A": {"B": 2, "C": 5},
    "B": {"C": 1},
    "C": {"G": 3}
}

class RouteProblem(Problem):
    def __init__(self, graph, initial, goal):
        self.graph = graph
        super().__init__(initial, goal)

    def actions(self, state):
        #KOI CEKORI MOZHAM DA NAPRAVAM
        return list(self.graph.get(state, {}))


    def result(self, state, action):
        #ako OD STATE JA NAPRAVAM AKCIJATA, KOJA KJE E SOSTOJBATA
        return action

    def path_cost(self, c, state1, action, state2):
        #cenata od sostojba 1 do sostojba 2
        return c + self.graph[state1][state2]


if __name__ == '__main__':
    initial="S"
    goal="G"
    newprob = RouteProblem(graph, initial, goal)

    result = uniform_cost_search(newprob)
    if result:
        print(result.solution())
        print(result.path_cost)
    else:
        print("No solution")