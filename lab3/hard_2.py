from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        return "Рисуем круг"


class Square(Shape):
    def draw(self):
        return "Рисуем квадрат"


class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type.lower() == "круг":
            return Circle()
        elif shape_type.lower() == "квадрат":
            return Square()
        else:
            return None


factory = ShapeFactory()

shape1 = factory.get_shape("круг")
shape2 = factory.get_shape("квадрат")

if shape1:
    print(shape1.draw())

if shape2:
    print(shape2.draw())
