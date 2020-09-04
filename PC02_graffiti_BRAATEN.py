# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 15:09:16 2020

@author: conno
"""
from turtle import *


panel = Screen()
w=750
h=750
panel.setup(width=w, height=h)

Turtle()
from turtle import *

image = "Bezos.gif"
panel.bgcolor("#ffa8cb")
panel.bgpic(image)

panel = Screen()

t =Turtle()

t.color("black","black")

t.penup()
t.left(90)
t.forward(160)
t.pendown()

t.begin_fill()
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.end_fill()


t.penup()
t.forward(43)
t.left(90)
t.forward(20)
t.pendown()
t.dot(27)

t.penup()
t.forward(24)
t.left(90)
t.forward(22)
t.pendown()
t.dot(27)


t.penup()
t.forward(200)
t.pendown()

t.pensize(20)
t.pencolor("yellow")

t.forward(105)

t.penup()
t.left(45)
t.forward(200)
t.pendown()

t.pencolor("green")

t.forward(40)
t.left(45)
t.forward(40)
t.left(45)
t.forward(40)
t.left(45)
t.forward(40)
t.left(45)
t.forward(40)
t.left(45)
t.forward(40)
t.left(45)
t.forward(40)
t.left(45)
t.forward(40)
t.left(45)

turtle.done()