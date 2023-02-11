from graphics import*
import time
def BRESENHAMLINE(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy/float(dx)

    x, y = x1, y1
    #creating the window
    win = GraphWin('BRESENHAM LINE', 600, 480)

    #checking the slope if slope > 1
    #then interchange the role of x and y
    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    #initialisation of the initial decision parameter
    P = 2 * dy - dx

    PutPixle(win, x, y)
    for k in range(2, dx):
        if P > 0:
            y = y + 1 if y > y2 else y - 1
            P = P + 2*(dy - dx)
        else:
            P = P + 2*dy
        x = x + 1 if x < x2 else x - 1
        # delay for 0.01 secs
        time.sleep(0.01)
        print(x,y)
        PutPixle(win, x, y)
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

    BRESENHAMLINE(x1, y1, x2, y2)

if __name__=="__main__":
    main()
 
