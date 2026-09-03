"""
📝 Задача: Робот со кутија
Имаме табла 4x4.
Почетна состојба: роботот е на позиција (0,0) и има кутија на позиција (1,1).
Целна состојба: кутијата треба да се донесе на позиција (3,3).
Роботот може да се движи Горе, Долу, Лево, Десно.
Ако роботот е веднаш до кутијата, може да ја турне во насока на движење (кутијата се движи заедно со него).
Роботот и кутијата не смеат да излезат надвор од таблата.

🔑 Правила
Состојбата ја претставуваме како tuple: (robot_pos, box_pos).
Акции:
Движење на роботот ако не е блокиран.
Туркање на кутијата ако роботот е до неа и има слободно поле во насоката.
Цел: кутијата да стигне на (3,3) (роботот може да биде било каде).

💡 Твоја задача
Напиши класа RobotBox(Problem) со состојба (robot_pos, box_pos).
Во successor генерирај ги сите можни акции:
Роботот се движи сам.
Роботот ја турка кутијата ако е до неа.
Користи breadth_first_graph_search за да најдеш најкраток пат
"""
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Robot(Problem):
    def __init__(self, initial):
        super().__init__(initial)
        self.goal = (3,3)


    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.

        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        successors = dict()

        directions = {
            "up":(0, 1),
            "down":(0, -1),
            "left":(-1, 0),
            "right":(1, 0)
        }

        rp, bp = state

        for action, (nx, ny) in directions.items():
            nrx = rp[0] + nx
            nry = rp[1] + ny

            if (nrx, nry) == bp:
                nbx = bp[0] + nx
                nby = bp[1] + ny
                if 0<= nbx < 4 and 0 <= nby < 4:
                    successors[action] = ((nrx, nry), (nbx, nby))

            elif 0<= nrx < 4 and 0 <= nry < 4:
                successors[action] = ((nrx, nry), bp)




        return successors

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба

        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата

        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """

        rp, bp = state
        return bp == self.goal


if __name__ == '__main__':
    robpos = tuple(map(int, input().split(',')))
    boxpos = tuple(map(int, input().split(',')))
    initial = (robpos, boxpos)
    robprob = Robot(initial)
    result = breadth_first_graph_search(robprob)

    if result:
        print(result.solution())
    else:
        print("No Solution!")