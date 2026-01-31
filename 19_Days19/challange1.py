from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forwards():
    # tim.setheading(0)
    tim.forward(20)

def backwards():
    tim.backward(20)

def counterClockwise():
    tim.circle(100,20)

def ClockWise():
    tim.circle(-100, 20)

def atas():
    tim.setheading(90)
    tim.forward(20)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    # tim.home()
    # screen.resetscreen()
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    # tim.home()
    # tim.clear()


screen.listen()

screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counterClockwise)
screen.onkey(key="d", fun=ClockWise)
screen.onkey(key="Up", fun=atas)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="l", fun=clear)


screen.exitonclick()
