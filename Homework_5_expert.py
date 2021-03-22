import mymodule as m


def fact():
    """Calculating the factorial of a number using a recursion.

    Input arguments: n, must be integer.
    Output: factorial of a number.
    """
    n = int(m.text
        ('Введите натуральное число для вычисления факториала: '))
    fact = lambda n: 1 if  n < 1 else n * fact(n-1)
    print(fact(n))


def calculate():
    """Сalculator for basic operations.

    Input arguments: x, first number, must be float,
        step - operation and operand without space, sting.
    Output: the calculation result.
    """
    print("""
        Возможные операции:
        +    сложение
        -    вычитание
        *    умножение
        /    деление
        ^    возведение в степень
        %    получение остатка от деления
        """
    )

    def calc(a, b, operation):
        """Receives two operands and an operation, 
            calls an operation on the operands"""


        def add(a1, b1):
            """Returns the result of adding operands"""
            return a1 + b1
            
        def remove(a1, b1):
            """Returns the result of subtraction operands"""
            return a1 - b1

        def multiply(a1, b1):
            """Returns the result of multiplication operands"""
            return a1 * b1

        def divide(a1, b1):
            """Returns the result of division operands"""
            return (a1) / (b1)

        def exp(a1, b1):
            """Returns the result of exponentiation operands"""
            return a1 ** b1

        def res(a1, b1):
            """Returns the remainder of the division operands"""
            return a1 % b1

        selector = {
            "+": add,
            "-": remove,
            "*": multiply,
            "/": divide,
            "^": exp,
            "%": res
            }
        

        return selector[operation](a,b)

    try:
        x = float(m.text('Введите первое число: '))
    except ValueError:
        print("Вы ввели не число. Попробуйте еще раз ")
        
    else:

        while True: 
            
            step = (m.text('(Enter - выход) \
                Введите операцию и операнд:  '))
            
            if not step:
                print("Всего хорошего...")
                break
        
            else: 
                try:
                    oprtn = (step[0])
                    y = float(step[1:])

                except ValueError:
                    print("""Нерпавильный ввод. 
                        Введите 'операция''операнд'""")

                except ZeroDivisionError:
                    print("Деление на ноль")

                else:
                    print(f"""Результат: {x} {oprtn} {y} = 
                        {calc(x, y, oprtn)} Продолжаем считать? """)
                    x = calc(x, y, oprtn)

while True:
    next_step = m.text(
"""
Выберите задачу:
Факториал:         1
Калькулятор:       2
Выход:             Enter
"""
    )
    if not next_step:
        print("Всего хорошего...")
        break
    else:
        m.choose_task(next_step, fact, calculate)
        