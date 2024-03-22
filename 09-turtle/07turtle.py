import turtle

s = turtle.Screen()
t = turtle.Turtle() 

s.bgcolor('black')
colors1 = ['aqua', 'red', 'blue', 'pink']
colors2 = ['red', 'blue', 'cyan', 'violet']
t.pen(pensize=5, speed=9)

for i in range(15, 2, -1):
    t.pencolor(colors1[(i-3) % len(colors1)])
    t.fillcolor(colors2[(i-3) % len(colors1)])
    t.begin_fill()
    for j in range(i):
        t.left(360/i)
        t.forward(50)
    t.end_fill()
s.exitonclick()