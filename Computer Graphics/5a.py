from graphics import*

def MidPointCircleDraw(x_centre, y_centre, r):
    win = GraphWin("Mid-Point Circle", 600, 480)
    X = r
    Y = 0

    print("(", x + x_centre, ", ", y + y_centre, ")",sep = "", end = "")


    if(r > 0) :
        print("(", x + x_centre, ", ", -y + y_centre, ")",sep = "", end = "")
        print("(", y + x_centre, ", ", x + y_centre, ")",sep = "", end = "")
        print("(", -y + x_centre, ", ",      x + y_centre, ")",sep = "")

    P = 1- r
    while x > y:
        y +=1

        if P<= 0:
            P = P + 2 * y + 1
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        if(x < y):
            break

        x1 = x + x_centre
        y1 = y + y_centre

        x2 = -x + x_centre
        y2 = y + y_centre

        x3 = x + x_centre
        y3 = -y + y_centre

        x4 = -x + x_centre
        y4 = -y + y_centre

        PutPixle(win, x1,y1)
        PutPixle(win, x2,y2)
        PutPixle(win, x3,y3)
        PutPixle(win, x4,y4)
        print("(", x1, ",", y1,")", sep = "", end = "")
        print("(", x2, ",", y2,")", sep = "", end = "")
        print("(", x3, ",", y3,")", sep = "", end = "")
        print("(", x4, ",", y4,")", sep = "", end = "")

        if x != y:
            x1 = y + x_centre
            y1 = x + y_centre

            x2 = -y + x_centre
            y2 = x + y_centre

            x3 = y + x_centre
            y3 = -x + y_centre

            x4 = -y + x_centre
            y4 = -x + y_centre

            PutPixle(win, x1,y1)
            PutPixle(win, x2,y2)
            PutPixle(win, x3,y3)
            PutPixle(win, x4,y4)

            print("(", x1, ",", y1,")", sep = "", end = "")
            print("(", x2, ",", y2,")", sep = "", end = "")
            print("(", x3, ",", y3,")", sep = "", end = "")
            print("(", x4, ",", y4,")", sep = "", end = "")

        win.getMouse()
        win.close()

def PutPixle(win, x, y):
    pt = Point(x,y)
    pt.draw(win)

if __name__ == '__main__':
    x =int(input("Enter Center coordinates x value: "))
    y =int(input("Enter Center coordinates y value: "))
    r = int(input("Enter Radius: "))
    MidPointCircleDraw(x, y, r)
    
    

        
        
