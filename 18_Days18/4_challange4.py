from turtle import *
import random

timy = Turtle()
angles = 180
timy.shape("classic")
# gap = 2
steps = 20
timy.hideturtle()
direction = [0, 90, 180, 270]
color = ['red', 'pink', 'blue', 'purple', 'brown', 'grey', 'green']
timy.pensize(5)
timy.speed("fastest")

for _ in range(200):
    timy.color(random.choice(color))
    # timy.pendown()
    timy.setheading(random.choice(direction))
    timy.forward(steps)

    # timy.penup()
    # timy.forward(gap)




screen = Screen()
screen.exitonclick()
