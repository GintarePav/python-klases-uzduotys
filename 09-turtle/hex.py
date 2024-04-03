import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(0)


def hex():
    for i in range(6):
        t.left(360/6)
        t.forward(100)

for i in range(6):
    hex()
    t.rt(60)
    t.fd(100)

s.exitonclick()