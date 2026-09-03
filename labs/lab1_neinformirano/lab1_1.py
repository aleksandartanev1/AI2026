from searching_framework import *

class Robot(Problem):

    def __init__(self, initial, M1_pos, M1_steps, M2_pos, M2_steps,
                 parts_M1, parts_M2, walls):

        super().__init__(initial)

        self.M1_pos = M1_pos
        self.M2_pos = M2_pos
        self.M1_steps = M1_steps
        self.M2_steps = M2_steps

        self.parts_M1 = set(parts_M1)
        self.parts_M2 = set(parts_M2)
        self.walls = set(walls)

        self.dir = {"Up": (0, 1), "Down": (0, -1),
                    "Left": (-1, 0), "Right": (1, 0)}

    def goal_test(self, state):
        a, b, c, d, r1, r2, f = state
        return r1 and r2

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


    def successor(self, state):

        successors = {}

        x, y, collected1, collected2, r1, r2, progress = state

        collected1 = set(collected1)
        collected2 = set(collected2)

        # MOVEMENT
        for action in self.dir:

            dx, dy = self.dir[action]
            nx, ny = x + dx, y + dy

            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in self.walls:

                new_c1 = set(collected1)
                new_c2 = set(collected2)

                # collect parts for M1
                if not r1 and (nx, ny) in self.parts_M1:
                    new_c1.add((nx, ny))

                # collect parts for M2 only if M1 repaired
                if r1 and (nx, ny) in self.parts_M2:
                    new_c2.add((nx, ny))

                successors[action] = (
                    nx, ny,
                    frozenset(new_c1),
                    frozenset(new_c2),
                    r1,
                    r2,
                    0
                )

        # REPAIR
        if not r1 and (x, y) == self.M1_pos and len(collected1) == len(self.parts_M1):

            if progress + 1 == self.M1_steps:
                successors["Repair"] = (
                    x, y,
                    frozenset(collected1),
                    frozenset(collected2),
                    True,
                    r2,
                    0
                )
            else:
                successors["Repair"] = (
                    x, y,
                    frozenset(collected1),
                    frozenset(collected2),
                    r1,
                    r2,
                    progress + 1
                )

        elif r1 and not r2 and (x, y) == self.M2_pos and len(collected2) == len(self.parts_M2):

            if progress + 1 == self.M2_steps:
                successors["Repair"] = (
                    x, y,
                    frozenset(collected1),
                    frozenset(collected2),
                    r1,
                    True,
                    0
                )
            else:
                successors["Repair"] = (
                    x, y,
                    frozenset(collected1),
                    frozenset(collected2),
                    r1,
                    r2,
                    progress + 1
                )

        return successors


if __name__ == '__main__':

    robot_start_pos = tuple(map(int, input().split(',')))
    M1_pos = tuple(map(int, input().split(',')))
    M1_steps = int(input())
    M2_pos = tuple(map(int, input().split(',')))
    M2_steps = int(input())

    parts_M1 = int(input())
    to_collect_M1 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M1)])

    parts_M2 = int(input())
    to_collect_M2 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M2)])

    walls = [(4,0),(5,0),(7,5),(8,5),(9,5),
             (1,6),(1,7),(0,6),(0,8),(0,9),
             (1,9),(2,9),(3,9)]

    initial_state = (robot_start_pos[0], robot_start_pos[1],
                     frozenset(), frozenset(),
                     False, False, 0)

    problem = Robot(initial_state, M1_pos, M1_steps,
                    M2_pos, M2_steps,
                    to_collect_M1, to_collect_M2,
                    walls)

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")
