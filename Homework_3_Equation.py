""" script for finding the roots of a quadratic equation.

Input arguments:
a, b, c must be integer, real or complex
"""
import cmath
import math
import mymodule as m

while True:
    try:
        a = float(m.text("Введите a = "))
        b = float(m.text("Введите b = "))
        c = float(m.text("Введите c = "))
        
        if a == 0:

            if b == 0:
                print("Такие коэфициенты недопустимы")
            else:
                x = -c / b
                print("x = {x}")
        
        else:
            
            D = b**2 - (4*a*c)
            print(f"Дискриминант = {D}")
        
            if D < 0:
                x1 = (-b + cmath.sqrt(D)) / (2*a)
                x2 = (-b - cmath.sqrt(D)) / (2*a)
                print(f"Корни: {x1} {x2}")
        
            elif D == 0:
                x = -b / (2*a)
                print(f"x = {x}")
        
            else:
                x1 = (-b + math.sqrt(D)) / (2*a)
                x2 = (-b - math.sqrt(D)) / (2*a)
                print(f"Корни: {x1} {x2}")
        break

    except ValueError:
        print(f"Вы ввели не число. Попробуйте снова: ")