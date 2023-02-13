#!/usr/bin/env python3
# Animates the transition from Sierpinski Triangle tree to Fractal tree

import turtle
turtle.title('Sierpinski Triangle tree to Fractal tree transition')
turtle.setworldcoordinates(-2000,-2000,2000,2000)
screen = turtle.Screen()
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()

def sierpinski_tree(x,y,length,tilt,angle,n):
    if n==0: return
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt)
    turtle.down()
    turtle.fd(length)
    sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),angle,n-1)
    
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt+angle)
    turtle.down()
    turtle.fd(length)
    sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),angle,n-1)

    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt-angle)
    turtle.down()
    turtle.fd(length)
    sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),angle,n-1)

def animate():
    global angle
    turtle.clear()
    sierpinski_tree(0,-250,1000,90,angle,7)
    screen.update()
    angle = 120 if angle <= 20 else angle-2
    screen.ontimer(animate,50)

angle = 120
animate()
screen.mainloop()