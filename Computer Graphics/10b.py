from graphics import *
def drawFace(center, size, win):
   face = Circle(Point(100, 50), 30)
   face.setFill("yellow")
   face.draw(win)
   Leye = Circle(Point(90, 60), 5)
   Leye.setFill("black")
   Leye.draw(win)
   Reye = Leye.clone()
   Reye.move(20, 0)
   Reye.draw(win)
   # arc = Arc( Point(100, 100),Point(80, 50), 180)
   # arc.setFill("black")
   # arc.draw(win)
   mouth1 = Line(Point(80, 40), Point(90, 30))
   mouth1.draw(win)
   mouth2 = Line(Point(90, 30), Point(110, 30))
   mouth2.draw(win)
   mouth3 = Line(Point(110, 30), Point(120, 40))
   mouth3.draw(win)
   # mouth = Oval(Point(120, 55), Point(105, 55)) # set corners of bounding box
   # mouth.setFill('red')
   # mouth.draw(win)
 
 
def main():
   win = GraphWin("Smiley Faces", 200, 200)
   win.setBackground("light blue")
   win.setCoords(0, 0, 200, 200)
  
   size = 0
   center = Point(150, 100)
   drawFace(center, size, win)
 
 
   # message = Text(Point(100, 10), "Click anywhere to Quit")
   # message.draw(win)
   win.getMouse()
   win.close()
 
main()
