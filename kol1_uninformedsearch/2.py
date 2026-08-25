from searching_framework import Problem, breadth_first_graph_search


# define your Problem class here
class Ballplay(Problem):
    def __init__(self, manpos, ballpos):
        initial = (manpos, ballpos)
        super().__init__(initial)
        self.goals = {(7, 2), (7, 3)}
        self.enemies = {(3, 3), (5, 4)}

    def goal_test(self, state):
        man_pos, ball_pos = state
        return ball_pos in self.goals

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def is_adjacent(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1

    def successor(self, state):
        succ = {}

        directions = {
            "up": (0, 1),
            "down": (0, -1),
            "right": (1, 0),
            "up-right": (1, 1),
            "down-right": (1, -1)
        }

        man_pos, ball_pos = state

        for direction, (dx, dy) in directions.items():

            new_ball = (ball_pos[0] + dx, ball_pos[1] + dy)

            x, y = man_pos
            nx = x + dx
            ny = y + dy

            new_man = (nx, ny)

            if new_man == ball_pos and 0 <= new_man[0] < 8 and 0 <= new_man[1] < 6:
                if 0 <= new_ball[0] < 8 and 0 <= new_ball[1] < 6 and new_ball not in self.enemies:
                    near_enemy = False
                    for enemy in self.enemies:
                        if self.is_adjacent(new_ball, enemy):
                            near_enemy = True
                    if not near_enemy:
                        # валиден Push потег!
                        action_name = f"Push ball {direction}"
                        new_state = (ball_pos, new_ball)  # човекот оди каде беше топката, топката оди понатаму
                        succ[action_name] = new_state
            else:
                if 0 <= new_man[0] < 8 and 0 <= new_man[1] < 6 and new_man not in self.enemies:
                    action_name = f"Move man {direction}"
                    new_state = (new_man, ball_pos)
                    succ[action_name] = new_state

        return succ


if __name__ == '__main__':
    initial_state = (tuple(map(int, input().split(','))),
                     tuple(map(int, input().split(','))))

    problem = Ballplay(initial_state[0], initial_state[1])

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")