from searching_framework import *


class Laser(Problem):
    def __init__(self, man_pos, target_pos, timer, laser_pos, blocked, n, m):
        initial = (tuple(man_pos), timer, tuple(laser_pos))
        super().__init__(initial, target_pos)
        self.timer = timer
        self.blocked = tuple(blocked)
        self.n = n
        self.m = m

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        manpos, tmr, lsrpos = state
        return manpos == self.goal

    def successor(self, state):
        succ = {}

        directions = {
            "Gore":(0, 1),
            "Dolu":(0, -1),
            "Levo":(-1, 0),
            "Desno":(1, 0),
            "Stoj":(0, 0)
        }

        man, timer, laser = state

        for action, (nx, ny) in directions.items():
            x, y = man
            dx = x + nx
            dy = y + ny
            if (dx, dy) not in self.blocked:
                if 0 <= dx <= self.n and 0 <= dy <= self.m:
                    newtimer = timer + 1
                    newlaser = laser
                    if newtimer == 1:
                        newlaser = (dx, dy)
                    if newtimer == 4:
                        lsx, lsy = newlaser
                        if dx == lsx or lsy == dy:
                            continue
                        newtimer = 1
                        newlaser = (dx, dy)

                    succ[action] = ((dx, dy), newtimer, newlaser)

        return succ


read_two = lambda: tuple(map(int, input().split()))
if __name__ == '__main__':
    N, M = read_two()
    man_pos = read_two()
    target_pos = read_two()
    timer = int(input())
    laser_pos = read_two()
    blocked = [read_two() for _ in range(int(input()))]

    problem = Laser(man_pos, target_pos, timer, laser_pos, blocked, N, M)

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")
