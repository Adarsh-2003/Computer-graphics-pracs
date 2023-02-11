import turtle as t
import random
t.forward(900)
t.back(1800)
t.home()
t.left(90)
t.forward(400)
t.back(800)
t.home()

#t.penup()
x=random.randrange(10,201)
y=random.randrange(10,201)
t.goto(x,y)

#t.penup()
t.circle(50)
t.write(x,font=("arial",12,"normal"))
t.forward(40)
t.write(y,font=("arial",12,"normal"))
t.forward(40)