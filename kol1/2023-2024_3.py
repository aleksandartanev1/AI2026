from searching_framework import *

#from utils import *
#from uninformed_search import *
#from informed_search import *

class Boxes(Problem):
    def __init__(self, man_pos, n, boxes):
        initial = (man_pos, tuple(boxes))
        super().__init__(initial)
        self.n = n
        self.dontstand = boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man_pos, boxes = state
        return len(boxes) == 0

    def successor(self, state):
        succ = {}

        actions = {
            "Dolu":(0, -1),
            "Levo":(-1, 0)
        }

        man_pos, boxes = state
        for action, (ax, ay) in actions.items():
            x, y = man_pos
            nx = x + ax
            ny = y + ay
            if 0 <= nx < self.n and 0 <= ny <= self.n:
                if (nx, ny) not in self.dontstand:
                    newboxes = tuple(
                        box for box in boxes if not (abs(nx - box[0]) <= 1 and abs(ny - box[1]) <= 1)
                    )
                    succ[action] = ((nx, ny), newboxes)



        return succ


if __name__ == '__main__':
    n = int(input())
    man_pos = (n-1, n-1)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    problem = Boxes(man_pos, n, boxes)

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")