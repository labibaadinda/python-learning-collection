from turtle import *
import random

timy = Turtle()
screen = Screen()
timy.shape("arrow")
angle = int(360)
colors = ['red', 'pink', 'blue', 'purple', 'brown', 'grey', 'green']


def draw_shape(num_sides):
    sudut = angle / num_sides

    for _ in range(num_sides):
        timy.forward(100)
        timy.left(sudut)

for num_sides_n in range(3, 11):
    timy.color(random.choice(colors))
    draw_shape(num_sides_n)



# for i in range(11):
#     for c in ('red', 'pink', 'blue', 'purple', 'brown', 'grey', 'green'):
#         timy.pendown()
#         num_sides = i + 3
#         sudut = angle / num_sides
#         timy.left(sudut)
#         steps = 100
#         timy.fd(steps)
#         timy.color(c)
#         timy.penup()










screen.exitonclick()