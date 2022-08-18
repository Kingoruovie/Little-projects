# Actually made a more lengthy code but had to rewrite using for loops since there repetitive task.

from random import randint
from turtle import Turtle, Screen

list_of_turtle = []
color_of_turtle = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_coordinate = [-75, -50, -25, 0, 25, 50, 75]

screen = Screen()
screen.setup(width=400, height=400)
# This is a for loop for the creation of the different instances of my turtles
for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_of_turtle[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-170, y_coordinate[turtle_index])
    list_of_turtle.append(new_turtle)

user_guess = screen.textinput(title="YOUR GUESS", prompt="Which turtle wins the race? Enter a color from the spectrum")

start_race = True
winning_turtle = ""
while start_race:
    # For loop running through a list of turtle created and making all of them move randomly
    for turtle in list_of_turtle:
        turtle.forward(randint(0, 10))
        # A conditional to make turtle not leave screen, but must under for loop to check all instances in list
        if turtle.xcor() > 160:
            winning_turtle = turtle.pencolor()
            start_race = False
# printing final result for my betting game_
if user_guess == winning_turtle:
    print(f"You won the bet. The color of the turtle who won was {winning_turtle}")
else:
    print(f"You lost the bet. The color of the turtle who won was {winning_turtle}")
screen.exitonclick()
