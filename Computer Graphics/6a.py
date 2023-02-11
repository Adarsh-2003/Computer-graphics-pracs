from graphics import *
win = GraphWin("Scale Square", 600, 600)
print("Corner 1")
x1=int(input("Enter X : "))
y1=int(input("Enter Y : "))
c1=Point(x1, y1)

print("Corner 2")
x2=int(input("Enter X : "))
y2=int(input("Enter Y : "))
c2 = Point(x2, y2)

s = Rectangle(c1, c2)
s.draw(win)

sx=float(input("Scaling Factor sx : "))
sy=float(input("Scaling Factor sy : "))

x1*=sx
x2*=sx
y1*=sy
y2*=sy
c1=Point(x1, y1)
c2=Point(x2, y2)

ss=Rectangle(c1, c2)
ss.draw(win)

win.getMouse()
win.close()
