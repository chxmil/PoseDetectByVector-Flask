import turtle
t = turtle.trutle()
t.screen.bgcolor('black')
t.pensize(2)
t.left(90)
t.backward(100)
t.speed(200)
t.shape('turtle')

def tree(i):
     if i<10:
         return
     else:
         t.forward(i)
         t.color('orenge')
         t.color('brown')
         t.left(30)
         tree(3*i/4)
         t.right(60)
         tree(3*i/4)
         t.left(30)
         t.backward(i)
         tree(100)
turtle.done()