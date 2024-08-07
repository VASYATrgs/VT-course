


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


from tkinter import *

root = Tk()
root.title("METANIT.COM")
root.geometry("300x250")

canvas = Canvas(bg="white", width=250, height=200)
canvas.pack(anchor=CENTER, expand=1)

canvas.create_rectangle(10, 0, 200, 60, fill="#80CBC4", outline="#004D40")

root.mainloop()