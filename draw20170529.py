import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawOAt(size,at):
    t1.fd(100)
    t1.write(t1.pos())
    t1.lt(72)
    t1.fd(100)
    t1.write(t1.pos())
    t1.lt(72)
    t1.fd(100)
    t1.write(t1.pos())
    t1.lt(72)
    t1.fd(100)
    t1.write(t1.pos())
    t1.lt(72)
    t1.fd(100)
    t1.write(t1.pos())

drawOAt(100,0)

# triangle
def drawtringleAt(size,at):
    t1.penup()
    t1.goto(300,0)
    t1.pendown()
    t1.forward(100)
    t1.write(t1.pos())
    t1.left(120)
    t1.forward(100)
    t1.write(t1.pos())
    t1.left(120)
    t1.forward(100)
    t1.write(t1.pos())
    t1.left(120)
    
drawtringleAt(100,-100)

def drawstarAt(size,at):
    t1.penup()
    t1.goto(-300,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    t1.fd(size)
    t1.lt(144)
    t1.fd(size)
    t1.lt(144)
    t1.fd(size)
    t1.lt(144)
    t1.fd(size)
    t1.lt(144)
    t1.fd(size)
    t1.lt(144)

drawstarAt(100,100)
