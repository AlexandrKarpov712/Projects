import mymodule as m


def symbols():
    """Counting the frequency of characters in the text.

    Input arguments: text, must be string.
    Output: dictionary of symbols.
    """
    string = (m.text("Введите строку: "))
    symbols = {}

    for i in string:
        if i in symbols:
            symbols[i] += 1
        else:
            symbols[i] = 1
    print ("Количество символов в строке:\n " +  str(symbols))


def words():
    """Counting the number of words in the text.

    Input arguments: text, must be string.
    Output: word count.
    """
    str = (m.text("Введите текст: "))
    n = len(str.split())
    print(f"Количество слов в тексте: {n}")


def sentences():
    """Counting the number of sentences in the text.

    Input arguments: text, must be string.
    Output: sentences count.
    """
    text = (m.text("Введите текст: "))
    a = text.count('. ') + text.count('! ') + text.count('? ') + 1
    print(f"Количество предложений в тексте: {a}")


while True:
    next_step = m.text(
"""
Выберите задачу:
Частота вхождений символов в текст:     1
Количество слов в тексте:               2
Количество предложений в тексте:        3
Выход:                                  Enter
"""
    )
    if not next_step:
        print("Всего хорошего...")
        break
    else:
        m.choose_task_3(next_step, symbols, words, sentences)