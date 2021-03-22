""" script for finding the roots of a quadratic equation.

Input arguments:
a, b, c must be integer or real
"""
import math
import mymodule as m
   
a = float(m.text("Введите a = "))
b = float(m.text("Введите b = "))
c = float(m.text("Введите c = "))
d = float(m.text("Введите c = "))

if a == 0:
    x = -c / b
    print("x = ", x)

else:
    D = b**2 - (4*a*c)
    print("Дискриминант = ", D)
    
    if D < 0:
        print("Корней нет")
    elif D == 0:
        x = -b / (2 * a)
        print("x = ", x)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Корни: ")
        print(x1)
        print(x2)

