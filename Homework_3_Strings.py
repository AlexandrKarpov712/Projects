import mymodule as m

def freq_symb():
    """Determine the frequency of using all characters in the text.

    Input Arguments: string.
    Output: dictionary with symbols and their number in the text.
    """
    string = (m.text("Введите строку: "))
    symbols = {}

    for i in string:
        if i in symbols:
            symbols[i] += 1
        else:
            symbols[i] = 1
    print ("Количество символов в строке:\n " +  str(symbols))


def freq_numb():
    """The frequency of using digits in a range of numbers.
    
    Input arguments: a, b are integer.
    Output: dictionary with digits and their number in the text.
    """
    while True:
        try:
            a = int(m.text("Введите первое число: "))
            b = int(m.text("Введите последнее число: "))
        
            symbols = {}
            string = "".join(map(str, range(a, b)))
        
            for i in string:
                if i in symbols:
                    symbols[i] += 1
                else:
                    symbols[i] = 1
            print("Количество цифр в диапазоне:\n " + str(symbols))
            break

        except ValueError:    
            print("Вы ввели не число. Попробуйте снова: ")
    

def fizz_buzz():
    """FizzBuzz 0 to 100.

    Prints numbers or words.
    """
    for i in range(0,101):
        if i % 15 == 0:
            print(f"FizzBuzz")
        elif i % 3 == 0:
            print(f"Fizz")
        elif i % 5 == 0:
            print(f"Buzz")
        else:
            print(i)


while True:
    next_step = m.text(
"""
Выберите задачу:
Частота символов:     1
Частота цифр:         2
FizzBuzz:             3
Выход:                Enter
"""
    )
    if not next_step:
        print("Увидимся...")
        break
    else:
        m.choose_task_3(next_step, freq_symb, freq_numb, fizz_buzz)