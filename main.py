from random import randint, choice
import turtle


tim = turtle.Turtle()
tim.speed("fastest")
turtle.colormode(255)
tim.pensize(1)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb

def random_turn():
    tim.seth(choice([90, 180, 270, 360]))

def random_walk(steps):
    for _ in range(0, steps):
        tim.forward(25)
        random_turn()
        tim.pencolor(random_color())


def random_circle_figurine(circles, radius):
    angle_step = 360 / circles
    for circle in range(circles):
        tim.pencolor(random_color())
        tim.circle(radius)
        tim.left(angle_step)





random_circle_figurine(60, 120)







screen = turtle.Screen()
screen.exitonclick()
