from turtle import *
from random import randint

screen = Screen()
screen.setup(400, 360)
screen.title("Let's Race Turtles")

speed(0)
penup() # lift pen so next statement does NOT draw
goto(-140, 140) # goto absolute position in the window

# racing track

for step in range(15):
    write(step, align = 'center') # write the number between 1 and 15
    right(90) # turn right 90 degrees

    for num in range(8):
        penup() # lift pen so next statement does NOT draw
        forward(10) # forward 10 pixels
        pendown() # put pen down so next statement does draw
        forward(10)

    penup() # lift pen so next statement does NOT draw
    backward(160) # backwards 160 pixels
    left(90) # left 90 degrees
    forward(20) # forwards 20 pixels
hideturtle()

# first player details
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')

# first player proceeds to racing track
player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()

# second player details
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')

# second player enters the racing track
player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()

# third player details
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')

# third player enters the racing track
player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()

# fourth player details
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('orange')

# fourth player enters the racing track
player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()

# turtles run at random speeds
for turn in range(100):
    player_1.forward(randint(1, 5))
    player_2.forward(randint(1, 5))
    player_3.forward(randint(1, 5))
    player_4.forward(randint(1, 5))

color('red')
goto(0, -100)
write('Finished', align = 'center', font=('Arial', 40, 'normal'))

# print(player_1.ycor())

# just wait around till the user closes the window
penup()
goto(0, 0)
while True:
    right(1)
