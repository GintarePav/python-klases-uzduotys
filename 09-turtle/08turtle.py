import turtle

s = turtle.Screen()
t = turtle.Turtle() 

t.penup()
t.goto(-300, 0)
t.pendown()

penColor = ["blue", "pink", "red", "violet"]
fillColor = ["violet", "red", "pink", "blue"]

t.pen(pensize=3, speed=3)

def kvadratas():
    for i in range(4):
        t.pencolor(penColor[i % len(penColor)])
        t.fillcolor(fillColor[i % len(fillColor)])
        t.begin_fill()
        t.left(90)
        t.forward(100)
    t.end_fill

for i in range(5):
    kvadratas()
    t.penup()
    t.forward(200)
    t.pendown()