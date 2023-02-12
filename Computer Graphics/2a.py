import turtle as t

# Set up the turtle
t.speed(10)

# Divide the screen into four regions
t.forward(900)
t.back(1800)
t.home()
t.left(90)
t.forward(400)
t.back(800)
t.home()

# Draw a circle in the top left region
t.penup()
t.goto(-150, 150)
t.pendown()
t.circle(50)
t.penup()
t.goto(-150, 90)
t.pendown()
t.write("Circle", align="center", font=("Arial", 16, "normal"))

# Draw a rectangle in the top right region
t.penup()
t.goto(50, 150)
t.pendown()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.penup()
t.goto(100, 90)
t.pendown()
t.write("Rectangle", align="center", font=("Arial", 16, "normal"))

# Draw an eclipse in the bottom left region
t.penup()
t.goto(-200, -150)
t.pendown()
t.seth(-45)
for i in range(2):
    t.circle(100,90)
    t.circle(100//2,90)
t.penup()
t.goto(-150, -200)
t.pendown()
t.write("Ellipse", align="center", font=("Arial", 16, "normal"))

# Draw a half eclipse in the bottom right region
t.penup()
t.goto(150, -100)
t.pendown()
for i in range(1):
    t.circle(100,90)
    t.circle(100//2,90)
t.seth(-45)
t.penup()
t.goto(200, -200)
t.pendown()
t.write("Half Ellipse", align="center", font=("Arial", 16, "normal"))

# Hide the turtle and exit on click
t.ht()
t.exitonclick()
