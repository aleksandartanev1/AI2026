from utils import *
from uninformed_search import *
from informed_search import *


class Boxes(Problem):
    def __init__(self, num_boxes, boxes, man_pos):
        # Бидејќи n не е експлицитно пратено во повикот во main, го наоѓаме преку почетната позиција (n-1, n-1)
        self.n = man_pos[0] + 1
        self.all_box_positions = set(boxes)  # Кутиите остануваат на таблата засекогаш, не смее да се згазне на нив

        # На почеток, ги собираме топките од кутиите кои веќе се соседни на почетната позиција на човечето
        initial_boxes = tuple(b for b in boxes if max(abs(man_pos[0] - b[0]), abs(man_pos[1] - b[1])) > 1)
        initial_state = (man_pos, initial_boxes)

        super().__init__(initial_state)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # Целта е постигната кога нема повеќе кутии со преостанати топки
        return len(state[1]) == 0

    def successor(self, state):
        successors = {}
        man_pos, remaining_boxes = state
        x, y = man_pos

        # Дефинирање на можните движења (Надолу го намалува y, Налево го намалува x)
        moves = {
            "Dolu": (x, y - 1),
            "Levo": (x - 1, y)
        }

        for action, (nx, ny) in moves.items():
            # Проверка за граници на таблата
            if 0 <= nx < self.n and 0 <= ny < self.n:
                # Човечето не смее да застане на поле каде што има кутија
                if (nx, ny) not in self.all_box_positions:
                    # Ги отстрануваме кутиите кои станале соседни (вклучувајќи и дијагонално) на новата позиција
                    new_boxes = tuple(b for b in remaining_boxes if max(abs(nx - b[0]), abs(ny - b[1])) > 1)
                    successors[action] = ((nx, ny), new_boxes)

        return successors


if __name__ == '__main__':
    n = int(input())
    man_pos = (n - 1, n - 1)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    prob = Boxes(num_boxes, boxes, man_pos)

    result = breadth_first_graph_search(prob)

    if result:
        print(result.solution())
    else:
        print("No Solution!")