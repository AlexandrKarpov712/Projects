import math
from Homework_8_Shape import Shape

class Triangle(Shape):
    def __init__(self, A, B, C):
        if self.__isTriangleExists(A, B, C):
            raise Exception("Triangle doesn't exist")
        super().__init__("Triangle", 2)
        self.__points = [A, B, C]

    def __isTriangleExists(self, A, B, C):
        a = B[1] - A[1]
        b = A[0] - B[0]
        c = -a * A[0] - b * A[1]
        return a * C[0] + b * C[1] + c == 0

    def __getLength(self):
        a, b, c = self.__points
        l1 = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        l2 = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
        l3 = math.sqrt((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2)
        return l1, l2, l3

    def perimeter(self):
        l1, l2, l3 = self.__getLength()
        return l1 + l2 + l3

    def area(self):
        l1, l2, l3 = self.__getLength()
        p = self.perimeter() / 2
        return math.sqrt(p * (p - l1) * (p - l2) * (p - l3))

    
class Square(Shape):
    def __init__(self, a):
        if a <= 0:
            raise Exception("Square doesn't exist")
        super().__init__("Square", 2)
        self.__a = a

    def perimeter(self):
        return 4 * self.__a

    def area(self):
        return self.__a ** 2

    def __add__(self, other):
        return Square(self.__a + other.__a)

    def __sub__(self, other):
        if self.__a > other.__a:
            return Square(self.__a - other.__a)
        else:
            return Square(other.__a - self.__a)


class Rectangle(Shape):
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise Exception("Rectangle doesn't exist")
        super().__init__("Rectangle", 2)
        self.__a = a
        self.__b = b

    def perimeter(self):
        return 2 * (self.__a + self.__b)

    def area(self):
        return self.__a * self.__b


class Cuboid(Shape):
    def __init__(self, a, b, c):
        super().__init__("Cuboid", 3)
        if a <= 0 or b <= 0 or c <= 0:
            raise Exception("Cuboid doesn't exist")
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        return 2 * (self.__a * self.__b + self.__b * self.__c + self.__a * self.__c)

    def volume(self):
        return self.__a * self.__b * self.__c