from turtle import Turtle, Screen, colormode
import random

colormode(255)
timmy = Turtle()
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):  # Use _ instead of 'tim'
        timmy.color(random_color())         # timmy is your Turtle object
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(10)                        # Draw spirograph with 10° gap


#another method
#at a time only use one method comment out another
# for tim in range (120):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.left(3)
#     timmy.circle(100)

screen = Screen()
screen.exitonclick()
