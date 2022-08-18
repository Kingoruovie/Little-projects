# polygon construction
from turtle import Turtle, Screen
from random import choice

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
           "SlateGray", "SeaGreen"]
terry = Turtle()

for _ in range(3, 11):
    terry.color(choice(colours))
    for i in range(_):
        terry.forward(100)
        terry.left(360 / _)

Screen().exitonclick()
