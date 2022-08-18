from turtle import Turtle


class Scoreboard(Turtle):
    """Keeping track of the score of each player"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.first_score = 0
        self.second_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Recording the scores of both the first and second player simultaneously"""
        self.clear()
        self.goto(100, 200)
        self.write(self.first_score, align="center", font=("Aerial", 70, "normal"))
        self.goto(-100, 200)
        self.write(self.second_score, align="center", font=("Aerial", 70, "normal"))

    def first_score_update(self):
        """Increasing the first player's score"""
        self.first_score += 1
        self.update_scoreboard()

    def second_score_update(self):
        """Increasing the second player's score"""
        self.second_score += 1
        self.update_scoreboard()
