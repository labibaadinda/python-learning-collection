from turtle import Turtle, Screen

# from turtle import *
# simple nya tu gini tinggal aja import * otomatis bakal ke import semua class dari module/library turtle
# tapi  ya jadinya ga gt keliatan aja
tiny = Turtle()

# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

for _ in range(4):
    tiny.right(90)
    tiny.forward(100)

screen = Screen()
screen.exitonclick()