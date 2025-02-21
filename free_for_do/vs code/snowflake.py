import turtle

def draw_star(turtle, size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

wn = turtle.Screen()
wn.bgcolor("black")

star = turtle.Turtle()
star.color("white")
star.pensize(3)

# 1
star.penup()
star.goto(-80, 60)
star.pendown()
draw_star(star, 20)

# 2
star.penup()
star.goto(80, 60)
star.pendown()
draw_star(star, 20)

# 3
star.penup()
star.goto(-120, 0)
star.pendown()
draw_star(star, 20)

# 4
star.penup()
star.goto(-40, 0)
star.pendown()
draw_star(star, 20)

# 5
star.penup()
star.goto(40, 0)
star.pendown()
draw_star(star, 20)

# 6
star.penup()
star.goto(120, 0)
star.pendown()
draw_star(star, 20)

# 7
star.penup()
star.goto(120, 0)
star.pendown()
draw_star(star, 20)

# 8
star.penup()
star.goto(120, 0)
star.pendown()
draw_star(star, 20)

# 9
star.penup()
star.goto(120, 0)
star.pendown()
draw_star(star, 20)

# 10
star.penup()
star.goto(120, 0)
star.pendown()
draw_star(star, 20)

# 11
star.penup()
star.goto(120, 0)
star.pendown()
draw_star(star, 20)

# 12
star.penup()
star.goto(120, 0)
star.pendown()
draw_star(star, 20)

# 13
star.penup()
star.goto(120, 0)
star.pendown()
draw_star(star, 20)

# 14
star.penup()
star.goto(120, 0)
star.pendown()
draw_star(star, 20)

wn.exitonclick()
