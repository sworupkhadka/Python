from turtle import Turtle,Screen
timmy=Turtle()

timmy.shape("turtle")
timmy.color("red")


for tim in range (15):                        #loop to repeat steps 15 times
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()



screen=Screen()
screen.exitonclick()

