import turtle as t
import random

timy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


steps = 20
timy.hideturtle()
direction = [0, 90, 180, 270]
timy.pensize(5)
timy.speed("fastest")

for _ in range(200):
    warna = random_color()
    timy.color(warna)
    timy.setheading(random.choice(direction))
    timy.forward(steps)

