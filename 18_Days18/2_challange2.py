# alias
# import turtle as t
#
# tim = t.Turtle()
# tadikan turtle tinggal manggil aja ya gaada error pas import turtle
# terus pas import heroes error (karena blm di download package nya)
# it is because turtle is a module that's packaged with the Python standard library

# import heroes
# import villains
#
# print(heroes.gen())

from turtle import *
timy = Turtle()
screen = Screen()
timy.shape("arrow")

for _ in range(15):
    timy.pendown()
    timy.forward(10)
    timy.penup()
    timy.forward(10)

# turtle.penup()
# turtle.pu()
# turtle.up()
# Pull the pen up – no drawing when moving.





screen.exitonclick()
