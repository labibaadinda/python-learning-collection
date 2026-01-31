import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

x = -230
y = -100

for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x, y)
    y += 30


