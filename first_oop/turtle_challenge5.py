# drawing a spirograph
import turtle
from random import randint

tina = turtle.Turtle()
turtle.colormode(255)
tina.speed("fastest")


def spirograph(size_of_turn):
    for turns in range(int(360 / size_of_turn)):
        tina.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        tina.circle(100)
        tina.left(size_of_turn)


spirograph(5)

screen = turtle.Screen()
screen.exitonclick()