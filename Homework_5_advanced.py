import math
import mymodule as m
from collections import Counter


def fact():
    """Calculating factorial without using recursion.

    Input arguments: n, must be an integer.
    Output: factorial of number n.
    """
    n = int(m.text
        ('Введите натуральное число для вычисления факториала: '))
    print((lambda a: math.factorial(a))(n))


def freq():
    """Counting the frequency of characters in the text.

    Input arguments: text, must be string.
    Output: dictionary of symbols.
    """
    text = (m.text("Введите строку: "))
    print((lambda res: Counter(res))(text))

while True:
    next_step = m.text(
"""
Выберите задачу:
Факториал:           1
Частота символов:    2
Выход:               Enter
"""
    )
    if not next_step:
        print("Увидимся...")
        break
    else:
        m.choose_task(next_step, fact, freq)








