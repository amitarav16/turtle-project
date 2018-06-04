# graphics game
import turtle
import math
import random

#setup screen
wn = turtle.Screen()
wn.bgcolor("light green")
wn.tracer(3)
wn.bgpic("sa.gif")
#borders
border = turtle.Turtle()
border.penup()
border.setpos(-500,-300)
border.pendown()
border.pensize(5)
border.forward(1000)
border.left(90)
border.forward(600)
border.left(90)
border.forward(1000)
border.left(90)
border.forward(600)
border.left(90)
# player a
a = turtle.Turtle()
a.color("purple")
a.shape("triangle")
a.penup()
a.speed(0)
#create multiple goal
maxgoal = 6
goals = []
for i in range(maxgoal):
    #create goal
    goals.append(turtle.Turtle())
    goals[i].color("red")
    goals[i].shape("circle")
    goals[i].penup()
    goals[i].speed(0)
    goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
#setting speed
speed = 1
# def func to move
def turnleft():
    a.left(30)
def turnright():
    a.right(30)
def increasespeed():
    global speed
    speed += 1
def collision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False

# bind keys
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
while True:
    a.forward(speed)
    #boundary
    if a.xcor() > 500 or a.xcor() < -500:
        a.right(180)
    if a.ycor() > 300 or a.ycor() < -300:
        a.right(180)
    #move the goal
    for i in range(maxgoal):
        goals[i].forward(4)
        # boundary check for goal
        if goals[i].xcor() > 490 or goals[i].xcor() < -490:
            goals[i].right(180)
        if goals[i].ycor() > 290 or goals[i].ycor() < -290:
            goals[i].right(180)
            # collision check
        if collision(a, goals[i]):
            goals[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[i].right(random.randint(0, 360))

turtle.done()