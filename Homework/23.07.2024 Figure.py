import math  # модуль для вычичсления квадратного уравнения

class Shape:  # основной главный класс для всех фигур
    def __init__(self):  # метод для базового конструктора
        return 0
      
    def calculate_area(self):  # метод для вычисления площади
        return 0

    def calculate_perimeter(self):  # метод для вычисления периметрам
        return 0

    def __str__(self) -> object:
        return 0
        # метод для строкового представления


class Triangle(Shape):  # подкласс для объекта Треугольник
    def __init__(self, a, b, c):  # принимаем три стороны треугольника
        super().__init__()  # вызов конструктора базового класса (для наследования и расширения, поддержки иерархии
        if not all(isinstance(side, (int)) and side > 0 for side in
                   [a, b, c]):  # проверка что стороны фигуры целые числа и положительные
            raise error("Значения сторон должны быть целыми положительными числами")
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        pp = (self.a + self.b + self.c) / 2  # вычисляем полупериметр
        return math.sqrt(pp * (pp - self.a) * (pp - self.b) * (pp - self.c))  # вычисляем площадь

    def calculate_perimeter(self):
        return self.a + self.b + self.c  # вычисляем периметр

    def __str__(self):
        return f"Стороны треугольника {self.a}, {self.b}, {self.c}"


class Rectangle(Shape):  # подкласс для объекта Прямоугольник
    def __init__(self, height, width):
        super().__init__()
        if not all(isinstance(value, (int)) and value > 0 for value in [height, width]):
            raise Error("Значения сторон должны быть целыми положительными числами")
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height * self.width)

    def __str__(self):
        return f"Стороны прямоуголника: длина {self.height}, ширина {self.width}"


class Circle(Shape):  # подкласс для объекта Круг
    def __init__(self, radius):
        super().__init__()
        if not isinstance(radius, (int)) and radius >= 0:
            raise Error("Радиус должен быть полоительным значением")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Радиус круга {self.radius}"


triangle = Triangle(4, 8, 9)
rectangle = Rectangle(12, 15)
circle = Circle(7)

print(triangle)
print(f"Площадь треугольника: {triangle.calculate_area()}, периметр треугольника: {triangle.calculate_perimeter()}")

print(rectangle)
print(f"Площадь прямоугольника: {rectangle.calculate_area()}, периметр прямоугольника: {rectangle.calculate_perimeter()}")

print(circle)
print(f"Площадь круга: {circle.calculate_area()}, периметр круга: {circle.calculate_perimeter()}")
