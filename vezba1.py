"""
📝 Задача: Вук и овци
Имаме табла 3x3.
На почеток: Вукот е на позиција (0,0) (горе лево).
Овците се на позиции (2,0) и (2,2) (долу лево и долу десно).
Цел: Вукот да стигне до (2,1) (средина долу), без да стапне на полиња каде има овци.

🔑 Правила
Вукот може да се движи Горе, Долу, Лево, Десно (ако не излегува надвор од таблата).
Ако некоја акција го носи на позиција каде има овца → таа состојба не е валидна.
Почетна состојба: (0,0)
Целна состојба: (2,1)

💡 Твоја задача
Напиши класа WolfSheep(Problem) слично како кај роботот.
Во successor провери дали новата позиција е дозволена (не е овца и е во граници).
Користи breadth_first_graph_search за да најдеш најкраток пат. */
"""

from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Wolves(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid = (3,3)
        self.sheep = ((2,0), (2,2))

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
            "up":(0,1),
            "down":(0,-1),
            "left":(-1, 0),
            "right":(1,0)
        }

        for action, (nx, ny) in directions.items():
            wx, wy = state
            nwx = wx + nx
            nwy = wy + ny

            newwolfpos = (nwx, nwy)

            if 0 <= nwx < self.grid[0] and 0 <= nwy < self.grid[1]:
                if newwolfpos not in self.sheep:
                    successors[action] = newwolfpos

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
        return state == self.goal


if __name__ == '__main__':
    wolf = Wolves((0,0), (2,1))
    result = breadth_first_graph_search(wolf)

    if result:
        print(result.solution())
    else:
        print("No Solution!")