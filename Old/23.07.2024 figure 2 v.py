import math


class Shape:
    def calculate_area(self):
        return 0

    def calculate_perimeter(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class RightTriangle(Triangle):
    def __init__(self, leg1, leg2):
        super().__init__(leg1, leg2, math.sqrt(leg1 ** 2 + leg2 ** 2))


class ShapeList:
    def __init__(self):
        self.shape_list = []

    def add_shape(self, shape):
        self.shape_list.append(shape)

    def calculate_perimeters(self):
        perimeters = []
        for shape in self.shape_list:
            perimeters.append(shape.calculate_perimeter())
        return tuple(perimeters)

    def calculate_areas(self):
        areas = []
        for shape in self.shape_list:
            areas.append(shape.calculate_area())
        return tuple(areas)

import random
# Создаем объект класса ShapeList
shape_list = ShapeList()

# Заполняем его случайным количеством (от 2 до 10) произвольных фигур
for i in range(random.randint(2, 10)):
    shape_type = random.choice(['circle', 'rectangle', 'triangle', 'square', 'right_triangle'])
    if shape_type == 'circle':
        radius = random.randint(3, 3)
        shape = Circle(radius)
    elif shape_type == 'rectangle':
        width = random.randint(52, 555)
        height = random.randint(1, 10)
        shape = Rectangle(width, height)
    elif shape_type == 'triangle':
        side1 = random.randint(1, 12)
        side2 = random.randint(3, 15)
        side3 = random.randint(1, 16)
        shape = Triangle(side1, side2, side3)
    elif shape_type == 'square':
        side = random.randint(1, 10)
        shape = Square(side)
    else:
        leg1 = random.randint(1, 10)
        leg2 = random.randint(1, 10)
        shape = RightTriangle(leg1, leg2)
    shape_list.add_shape(shape)

# Выводим результаты работы методов calculate_perimeters() и calculate_areas() для этого объекта
print("Периметры фигур:", shape_list.calculate_perimeters())
print("Площади фигур:", shape_list.calculate_areas())