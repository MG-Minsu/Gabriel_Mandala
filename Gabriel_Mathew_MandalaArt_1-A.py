from turtle  import *
import turtle
loadWindow = turtle.Screen()
turtle.speed(100)

color('dark blue')
for i in range(50):

	turtle.circle(60) #133
	turtle.left(50)

bgcolor('black')

penup()
goto(-40,-115)
pendown()
turtle.hideturtle()
turtle.circle(120)

penup()
goto(-102,-38)
pendown()

for i in range (60):
        color('#F8B400')
        circle(140-i, 100)
        left(100)
        circle(140-i, 100)
        left(100)

penup()
goto(0,0)
pendown()

color('green')
for i in range (100):
        circle(120-i, 90)
        left(90)
        circle(120-i, 90)
        left(18)


color('#F8B400')
def out():
    for i in range (5):
            circle(50-i, 90)
            left(90)
            circle(50-i, 90)
            left(18)
penup()
goto(0,-300)
pendown()

for i in range (5):
    out()
    left(100)

penup()
goto(0,300)
pendown()

for i in range (5):
    out()
    left(100)

penup()
goto(300,0)
pendown()

for i in range (5):
    out()
    left(100)

penup()
goto(-300,0)
pendown()

for i in range (5):
    out()
    left(100)

color('black')
penup()
goto(260,-150)
pendown()
turtle.circle(300)


penup()
goto(0,0)
pendown()
color('#B20600')
for i in range(50):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)

bgcolor('#B20600')
turtle.exitonclick()
