import turtle
import random

width = 640
height = 480
turtle.Screen().setup(width, height)
# turtle.hideturtle()
turtle.speed(10)


def snowflake(size):
    turtle.penup()
    turtle.setpos(random.randint(0, 100), random.randint(0, 100))  # random position
    turtle.pendown()
    # one snowlake branch
    for _ in range(3):
        turtle.forward(size / 3)
        turtle.left(45)
        turtle.forward(size / 10)
        turtle.backward(size / 10)
        turtle.right(90)
        turtle.forward(size / 10)
        turtle.backward(size / 10)
        turtle.left(45)
    turtle.forward(size / 8)
    turtle.backward(size + size / 8)
    turtle.left(45)


snowflake(200)
'''
for _ in range(random.randint(0, 10)):
  snowflake(random.randint(0, 10))
'''
