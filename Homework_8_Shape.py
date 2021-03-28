class Shape:
    def __init__(self, name, dimension):
        if dimension < 2 or dimension > 3:
            raise Exception("Bad dimension")
        self.__name = name
        self.__dimension = dimension

    def __str__(self):
        result = '{0}D shape: {1}\n'.format(self.__dimension, self.__name)
        if self.__dimension == 2:
            result = result + 'Perimeter: {0}\nArea: {1}'.format(self.perimeter(), self.area())
        else:
            result = result + 'Area: {0}\nVolume: {1}'.format(self.area(), self.volume())
        return result

    def perimeter(self):
        if self.__dimension != 2:
            raise Exception("We can't calculate perimeter of 3D shape")
        pass

    def area(self):
        pass

    def volume(self):
        if self.__dimension != 3:
            raise Exception("We can't calculate volume of 2D shape")
        pass
