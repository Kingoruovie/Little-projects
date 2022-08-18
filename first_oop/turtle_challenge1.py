# draw a square

from turtle import Turtle, Screen

x = Turtle()

for _ in range(4):
    x.forward(100)
    x.left(90)

x.speed(1)
Screen().exitonclick()
