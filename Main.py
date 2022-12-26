from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.speed(20)


def move_forward():
    tim.fd(10)


def move_backward():
    tim.bk(10)


def move_right():
    tim.setheading(tim.heading() - 10)


def move_left():
    tim.setheading(tim.heading() + 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()    

my_screen = Screen()
my_screen.listen()
my_screen.onkeypress(move_forward, "w")
my_screen.onkeypress(move_backward, "s")
my_screen.onkeypress(move_right, "d")
my_screen.onkeypress(move_left, "a")
my_screen.onkeypress(clear, "c")
my_screen.exitonclick()
