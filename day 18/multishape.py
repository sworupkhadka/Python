from turtle import Turtle, Screen     # Import turtle graphics
import random                         # For random color choice

colors = ["red", "orange", "black", "green", "blue", "purple"]

timmy = Turtle()                      # Create turtle object
timmy.color("red")                    # Set initial color

def draw(num_sides):                  # Draw polygon function
    angle = 360 / num_sides
    for tim in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side in range(3, 11):       # Loop from triangle to decagon
    timmy.color(random.choice(colors))
    draw(shape_side)

screen = Screen()                     # Create window
screen.exitonclick()                  # Close on click
