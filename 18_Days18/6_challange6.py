from turtle import *
import random
tim = Turtle()
tim.hideturtle()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def daw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.speed("fastest")
        warna = random_color()
        tim.color(warna)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

daw_spirograph(9)

# for _ in range(200):
#     tim.speed("fastest")
#     warna = random_color()
#     tim.color(warna)
#     tim.circle(100)
#     tim.setheading(tim.heading() + 10)

# for _ in range(200):
#     tim.speed("fastest")
#     warna = random_color()
#     tim.color(warna)
#     tim.pendown()
#     tim.circle(100)
#     tim.penup()
#     tim.right(10)









screen = Screen()
screen.exitonclick()