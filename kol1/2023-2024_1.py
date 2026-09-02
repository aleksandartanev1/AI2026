from searching_framework import *


class Boxes(Problem):
    def __init__(self, man, boxes, n):
        self.n = n
        self.all_boxes = set(boxes)  # кутиите се ТРАЈНА пречка, дури и по полнење
        remaining = self.remove_adjacent(man, list(boxes))
        initial = (man, tuple(remaining))
        super().__init__(initial)

    def remove_adjacent(self, pos, boxes):
        """Ги отстранува од списокот на 'непополнети' кутии сите кои се
        соседни (вклучувајќи дијагонално) на дадената позиција - топката
        се става бесплатно, без посебен потег."""
        x, y = pos
        remaining = []
        for (bx, by) in boxes:
            if abs(bx - x) <= 1 and abs(by - y) <= 1:
                continue  # топка е ставена во оваа кутија
            remaining.append((bx, by))
        return remaining

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man, box = state
        return len(box) == 0

    def successor(self, state):
        succ = {}
        manpos, box = state

        moves = {
            "Gore": (0, 1),
            "Desno": (1, 0)
        }

        x, y = manpos

        for action, (mx, my) in moves.items():
            nx, ny = x + mx, y + my

            if not (0 <= nx < self.n and 0 <= ny < self.n):
                continue  # надвор од таблата

            if (nx, ny) in self.all_boxes:
                continue  # полето трајно е зафатено со кутија (полна или празна)

            new_boxes = self.remove_adjacent((nx, ny), box)
            succ[action] = ((nx, ny), tuple(new_boxes))

        return succ


if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    problem = Boxes(man_pos, boxes, n)

    result = breadth_first_graph_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")