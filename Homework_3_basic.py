"""The script performs simple arithmetic calculations

Input arguments: operation name, strings:
    'Простое число', 'НОД' or 'НОК'
Args n, a, b, x, y are integers
"""
import math
import mymodule as m

while True:
    task = m.text("Введите задание: ")
    if  task.isdigit():
        print(f"Неправильный ввод, попробуйте снова")
    else:
        if task == ('Выход'):
            break
        else:

            if task == 'Простое число':
            # Простое число
                n = int(m.text("Введите число: "))
                k = 0
                for i in range(2, n):  
                    if (n % i == 0):
                        k = k + 1
                if (k > 1): 
                    print(f"Число {n} не является простым")
                else:
                    print(f"Число {n} простое")

            elif task == 'НОД':
            # НОД
                a = int(m.text("Введите первое число: "))
                b = int(m.text("Введите второе число: "))
                while a != 0 and b != 0:
                    if a > b:
                        a = a % b
                    else:
                        b = b % a
                print (f"Наибольший общий делитель = {a + b}")

            elif task == 'НОК':
                # НОК
                def NOK(a, b):
                    """ Returns the least common multiple of two numbers"""
                    return (a * b) // math.gcd(a, b)

                x = int(m.text(f"Введите первое число: "))
                y = int(m.text(f"Введите второе число: "))
                print(f"Наименьшее общее кратное =  {NOK(x, y)}")

            else:
                print(f'Такого задания нет')