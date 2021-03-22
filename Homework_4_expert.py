"""Solving a math example.

Input arguments: signs of mathematical operations, brackets, numbers
    numbers must be integer.
Output: solved example. 
"""
import mymodule as m
import requests


def LIST(s):
    """Converting a string to a list."""
    L = []
    flag = True
    l = len(s)

    for i in range(l):
        if s[i].isdigit() and flag:
            t = ""
            j = 0

            while s[i + j].isdigit():
                t += s[i + j]
                if i + j == l - 1:
                    break
                j += 1

            L.append(t)
            flag = False
 
        elif not s[i].isdigit():
            L.append(s[i])
            flag = True
 
    return L
 
 
def POL(L):
    """Converting a list to a reverse polish notation."""
    S, L2 = [], []
    table = {"*": 1, "/": 1, "+": 0, "-": 0, "(": -1, ")": -1}

    for i in L:
        if i.isdigit():
            L2.append(i)
        elif i == "(":
            S.append(i)
        elif i == ")":
            while S[-1] != "(":
                L2.append(S.pop())
            S.pop()
        else:
            while len(S) != 0 and (table[S[-1]] >= table[i]):
                L2.append(S.pop())            
            S.append(i)
 
    while len(S) != 0:
        L2.append(S.pop())
 
    return L2
 
 
def CALC(L):
    """Calculations."""
    St = []

    for i in L:
        if i == '+':
            St.append(int(St.pop()) + int(St.pop()))
        elif i == '-':
            St.append(-int(St.pop()) + int(St.pop()))
        elif i == '*':
            St.append(int(St.pop()) * int(St.pop()))
        elif i == '/':
            a = int(St.pop())
            b = float(St.pop())
            St.append(b/a)
        else:
            St.append(i)
 
    return St[0]
 
s = m.text("Введите пример: ")
L = LIST(s)
L = POL(L)
print(f"Ответ: {int(CALC(L))}")








