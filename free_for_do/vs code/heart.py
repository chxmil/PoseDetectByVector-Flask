import turtle

wn = turtle.Screen()

wn.bgcolor('Black')

wn.setup( width = 250, height = 250)

turtle = turtle.Turtle()

def snowflake (size, pensize, x, y):

    """ function that draws a snowflake """

    turtle.speed(100)

    turtle.penup()

    turtle.goto(x, y)

    turtle.forward(10*size)

    turtle.left(45)

    turtle.pendown()

    turtle.color('white')


    for x in range (8):
        branch(size)
        turtle.left(45)

def branch (size):

    for z in range (3):

        for z in range (3):

            turtle.forward(10.0*size/3)
            turtle.backward(10.0*size/3)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(10.0*size/3)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(10.0*size)

snowflake(8, 6, 0, 0)

wn.exitonclick()