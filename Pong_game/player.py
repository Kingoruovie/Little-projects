from turtle import Turtle


class Player(Turtle):
    """Making players by combining turtles"""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moving player up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moving player down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
