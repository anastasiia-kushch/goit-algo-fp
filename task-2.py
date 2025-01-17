import turtle
screen = turtle.Screen() 
screen.setup(320, 320)   

TTL = turtle.Turtle()
TTL.speed(0) 
TTL.color("brown") 
TTL.pensize(1) 

TTL.penup() 
TTL.setposition(0, -100)
TTL.pendown() 
TTL.hideturtle()
TTL.setheading(90)

def treeFractal(TTL, recursionLevel, branchLength, branchReduction, angle):
  if recursionLevel == 0:
    TTL.fd(0)
  else:
    branchLength = branchLength - branchReduction
    TTL.forward(branchLength)
    TTL.left(angle)
    treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
    TTL.right(angle * 2)
    treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
    TTL.left(angle)
    TTL.backward(branchLength)

treeFractal(TTL, 8, 50, 5, 45)

screen.exitonclick()