import turtle

def triforce(t, size, order, colorchangedepth=-1, colors = ["magenta", "blue", "green"], color = "magenta"):
    changecolors = False
    if (colorchangedepth == 0):
        changecolors = True
    if order == 0:
        for i in range(0,3):
            t.color(color)
            t.forward(size)
            t.left(120)
    else:
        if(changecolors):
            color = colors[0]
        triforce(t, size/2, order-1, colorchangedepth-1, colors, color)
        t.penup()
        t.left(60)
        t.forward(size/2)
        t.right(60)
        t.pendown()
        if(changecolors):
            color = colors[1]
        triforce(t, size/2, order-1, colorchangedepth-1, colors, color)
        t.penup()
        t.right(60)
        t.forward(size/2)
        t.left(60)
        t.pendown()
        if(changecolors):
            color = colors[2]
        triforce(t, size/2, order-1, colorchangedepth-1, colors, color)
        t.penup()
        t.backward(size/2)
        t.pendown()
        
#colors = ["magenta", "blue", "green"]
wn = turtle.Screen() 
dude = turtle.Turtle()
dude.speed('fast')
triforce(dude, 100, 3, 1)

wn.mainloop()
