import turtle

s = turtle.Screen()
t = turtle.Turtle() 

t.color('green')

for i in range(3, 13):
    for j in range(i):
        t.left(360/i)
        t.forward(50)

s.exitonclick()