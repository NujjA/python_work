import turtle

def koch_old(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:          # The base case is just a straight line
        t.forward(size)
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

def tornline(t, order, size, degree):
    if order == 0:
        t.forward(size)
    else:
        tornline(t, order-1, size/2, degree)
        t.right(90-degree)
        tornline(t, order-1, size/2, degree)
        t.right(180+ (2*degree))
        tornline(t, order-1, size/2, degree)
        t.right(90-degree)
        tornline(t, order-1, size/2, degree)
        
def csquare(t, order, size, degree):
    for i in range(0,4):
        tornline(t, order, size, degree)
        t.right(90)
        

wn = turtle.Screen() 
dude = turtle.Turtle()
dude.speed('fast')
csquare(dude, 4, 100, 10)

wn.mainloop()
           

