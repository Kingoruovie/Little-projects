from turtle import Turtle
FONT = ("Verdana", 24, "normal")


class Scoreboard(Turtle):
    """Keeping track of the score"""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-290, 260)
        self.hideturtle()
        self.level_number = 1
        self.write_level()

    def write_level(self):
        self.write(f"level: {self.level_number}", align="left", font=FONT)

    def level_increment(self):
        self.clear()
        self.level_number += 1
        self.write_level()

    def game_over_trigger(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


