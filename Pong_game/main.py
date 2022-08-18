from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
from line import Line
# imported to reduce the speed of moving turtles on screen
import time

# Screen characteristics
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")

# Animation control. Set to 0 to switch off the animation
screen.tracer(0)

# Players of the game for both the left and the right
first_player = Player((350, 0))
second_player = Player((-350, 0))

# Ball or probably the tennis being played by each player
ball_made = Ball()

# The scorekeeper for each player
score = Scoreboard()

# Line sharing the screen so each player knows his part
line = Line()

# The screen method to control the players
screen.listen()
screen.onkeypress(first_player.go_up, "Up")
screen.onkeypress(first_player.go_down, "Down")
screen.onkeypress(second_player.go_up, "w")
screen.onkeypress(second_player.go_down, "s")

is_game_on = True
while is_game_on:
    # Sleep time varied to make the level much sophisticated than it starting point
    time.sleep(ball_made.move_speed)
    # The continuous motion of the ball to enhance the indefinite until a player is found faulted
    ball_made.movement()
    # Conditional to make ball bounce of the top or bottom
    if ball_made.ycor() > 280 or ball_made.ycor() < -280:
        ball_made.bounce_y()
    # Conditional to make ball bounce of the players bat
    if ball_made.xcor() > 320 and ball_made.distance(first_player) < 50 or \
            ball_made.xcor() < -320 and ball_made.distance(second_player) < 50:
        ball_made.bounce_x()
    # Conditional to check the failure of any player
    if ball_made.xcor() > 380:
        # Increment in second player's score since first player faulted
        score.second_score_update()
        # Reset balls position to the center
        ball_made.reset_position()
    if ball_made.xcor() < -380:
        score.first_score_update()
        ball_made.reset_position()
    # Update to enhance the display and movement since animation is shut
    screen.update()

screen.exitonclick()
