﻿import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def giyukAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)



def nieunAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.rt(90)
    t1.fd(size)
    t1.lt(90)
    t1.fd(size)


def miAt(x,y,size):
    giyukAt(x,y,size)
    t1.penup()
    t1.goto(x,y)
    t1.lt(90)
    t1.pendown()
    nieunAt(x,y,size)

miAt(-100,100,100)