"""
📝 Задача: Автомобил на пат
Имаме автомобил кој се движи по еднодимензионален пат (линија со позиции од 0 до 10).
Почетна состојба: автомобилот е на позиција 0.
Целна состојба: автомобилот треба да стигне до позиција 7.
Дозволени акции:
Напред за 1 чекор → +1
Напред за 2 чекори → +2
Назад за 1 чекор → -1

🔑 Правила
Автомобилот не смее да излезе надвор од патот (позиции мора да бидат во опсег 0–10).
Почетна состојба: (0)
Целна состојба: (7)
💡 Твоја задача

Напиши класа CarPath(Problem) која ќе го моделира проблемот.
Во successor генерирај ги сите можни нови позиции според акциите.
Користи breadth_first_graph_search за да најдеш најкраток пат од 0 до 7.
"""
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class CarPath(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)


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
            "twostep":2,
            "onestep":1,
            "stepback":-1
        }

        for action, value in directions.items():
            position = state
            newposition = position + value

            if 0 <= newposition <= 10:
                successors[action] = newposition


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
    start = int(input())
    finish = int(input())
    car = CarPath(start, finish)
    result = breadth_first_graph_search(car)

    if result:
        print(result.solution())
    else:
        print("No Solution!")