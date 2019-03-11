#Analouge Clock by SubControl(Mustafa Dağkıranlar)
#-----Notes-Start-------#
#     wn = window       #
#-----Notes-End---------#

# Watch interface start
import turtle
import time
window = turtle.Screen()
window.bgcolor("white")
window.setup(width = 600, height = 600)
window.title("Analog Clock by MD")
window.tracer(0)# turns off the animation
# Watch interface end

# Create our drawing pen
pen = turtle.Turtle()
pen.hideturtle()# hide the drawing pen
pen.speed(0)# animation speed 0 is the fastest
pen.pensize(3)# width of the lines

def draw_clock(h, m, s, pen): # Drawing clock with pen code
    # Draw Clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)# radius of circle

    # Draw lines for hours
    pen.penup()
    pen.goto(0, 0)# Center
    pen.setheading(90)

    for _ in range(12): #12 hours
        pen.fd(190)# go up to the circle
        pen.pendown()
        pen.fd(20)
        pen.up()
        pen.goto(0, 0)
        pen.rt(30)# each hour is 30 degrees

    # Draw hour hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("grey")
    pen.setheading(90)# 0 right 90 up 180 left 270 down
    angle = (h / 12) * 360 + (m / 60) * 30
    pen.rt(angle)
    pen.pendown()
    pen.fd(80)

    # Draw minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("blue")
    pen.setheading(90)# 0 right 90 up 180 left 270 down
    angle = (m / 60) * 360 + (s / 60) + 6
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    # Draw second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)# 0 right 90 up 180 left 270 down
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

while True:
    h = int(time.strftime("%I"))# Gives time straight forward %I gives time 0 to 12
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    draw_clock(h, m, s, pen)
    window.update()
    time.sleep(1)
    pen.clear()


window.mainloop()  # with this loop window never close
