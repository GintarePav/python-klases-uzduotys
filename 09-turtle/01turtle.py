import turtle
s = turtle.Screen() #ekranas, popieriaus lapas
t = turtle.Turtle() #zymeklis, piestukas
t.speed(1) # 1 labai letas, 5 normalus, 10 greitas, 0 pats greiciausias
t.right(90) #laipsniai, arba t.rt(90)
t.forward(100) #keliauja nurodytus zinksnius
t.left(120) #laipsniai
t.backward(100) #zingsniai
t.home() #pradines koordinates
t.clear() #isvalo
t.goto(120, -50)
t.color('blue') #spalva
s.exitonclick() #uzdarys langa