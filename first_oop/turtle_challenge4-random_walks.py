# random walks have various application in the aspect of modelling the uncertainties of things
import turtle
import random
from turtle import Screen

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tom = turtle.Turtle()
tom.pensize(15)
tom.speed("fastest")
turtle.colormode(255)
for movement in range(200):
    tom.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    tom.forward(30)
    tom.seth(random.choice(directions))

Screen().exitonclick()
