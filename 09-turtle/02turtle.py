import turtle

s = turtle.Screen()
t = turtle.Turtle() 
t.speed(5)
t.color('blue')
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.clear()

for i in range(4):
    t.lt(90)
    t.fd(100)

t.clear()
t.color('red')

for i in range(5):
    t.lt(360/5)
    t.fd(100)

s.exitonclick()