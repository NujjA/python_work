import turtle

def make_window(colr, ttle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w
    
def make_turtle(colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def drawpattern(turtname, turnangle, linesize, increaseby, numsides):
    currentline = linesize
    for i in range(numsides):
        drawside(turtname, turnangle, currentline)
        currentline += increaseby

def drawside(turtname, turnangle, linesize):
    turtname.forward(linesize)
    turtname.right(turnangle)

############
wn = make_window("lightgreen", "Tess makes a shape")
tess = make_turtle("hotpink", 5)
numsides = 30
turnangle = 95
linesize = 10
increaseby = 5
drawpattern(tess, turnangle, linesize, increaseby, numsides)
wn.mainloop()
