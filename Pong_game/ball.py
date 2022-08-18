from turtle import Turtle
from random import randint


class Ball(Turtle):
    """Ball makeup and movement"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(randint(-45, 45))
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def movement(self):
        """The move of the ball as to simultaneous increment in both the x-axis and y-axis.
        Note that this covers for both the angle of reflection in a trivial way"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bouncing off the top or bottom of the screen"""
        self.y_move *= -1

    def bounce_x(self):
        """Bouncing off of the bat of the players"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Resetting position after the failure of any player"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


