from turtle import *

screen = Screen()
screen.setup(400, 400)
screen.title("Its a Square")

ttl = Turtle()  
ttl.color('blue', 'red')
ttl.penup()
# Remember X=0, Y=0 is center of the screen
ttl.goto(-125, 125)
ttl.pendown()
ttl.begin_fill()

for step in range(4):
    ttl.forward(250) # 250 pixels
    ttl.right(90) # turn right 90 degrees
ttl.end_fill()
ttl.penup()
ttl.goto(0, 0)
while True:
    ttl.right(1)
