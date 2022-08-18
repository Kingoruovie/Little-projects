from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_clockwise():
    tim.left(10)


def turn_anticlockwise():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.speed("fastest")
    tim.setposition(0, 0)
    tim.seth(0)
    tim.speed("normal")
    tim.pendown()


screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_clockwise, "a")
screen.onkeypress(turn_anticlockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()
