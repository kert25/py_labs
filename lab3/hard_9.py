from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def description(self):
        return "Это геометрическая фигура."


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius**2)


sq = Square(5)
print(f"{sq.description()} Площадь квадрата: {sq.area()}")

cir = Circle(3)
print(f"{cir.description()} Площадь круга: {cir.area()}")
