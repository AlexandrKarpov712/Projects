import mymodule as m

def light():
    """Accepts a color as input, implements the work of a traffic light

    Input Argument: color, must be string
    Output: Returns a permitted action
    """
    color = m.text("Введите цвет: ")
    if color == 'Зеленый':
        print("Движение разрешено")
    elif color == 'Красный':
        print("Движение запрещено")
    elif color == 'Желтый':
        print("Дождитесь смены сигнала")
    else:
        print ("Такого сигнала нет")


def light_inf():
    """Accepts a color as input, implements the work of a traffic light

    Input Argument: color, must be string
    Output: Returns a permitted action
    Exit condition: string "Выход"
    """
    while 5 < 6:
        color = m.text("Введите цвет: ")
        if color == ('Выход'):
            break
        else:
            if color == 'Зеленый':   
                print("Движение разрешено")
            elif color == 'Красный':
                print("Движение запрещено")
            elif color == 'Желтый':
                print("Дождитесь смены сигнала")
            else:
                print ("Такого сигнала нет")
    
"""Task selection. Inputs: 1, 2 or Enter"""
while True:
    next_step = m.text(
"""
Выберите задачу:
Светофор:                          1
Светофор в бесконечном цикле:      2
Выход:                             Enter
"""
    )
    if not next_step:
        print("Увидимся...")
        break
    else:
        m.choose_task(next_step, light, light_inf)
