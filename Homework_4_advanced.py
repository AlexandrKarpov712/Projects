import mymodule as m

def del_same():
    """Removes duplicate items from the list.

    Input arguments: list of elements.
    Output: list without duplicates.
    """
    l = [str(i) for i 
        in m.text('Введите элементы списка через пробел: ').split()]
    print(f"Первоначальный список : {str(l)}")
    print (f"Список без повторений: {list(set(l))}")


def brackets():
    """Checking for correct parentheses in text.
    
    Input arguments: text with brackets, must be string.
    Output: correctness message.
    """
    text = [str(i) for i in m.text('Введите текст со скобками: ')]
    bkt_open = ["[","{","(","<"]
    bkt_close = ["]","}",")",">"]
    stack = []

    for i in text:
        if i in bkt_open:
            stack.append(i)
        elif i in bkt_close:
            tmp = bkt_close.index(i)

            if ((len(stack) > 0) and
                (bkt_open[tmp] == stack[len(stack)-1])):
                stack.pop()
            else:
                print("Скобки расставлены некорректно")

    if len(stack) == 0:
        print("Скобки расставлены корректно")

while True:
    next_step = m.text(
"""
Выберите задачу:
Удаление встречающихся элементов:      1
Проверка скобок:                       2
Выход:                                 Enter
"""
    )
    if not next_step:
        print("Увидимся...")
        break
    else:
        m.choose_task(next_step, del_same, brackets)