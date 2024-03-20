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
striker = turtle.Turtle()
striker.color("blue")
striker.shape("triangle")
striker.penup()
striker.speed(0)
striker.setposition(0, -120)
striker.setheading(90)

# Create the GK turtle
goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setheading(-90)
goal.setposition(0, 200)

# Create the ball
ball = turtle.Turtle()
ball.color("yellow")
ball.shape("circle")
ball.penup()
ball.speed(0)
ball.setheading(90)
ball.shapesize(0.3, 0.3)
ball.setposition(0, -100)

# Draw the result on the bottom
conclusion = turtle.Turtle()
conclusion.color("white")
conclusion.penup()
conclusion.speed(0)
conclusion.hideturtle()

# Draw the players on each side
players = turtle.Turtle()
players.color("white")
players.speed(0)
players.hideturtle()

# Draw exit button
stoppage = turtle.Turtle()
stoppage.penup()
stoppage.goto(250, 350)
stoppage.shape("square")
stoppage.shapesize(2)
stoppage.fillcolor("red")
# stoppage.write("Exit!", move=False, align="center", font=("Arial", 10, "normal"))


# Draw new players button
newplayers = turtle.Turtle()
newplayers.penup()
newplayers.goto(-250, 350)
newplayers.shape("square")
newplayers.shapesize(3)
newplayers.fillcolor("blue")


# newplayers.write("New\n", move=False, align="center", font=("Arial", 10, "normal"))
# newplayers.write("players", move=False, align="center", font=("Arial", 10, "normal"))


def resetTheGame():
    # Reset the ST turtle
    striker.penup()
    striker.speed(0)
    striker.setposition(0, -120)
    striker.setheading(90)
    # Reset the GK turtle
    goal.penup()
    goal.speed(0)
    goal.setheading(-90)
    goal.setposition(0, 200)
    # Reset the ball
    ball.penup()
    ball.speed(0)
    ball.setheading(90)
    ball.shapesize(0.3, 0.3)
    ball.setposition(0, -100)
    players.reset()
    players.penup()
    players.hideturtle()
    conclusion.reset()
    conclusion.penup()
    conclusion.hideturtle()


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
    players.setposition(-450, -60)
    players.write("Overall GK:" + str(round(overall)), move=False, align="left", font=("Arial", 12, "normal"))
    return overall


def overallST(st):
    overall = 15 / 100 * st.decision + 5 / 100 * st.flair + 23 / 100 * st.finishing + 23 / 100 * st.penalty + 17 / 100 * st.shooting + 17 / 100 * st.composure
    players.setposition(330, -60)
    players.write("Overall ST:" + str(round(overall)), move=False, align="left", font=("Arial", 12, "normal"))
    return overall


def printGK(gk):
    players.setposition(-450, 40)
    players.write("GK Reflexes:" + str(gk.reflexes), move=False, align="left", font=("Arial", 12, "normal"))
    players.setposition(-450, 20)
    players.write("GK Decisions:" + str(gk.decision), move=False, align="left", font=("Arial", 12, "normal"))
    players.setposition(-450, 0)
    players.write("GK Shot Stopping:" + str(gk.shotStopping), move=False, align="left", font=("Arial", 12, "normal"))
    players.setposition(-450, -20)
    players.write("GK Anticipation:" + str(gk.anticipation), move=False, align="left", font=("Arial", 12, "normal"))
    players.setposition(-450, -40)
    players.write("GK Balance:" + str(gk.balance), move=False, align="left", font=("Arial", 12, "normal"))


def printST(st):
    players.setposition(330, 60)
    players.write("ST Decisions:" + str(st.decision), move=False, align="left", font=("Arial", 12, "normal"))
    players.setposition(330, 40)
    players.write("ST Flair:" + str(st.flair), move=False, align="left", font=("Arial", 12, "normal"))
    players.setposition(330, 20)
    players.write("ST Finishing:" + str(st.finishing), move=False, align="left", font=("Arial", 12, "normal"))
    players.setposition(330, 0)
    players.write("ST Penalty:" + str(st.penalty), move=False, align="left", font=("Arial", 12, "normal"))
    players.setposition(330, -20)
    players.write("ST Shooting" + str(st.shooting), move=False, align="left", font=("Arial", 12, "normal"))
    players.setposition(330, -40)
    players.write("ST Composure" + str(st.composure), move=False, align="left", font=("Arial", 12, "normal"))


def rezultat(s1, s2):
    conclusion.setposition(15, -300)
    if s1 < s2:
        caz = random.randint(1, 3)
        if caz == 1:
            goal.lt(90)
            goal.fd(120)
            ball.fd(330)
            ball.lt(90)
            ball.fd(100)
            conclusion.write("No chance for the keeper. It is a goal!", move=False, align="center",
                             font=("Arial", 28, "normal"))
        elif caz == 2:
            goal.lt(-90)
            goal.fd(120)
            ball.fd(320)
            ball.lt(-90)
            ball.fd(120)
            conclusion.write("No chance for the keeper. It is a goal!", move=False, align="center",
                             font=("Arial", 28, "normal"))
        else:
            ball.fd(340)
            ball.lt(90)
            ball.fd(100)
            conclusion.write("No chance for the keeper. It is a goal!", move=False, align="center",
                             font=("Arial", 28, "normal"))
    else:
        caz = random.randint(1, 3)
        if caz == 1:
            goal.lt(-90)
            goal.fd(100)
            ball.fd(300)
            ball.lt(90)
            ball.fd(100)
            conclusion.write("What a catch from the keeper!", move=False, align="center", font=("Arial", 28, "normal"))
        elif caz == 2:
            goal.lt(90)
            goal.fd(100)
            ball.fd(300)
            ball.lt(-90)
            ball.fd(100)
            conclusion.write("What a catch from the keeper!", move=False, align="center", font=("Arial", 28, "normal"))
        else:
            ball.fd(300)
            conclusion.write("What a catch from the keeper!", move=False, align="center", font=("Arial", 28, "normal"))


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


newplayers.onclick(letsPlay)
stoppage.onclick(letsStop)
mainScreen.mainloop()
