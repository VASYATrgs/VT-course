import math

class Triangle:
    def __init__(self, A, B, C):
        # Функция вычисляет длину стороны согласно координатам точек
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        # На основании соседних координат вычисляем длину стороны AB
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CA = sideLen(self.C, self.A)

    # Вычисление площади треугольника по формуле Герона
    def areaTriangle(self):
        semi_perimeter = self.perimeterTriangle() / 2

        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))

    # вычисляем периметр треугольника
    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA

    # Вычисляем высоту треугольника
    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)


treugolnik1 = Triangle((3, 5), (12, 7), (32, 40))

print(treugolnik1.areaTriangle())
print(treugolnik1.heightTriangle())
print(treugolnik1.perimeterTriangle())


import turtle

def generateSquarePoints(i):
    """ generate points for a square of any size """
    return [(i, 0), (i, i), (0, i), (0, 0)]

def drawPolyLine(start, points, lineColour="black", fillColour="white"):
    """ draw shapes using a list of coordinates """
    turtle.pencolor(lineColour)
    turtle.fillcolor(fillColour)

    turtle.penup()

    turtle.goto(start)  # make the turtle go to the start position

    turtle.pendown()
    turtle.begin_fill()

    x, y = start

    for point in points:  # go through a list of (relative) points
        dx, dy = point
        turtle.goto(x + dx, y + dy)
    turtle.goto(start)  # connect them to start to form a closed shape

    turtle.end_fill()
    turtle.penup()

if __name__ == "__main__":

    def testPolyLines():
        """ test shapes shape drawing functions """
        # A triangle
        triangleShape = [(200, 333), (100, 100), (0, 0),]
        drawPolyLine((100, -100), triangleShape, fillColour="green")


    def main():
        testPolyLines()
        turtle.done()

    main()
