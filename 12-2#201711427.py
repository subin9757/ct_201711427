import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.penup()
t1.goto(300,0)
t1.pendown()

def drawTriangle(size):
  for i in range(0,3):
    t1.forward(size)
    t1.right(120)

def drawTriangleAt(x, y, size):
  t1.penup()
  t1.goto(x, y)
  t1.pendown()
  drawTriangle(size)

drawTriangleAt(0,0,50)

def drawStar(size):
  for i in range(0,5):
    t1.forward(size)
    t1.right(144)

def drawStarAt(x, y, size):
  t1.penup()
  t1.goto(x, y)
  t1.pendown()
  drawStar(size)


drawStarAt(-100,-100,50)

def drawSquare(size):
  for i in range(0, 4):
    t1.forward(size)
    t1.right(90)

def drawSquareAt(x, y, size):
  t1.penup()
  t1.goto(x, y)
  t1.pendown()
  drawSquare(size)
    
drawSquareAt(100,100,50)
