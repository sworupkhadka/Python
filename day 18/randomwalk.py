from turtle import Turtle, Screen     # Import turtle graphics
import random                         # For random color choice

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "gray"]
direction=[0,90,180,270]

timmy = Turtle()                      # Create turtle object
timmy.pensize(10)
timmy.speed("fastest")

for tim in range (1000):
    timmy.forward(30)
    timmy.setheading(random.choice(direction))
    timmy.color(random.choice(colors))

screen = Screen()                     # Create window
screen.exitonclick()                  # Close on click
