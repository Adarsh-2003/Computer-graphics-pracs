from graphics import *
 
WIDTH, HEIGHT = 800, 400
RADIUS = 40
 
def main():
   win = GraphWin('Experiment 2-3', WIDTH, HEIGHT)
 
   st = Rectangle(Point(75, 25), Point(145, 50))
   st.draw(win)
   st.setFill('red')
   s = Rectangle(Point(50, 50), Point(175, 100))
   s.draw(win)
   s.setFill('blue')
   c1 = Circle(Point(75, 100), 10)
   c1.draw(win)
   c1.setFill('black')
   c2 = Circle(Point(145, 100), 10)
   c2.draw(win)
   c2.setFill('black')
   l = Line(Point(0,112), Point(WIDTH, 112))
   l.draw(win)
   while s.getCenter().getX() < WIDTH - RADIUS:
       s.move(1, 0)
       st.move(1,0)
       c1.move(1,0)
       c2.move(1,0)
   win.getMouse()
   win.close()
main()
