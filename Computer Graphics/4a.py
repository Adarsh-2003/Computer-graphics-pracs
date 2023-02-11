from graphics import*
import time

def dda(x1, y1, x2, y2):
    """DDA LINE DRAWING ALGORITHM"""

  #creating the window
    winx=600
    winy=600
    win = GraphWin('DDA LINE', winx, winy)

  #measure the distance
    dx= abs(x2 - x1)
    dy= abs(y2 - y1)

  #check the start & end point
    if(x1 > x2):
        x , y = x2 , y2
        xend = x1
    else:
        x , y = x1 , y1
        xend= x2

    #calculaye the steps
    steps= dx if (dx > dy) else dy

    #calculate the increment for x & y
    x_inc = dx / steps
    y_inc = dy / steps

    # loop for making the line based on point
    PutPixle(win, x, y)
    while True:
        x = x + x_inc
        y = y - y_inc
        print(x,y)
        time.sleep(0.01)
        PutPixle(win, round(x),round(y))
        if (x > xend): break

    win.getMouse()
    win.close()

def PutPixle(win, x, y):
    """ PLOT A PIXLE IN THE WINDOW AT POINT(x,y) """
    pt= Point(x, y)
    pt.draw(win)

def main():
    x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start y: "))
    x2 = int(input("Enter Start X: "))
    y2 = int(input("Enter Start Y: "))

    dda(x1, y1, x2, y2)

if __name__=="__main__":
    main()
