import random
import turtle

# Set up screen
mainScreen = turtle.Screen()
mainScreen.bgcolor("green")
mainScreen.title("Penalty shootout")

# Draw penalty area
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(150, 200)
border_pen.pendown()
border_pen.setheading(90)
for side in range(3):
    if side % 2 == 0:
        border_pen.fd(80)
        border_pen.lt(90)
    else:
        border_pen.fd(300)
        border_pen.lt(90)
border_pen.penup()
border_pen.setposition(-300, -170)
border_pen.pendown()
for side in range(4):
    if side % 2 == 0:
        border_pen.fd(600)
        border_pen.lt(90)
    else:
        border_pen.fd(370)
        border_pen.lt(90)
border_pen.penup()
border_pen.setposition(-200, -60)
border_pen.pendown()
for side in range(4):
    if side % 2 == 0:
        border_pen.fd(400)
        border_pen.lt(90)
    else:
        border_pen.fd(260)
        border_pen.lt(90)
border_pen.hideturtle()

# Create the ST turtle
strikerTurtle = turtle.Turtle()
strikerTurtle.color("blue")
strikerTurtle.shape("triangle")
strikerTurtle.penup()
strikerTurtle.speed(0)
strikerTurtle.setposition(0, -120)
strikerTurtle.setheading(90)

# Create the GK turtle
goalkeeperTurtle = turtle.Turtle()
goalkeeperTurtle.color("red")
goalkeeperTurtle.shape("circle")
goalkeeperTurtle.penup()
goalkeeperTurtle.speed(0)
goalkeeperTurtle.setheading(-90)
goalkeeperTurtle.setposition(0, 200)

# Create the ball
ballTurtle = turtle.Turtle()
ballTurtle.color("yellow")
ballTurtle.shape("circle")
ballTurtle.penup()
ballTurtle.speed(0)
ballTurtle.setheading(90)
ballTurtle.shapesize(0.3, 0.3)
ballTurtle.setposition(0, -100)

# Draw the result on the bottom
conclusionTurtle = turtle.Turtle()
conclusionTurtle.color("white")
conclusionTurtle.penup()
conclusionTurtle.speed(0)
conclusionTurtle.hideturtle()

# Draw the players on each side
playersTurtle = turtle.Turtle()
playersTurtle.color("white")
playersTurtle.speed(0)
playersTurtle.hideturtle()

# Draw exit button
stopTurtle = turtle.Turtle()
stopTurtle.penup()
stopTurtle.goto(250, 350)
stopTurtle.shape("square")
stopTurtle.shapesize(2)
stopTurtle.fillcolor("red")
# stopTurtle.write("Exit")
# stoppage.write("Exit!", move=False, align="center", font=("Arial", 10, "normal"))


# Draw new players button
newPlayersTurtle = turtle.Turtle()
newPlayersTurtle.penup()
newPlayersTurtle.goto(-250, 350)
newPlayersTurtle.shape("square")
newPlayersTurtle.shapesize(3)
newPlayersTurtle.fillcolor("blue")
# newPlayersTurtle.write("Repeat")


# newplayers.write("New\n", move=False, align="center", font=("Arial", 10, "normal"))
# newplayers.write("players", move=False, align="center", font=("Arial", 10, "normal"))


def resetTheGame():
    # Reset the ST turtle
    strikerTurtle.penup()
    strikerTurtle.speed(0)
    strikerTurtle.setposition(0, -120)
    strikerTurtle.setheading(90)
    # Reset the GK turtle
    goalkeeperTurtle.penup()
    goalkeeperTurtle.speed(0)
    goalkeeperTurtle.setheading(-90)
    goalkeeperTurtle.setposition(0, 200)
    # Reset the ball
    ballTurtle.penup()
    ballTurtle.speed(0)
    ballTurtle.setheading(90)
    ballTurtle.shapesize(0.3, 0.3)
    ballTurtle.setposition(0, -100)
    playersTurtle.reset()
    playersTurtle.penup()
    playersTurtle.hideturtle()
    conclusionTurtle.reset()
    conclusionTurtle.penup()
    conclusionTurtle.hideturtle()


class GK:
    reflexes = 0
    decision = 0
    shotStopping = 0
    anticipation = 0
    balance = 0


class ST:
    decision = 0
    flair = 0
    finishing = 0
    penalty = 0
    shooting = 0
    composure = 0


def gkAttributes(goalie):
    goalie.reflexes = random.randint(1, 18)
    goalie.decision = random.randint(1, 18)
    goalie.shotStopping = random.randint(1, 18)
    goalie.anticipation = random.randint(1, 18)
    goalie.balance = random.randint(1, 18)


def stAttributes(striker):
    striker.decision = random.randint(3, 20)
    striker.flair = random.randint(3, 20)
    striker.finishing = random.randint(3, 20)
    striker.penalty = random.randint(3, 20)
    striker.shooting = random.randint(3, 20)
    striker.composure = random.randint(3, 20)


def overallGK(gk):
    overall = 25 / 100 * gk.reflexes + 18 / 100 * gk.decision + 25 / 100 * gk.shotStopping + 18 / 100 * gk.anticipation + 14 / 100 * gk.balance
    playersTurtle.setposition(-450, -60)
    playersTurtle.write("Overall GK:" + str(round(overall)), move=False, align="left", font=("Arial", 12, "normal"))
    return overall


def overallST(st):
    overall = 15 / 100 * st.decision + 5 / 100 * st.flair + 23 / 100 * st.finishing + 23 / 100 * st.penalty + 17 / 100 * st.shooting + 17 / 100 * st.composure
    playersTurtle.setposition(330, -60)
    playersTurtle.write("Overall ST:" + str(round(overall)), move=False, align="left", font=("Arial", 12, "normal"))
    return overall


def printGK(gk):
    playersTurtle.setposition(-450, 40)
    playersTurtle.write("GK Reflexes:" + str(gk.reflexes), move=False, align="left", font=("Arial", 12, "normal"))
    playersTurtle.setposition(-450, 20)
    playersTurtle.write("GK Decisions:" + str(gk.decision), move=False, align="left", font=("Arial", 12, "normal"))
    playersTurtle.setposition(-450, 0)
    playersTurtle.write("GK Shot Stopping:" + str(gk.shotStopping), move=False, align="left", font=("Arial", 12, "normal"))
    playersTurtle.setposition(-450, -20)
    playersTurtle.write("GK Anticipation:" + str(gk.anticipation), move=False, align="left", font=("Arial", 12, "normal"))
    playersTurtle.setposition(-450, -40)
    playersTurtle.write("GK Balance:" + str(gk.balance), move=False, align="left", font=("Arial", 12, "normal"))


def printST(st):
    playersTurtle.setposition(330, 60)
    playersTurtle.write("ST Decisions:" + str(st.decision), move=False, align="left", font=("Arial", 12, "normal"))
    playersTurtle.setposition(330, 40)
    playersTurtle.write("ST Flair:" + str(st.flair), move=False, align="left", font=("Arial", 12, "normal"))
    playersTurtle.setposition(330, 20)
    playersTurtle.write("ST Finishing:" + str(st.finishing), move=False, align="left", font=("Arial", 12, "normal"))
    playersTurtle.setposition(330, 0)
    playersTurtle.write("ST Penalty:" + str(st.penalty), move=False, align="left", font=("Arial", 12, "normal"))
    playersTurtle.setposition(330, -20)
    playersTurtle.write("ST Shooting" + str(st.shooting), move=False, align="left", font=("Arial", 12, "normal"))
    playersTurtle.setposition(330, -40)
    playersTurtle.write("ST Composure" + str(st.composure), move=False, align="left", font=("Arial", 12, "normal"))


def rezultat(s1, s2):
    conclusionTurtle.setposition(15, -300)
    if s1 < s2:
        caz = random.randint(1, 3)
        if caz == 1:
            goalkeeperTurtle.lt(90)
            goalkeeperTurtle.fd(120)
            ballTurtle.fd(330)
            ballTurtle.lt(90)
            ballTurtle.fd(100)
            conclusionTurtle.write("No chance for the keeper. It is a goal!", move=False, align="center",
                                   font=("Arial", 28, "normal"))
        elif caz == 2:
            goalkeeperTurtle.lt(-90)
            goalkeeperTurtle.fd(120)
            ballTurtle.fd(320)
            ballTurtle.lt(-90)
            ballTurtle.fd(120)
            conclusionTurtle.write("No chance for the keeper. It is a goal!", move=False, align="center",
                                   font=("Arial", 28, "normal"))
        else:
            ballTurtle.fd(340)
            ballTurtle.lt(90)
            ballTurtle.fd(100)
            conclusionTurtle.write("No chance for the keeper. It is a goal!", move=False, align="center",
                                   font=("Arial", 28, "normal"))
    else:
        caz = random.randint(1, 3)
        if caz == 1:
            goalkeeperTurtle.lt(-90)
            goalkeeperTurtle.fd(100)
            ballTurtle.fd(300)
            ballTurtle.lt(90)
            ballTurtle.fd(100)
            conclusionTurtle.write("What a catch from the keeper!", move=False, align="center", font=("Arial", 28, "normal"))
        elif caz == 2:
            goalkeeperTurtle.lt(90)
            goalkeeperTurtle.fd(100)
            ballTurtle.fd(300)
            ballTurtle.lt(-90)
            ballTurtle.fd(100)
            conclusionTurtle.write("What a catch from the keeper!", move=False, align="center", font=("Arial", 28, "normal"))
        else:
            ballTurtle.fd(300)
            conclusionTurtle.write("What a catch from the keeper!", move=False, align="center", font=("Arial", 28, "normal"))


def letsPlay(x, y):
    resetTheGame()
    Bob1 = GK()
    gkAttributes(Bob1)
    printGK(Bob1)
    score1 = round(overallGK(Bob1))
    Bob = ST()
    stAttributes(Bob)
    printST(Bob)
    score2 = round(overallST(Bob))
    rezultat(score1, score2)


def letsStop(x, y):
    mainScreen.bye()


newPlayersTurtle.onclick(letsPlay)
stopTurtle.onclick(letsStop)
mainScreen.mainloop()
