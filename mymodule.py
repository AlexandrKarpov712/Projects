"""Module for the most frequently used operations in homeworks.

Classes: TreeNode
Functions: text(g), write_to_file(data, filename="./text.txt"),
    read_from_file(filename="./text.txt"), 
    choose_task(step, func1, func2), __init__(self, value),
    choose_task_3(step, func1, func2, func3)
"""

def text(g):
    """Entering data from the keyboard"""
    text = input(g)
    return text

def write_to_file(data, filename="./text.txt"):
    """Writing data to a file"""
    with open(filename, "wb") as f:
        f.write(data)

def read_from_file(filename="./text.txt"):
    """Reading data from a file"""
    with open(filename, "rb") as f:
        data = f.read()
    return data

def choose_task(step, func1, func2):
    """Task selection"""
    if step == "1":
        func1() 
    elif step == "2":
        func2()
    else:
        print("Повторите ввод...")

def choose_task_3(step, func1, func2, func3):
    """Task selection"""
    if step == "1":
        func1()  
    elif step == "2":
        func2()
    elif step == "3":
        func3()
    else:
        print("Повторите ввод...")
        
        
class TreeNode:
    """TreeNode class is used to hold Tree object data.

    Methods:    
        __init__(self, value)
        pre_order(node)
    """

    def __init__(self, value):
        """Tree Class constructor to initialize the object.
.       
        Input arguments: value - the value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None