import Homework_8_decorators
from Homework_8_Shapes import Triangle
from Homework_8_Shapes import Rectangle
from Homework_8_Shapes import Square
from Homework_8_Shapes import Cuboid

t = Triangle((1, 1), (4, 1), (1, 5))
print(t)
r = Rectangle(3, 5)
print(r)
c = Cuboid(2, 3, 4)
print(c)
s1 = Square(3)
s2 = Square(6)
print(s1 - s2)
print(Homework_8_decorators.factorial(5))