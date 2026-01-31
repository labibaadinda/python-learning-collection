# Turtle Graphics, Event Listeners, State, Multiple Instances

# listen() memberitahu jendela Turtle (objek Screen) untuk mulai mendengarkan input keyboard
# artinya :
# Sebelum kamu bisa menangkap event seperti menekan tombol panah, spasi, huruf,dsb.
# kamu harus mengaktifkan pendengar (listener) dengan screen.listen()
# Setelah itu kamu  bia menggunakan onkey(), onkeypress(), atau onkeyrelease()
# untuk mengaitkan tombol tertentu dengan fungsi yang kamu buat.

# Analogi gampang
# Bayangkan Screen itu seperti panggung dan listen() itu seperti "menaruh microfon aktif"
# Tanpa memanggil listen(), panggungnya tidak akan mendengar tombol yang ditekan dari keyboard



# konsep tersebut diturunkan dari Higher-Order Function
# A higher-order function is a function that takes another function as an argument,
# or returns a function as its result (atau keduanya)
# dengan kata lain, fungsi yang memperlakukan fungsi lain sebagai data.


import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

x = -230
y = -100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Congratulation your {winner} turtle win win !")
            else:
                print(f"Sorry you lose, the turtle winner is turtle {winner} !")

        race = random.randint(0, 10)
        turtle.forward(race)














screen.exitonclick()


