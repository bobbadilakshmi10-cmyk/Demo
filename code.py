'''import turtle
t=turtle.Turtle()
t.speed(5)
for _ in range(5):
    t.forward(100)
    t.right(90)
turtle.done()'''

'''import turtle
t=turtle.Turtle()
t.speed(5)
for i in range(100):
    t.circle(i*2)
    t.right(5)
turtle.done()'''

'''import turtle
t=turtle.Turtle()
t.speed(10)
colors=["red","blue","green","yellow","orange"]
for i in range(36):
    t.color(colors[i % 6])
    t.forward(200)
    t.right(170)
turtle.done()'''

import turtle 
numcircles= 120
maxradius= 300
rotationangle= 12
pensize= 3
speed= 0
colors=["red", "orange", "yellow", "lime", "cyan", "blue", "purple", "magenta"]
backgroundcolor= "black"
fillshapes= False
addcenterdot= True
centerdotcolor= "white"
centerdotsize=50
screen= turtle.Screen()
screen.bgcolor(backgroundcolor)
screen.setup(width=900, height=700)

t= turtle.Turtle()
t.speed(speed)
t.pensize(pensize)
t.hideturtle()

for i in range(numcircles):
    t.color(colors[i%len(colors)])
    if fillshapes:
        t.begin_fill()
    t.circle(i*(maxradius/numcircles))
    if fillshapes:
        t.end_fill()
    t.right(rotationangle)
if addcenterdot:
    t.penup()
    t.goto(0,0)
    t.dot(centerdotsize,centerdotcolor)
    t.dot(centerdotsize-15, "yellow")
turtle.done()

