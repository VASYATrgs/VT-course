lst = [((3, 2), (6, 7), (0, 12))]

result = [(i1, i2) for i1, e1 in enumerate(lst) for i2, e2 in enumerate(e1) if e2 in ['w', 'W']]
print(result)


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
