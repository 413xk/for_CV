import turtle

turtle.Screen().setup(640, 480)
turtle.Screen().bgcolor('lightgreen')
turtle.speed(10)


def teddy_bear():
    head(150)
    ears(50)
    eyes(20)
    nose(80)


def head(size):
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.fillcolor('BurlyWood')
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


def ears(size):
    for i in range(-1, 2, 2):
        turtle.penup()
        turtle.goto(120 * i, 60)
        turtle.pendown()
        turtle.fillcolor('LightPink')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()


def eyes(size):
    for i in range(-1, 2, 2):
        turtle.penup()
        turtle.goto(60 * i, -30)
        turtle.pendown()
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()


def nose(size):
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.fillcolor('NavajoWhite')
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, -170)
    turtle.pendown()
    turtle.goto(0, -80)
    turtle.fillcolor('Maroon')
    turtle.begin_fill()
    turtle.circle(size / 5)
    turtle.end_fill()


teddy_bear()

