import turtle
#draw a ninja
ninja = turtle.Turtle()
ninja.speed(10)

for i in range(45):
    ninja.forward(25)
    ninja.right(10)
    ninja.forward(5)
    ninja.left(15)
    ninja.forward(12.5)
    ninja.right(7.5)

ninja.penup()
ninja.setposition(0, 0)
ninja.pendown()

ninja.right(2)

turtle.done()
