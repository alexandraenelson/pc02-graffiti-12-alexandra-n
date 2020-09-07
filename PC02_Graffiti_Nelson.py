#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:23:28 2020

@author: Alexandra

#Turtle Programming Challenge

"""
from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

#Creating turtle
t = Turtle()
t.pensize(10)

clear()

color(255,99,71)
t.forward(100)
up()
goto(-200,200)
down()
t.pensize(20)
circle(40)
up()
goto(200,-200)
down()
fillcolor(255, 255, 255)
dot()
dot(60)






