#Program to create a house like figure and perform the following operations.
#i.Scaling about the origin followed by translation.
#ii. Scaling with reference to an arbitrary point.
#iii. Reflect about the line y = mx + c.
from graphics import *
win = GraphWin("House", 600,600)
lst1=[200,200,300,300]
line1=[200,200,250,150]
line2=[250,150,300,200]

def drawHouse():
    c1=Point(lst1[0],lst1[1])

    #x2=300
    #y2=300
    c2=Point(lst1[2],lst1[3])

    s = Rectangle(c1, c2)
    s.draw(win)

    pt1 = Point(line1[0],line1[1])
    pt2 = Point(line1[2],line1[3])
    line = Line(pt1, pt2)
    line.draw(win)
    pt3 = Point(line2[0],line2[1])
    pt4 = Point(line2[2],line2[3])
    line = Line(pt3, pt4)
    line.draw(win)

print("Before Scaling")
drawHouse()

print("After Scaling")

l1=len(lst1)
for i in range(l1):
    lst1[i]*=2

l2=len(line1)
for i in range (l2):
    line1[i]*=2

l3=len(line2)
for i in range(l3):
    line2[i]*=2

drawHouse()
