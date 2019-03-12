# simple snake game by SubControl(Mustafa Dağkıranlar)

import turtle
import time
import random

# change game speed
delay = 0.1

# setup screen
wn = turtle.Screen()
wn.title("Snake by Mustafa")
wn.bgcolor("black")
wn.setup(width=600, height=600)
# turns off the animation(turns off screen updates)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
# animation speed of the turtle
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 100)

segments = []

# functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Keyboard bindings
wn.listen()
#for python3 if python2 wn.onkey()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()
    # check for a collision with the food
    if head.distance(food) < 20: # head of the snake is 20 by 20
        # move the food to a random place
        x = random.randint(-290, 290) # left border of creen is -300 and the right side is 300 up side 300 down side -300 so food span in range of 290 - 290
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment
        new_segment = turtle.Turtle
        new_segment.speed(0)
        new_segment.shape("circle")


    move()

    time.sleep(delay)


wn.mainloop()