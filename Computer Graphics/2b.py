import turtle
import math
t = turtle.Turtle()
t.color("black")
t.speed(5)

def drawRectangle(t, width, height,color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()

#front of the house
t.penup()
t.goto(-150, -120)
t.pendown()
drawRectangle(t, 100, 110, "blue")

#front door
t.penup()
t.goto(-120, -120)
t.pendown()
drawRectangle(t, 40, 60, "lightgreen")

#front roof
t.penup()
t.goto(-150, -10)
t.pendown()
drawTriangle(t, 100, "red")
