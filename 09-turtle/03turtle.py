import turtle

s = turtle.Screen()
t = turtle.Turtle() 

kiek = int(input("kokiakampi breziame? "))
ilgis = int(input("kokio ilgio krastine? "))

t.color('red')
s.bgcolor('yellow')
s.title('test')
t.pensize(5)

for i in range(kiek):
    t.lt(360/kiek)
    t.fd(ilgis)

s.exitonclick()