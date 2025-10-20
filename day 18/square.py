from turtle import Turtle, Screen

timmy= Turtle()                         #creating a object timmy to access Turtle
timmy.shape("turtle")
timmy.color("red")

# drawing a square
timmy.forward(100)                      #move 100 spaces forward
timmy.left(90)                          #turn 90 degree to the left
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)

screen=Screen()                                       #creating a object screen
screen.exitonclick()                                  # so that screen closes only on click