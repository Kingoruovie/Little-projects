from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Turtle at the base of the game interface"""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_upward_distance(self):
        self.forward(MOVE_DISTANCE)

    def check_reach_edge(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
