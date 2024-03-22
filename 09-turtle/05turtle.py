import turtle

s = turtle.Screen()
t = turtle.Turtle() 

s.bgcolor('purple')
t.pencolor('pink')
t.fillcolor('cyan')
t.speed(8)
t.pensize(4)
t.begin_fill()
t.circle(90)
t.end_fill()
t.penup()
t.goto(0, -200)
t.pendown()

s.exitonclick()