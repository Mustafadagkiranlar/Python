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
head.shape("circle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
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

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1) # Pause game for 1 Sec
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

    # check for a collision with the food
    if head.distance(food) < 20: # head of the snake is 20 by 20
        # move the food to a random place
        x = random.randint(-290, 290) # left border of creen is -300 and the right side is 300 up side 300 down side -300 so food span in range of 290 - 290
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup() # Make sure to dont draw on the screen
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1): # ref : https://www.youtube.com/watch?v=DxVPN1PIuLM&t=121s (6:00)
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with the body segments
    for segments in segments:
        if segments.distance(head)< 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"


    time.sleep(delay)


wn.mainloop()