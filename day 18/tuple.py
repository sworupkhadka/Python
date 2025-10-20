from turtle import Turtle, Screen, colormode
import random

colormode(255)                         # <-- Set color mode globally (0–255)

directions = [0, 90, 180, 270]

timmy = Turtle()                       # Create turtle object

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)                   # Return RGB tuple

timmy.pensize(10)
timmy.speed("fastest")

for _ in range(1000):
    timmy.color(random_color())        # Use random RGB color
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
