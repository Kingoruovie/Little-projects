import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
level_score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_upward_distance, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if player.check_reach_edge():
        level_score.level_increment()
        player.go_to_start()
        car_manager.level_up()
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.list_of_cars:
        if car.distance(player) < 20:
            level_score.game_over_trigger()
            game_is_on = False

screen.exitonclick()
