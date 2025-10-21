from turtle import Turtle , Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(20)
    
def move_left():
    tim.left(90)
    tim.forward(10)

def move_right():
    tim.right(90)
    tim.forward(10)

def move_backward():
        tim.left(180)
        tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="space", fun=clear)
screen.exitonclick()
