import turtle

sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

left_player = 0
right_player = 0

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left Player : {} Right Player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))


def lef_paddle_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def left_paddle_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)


def right_paddle_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def right_paddle_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


def display_scores():
    sketch.clear()
    sketch.write("Left Player : {} Right Player: {}".format(left_player, right_player), align="center", font=("Courier", 24, "normal"))


sc.listen()
sc.onkeypress(lef_paddle_up, "w")
sc.onkeypress(left_paddle_down, "a")
sc.onkeypress(right_paddle_up, "Up")
sc.onkeypress(right_paddle_down, "Down")
sc.update()


while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # bounces off top wall
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    # bounces off bottom wall
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    # misses the right paddle
    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player += 1
        display_scores()
        
    # misses the left paddle
    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player += 1
        display_scores()

    # right paddle collision
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < (right_pad.ycor() + 70) and ball.ycor() > (right_pad.ycor() - 70)):
        ball.setx(360)
        ball.dx*=-1

    # left paddle collision
    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < (left_pad.ycor() + 70) and ball.ycor() > (left_pad.ycor() - 70)):
        ball.setx(-360)
        ball.dx *= -1
