from turtle import Turtle


class Line(Turtle):
    """Drawing the broken line to divide the screen"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(5)
        self.hideturtle()
        self.draw()

    def draw(self):
        self.penup()
        self.goto(0, -300)
        self.pendown()
        self.setheading(90)
        for i in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()