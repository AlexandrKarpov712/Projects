import mymodule as m


def fact():  
    """Calculating the factorial of a number using a function.

    Input arguments: n, must be integer.
    Output: factorial of a number.
    """
    def factorial(n):
        "Calculating the factorial of a number without recursion"
        fact = 1
        for i in range(1, n + 1):
            fact *= i

        return fact

    while True:
        try:
            n = int(m.text("""Введите натуральное число 
                для вычисления факториала: """))
        except:
            print('Еще раз')
            continue
        else:
            print(f"Факториал равен: {factorial(n)}")
            break


def bank():
    """Calculating the deposit.

    Input arguments: sum, percent, time, must be integers.
    Output: amount of money on the deposit.
    """
    def deposit(a, b, c):
        """Deposit calculation function"""
        for i in range(time):
            dep = (sum + (sum*percent)/100)

        return dep

    while True:
        try:
            sum = int(m.text("Введите размер взноса: "))
            percent = int(m.text("Введите банковский процент: "))
            time = int(m.text("Введите количество месяцев: "))
        except:
            print('Еще раз')
            continue
        else:
            print(f"""Предполагаемая сумма денег на вкладе: 
                {deposit(sum, percent, time)}""")
            break

while True:
    next_step = m.text(
"""
Выберите задачу:
Факториал:     1
Копилка:       2
Выход:         Enter
"""
    )
    if not next_step:
        print("Всего хорошего...")
        break
    else:
        m.choose_task(next_step, fact, bank)