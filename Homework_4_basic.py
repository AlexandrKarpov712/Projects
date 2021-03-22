import collections
from random import randint
import mymodule as m


def sort():
    """Bubble sort of generated list of numbers.

    Input arguments: number of elements of list, must be int.
    Output: list sorted in ascending order.
    """
    def bubble(list):
        """List sorting implementation."""
        for i in range(n - 1):
            for j in range(n - i - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]

    n = m.text("Введите количество элементов в списке: ")

    if n.isdigit(): 
        n = int(n)
        l = []
        for i in range(n):
            l.append(randint(1, 99))
        print(f"Сгенерированный список: {l}")
        bubble(l)
        print(f"Отсортированый список: {l}")
    else:
        print("Неверный ввод, введите положительное число")


def coinc():
    """Checking the list for matching elements.

    Input arguments: list1, list2. elements must be string.
    Output: match message.
    """
    list1 = [str(i) for i in m.text
        ('Введите элементы первого списка через пробел: ').split()]
    list2 = [str(i) for i in m.text
        ('Введите элементы второго списка через пробел: ').split()]
    print (f"Список 1: {str(list1)}")
    print (f"Список 2: {str(list2)}")

    if collections.Counter(list1) == collections.Counter(list2):
        
        print ("Множества элементов совпадают")
    else :
        print ("Множества не совпадают")


while True:
    next_step = m.text(
"""
Выберите задачу:
Сортировка пузырьком:                  1
Сравнение множеств списков:            2
Выход:                                 Enter
"""
    )
    if not next_step:
        print("Увидимся...")
        break
    else:
        m.choose_task(next_step, sort, coinc)