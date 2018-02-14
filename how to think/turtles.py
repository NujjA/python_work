import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex

colorvar = "blue"
alex.color(colorvar)

alex.penup()
size = 100
line = 15

for i in range(12):
    alex.forward(size)
    alex.pendown()
    alex.forward(line)
    alex.penup()
    alex.forward(line)
    alex.stamp()
    alex.backward(size + line + line)
    alex.right(30)

wn.mainloop()             # Wait for user to close window
