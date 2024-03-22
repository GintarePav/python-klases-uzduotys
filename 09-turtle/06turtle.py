import turtle

s = turtle.Screen()
t = turtle.Turtle() 

s.bgcolor('purple')
t.pen(pencolor='blue', fillcolor='silver', pensize=5, speed=9)

t.begin_fill()
t.circle(90)
t.end_fill()
t.penup()
t.goto(0, -200)
t.pendown()

t.reset()

s.exitonclick()