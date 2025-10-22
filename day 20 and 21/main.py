from turtle import Turtle, Screen
import time
import random

# --- Screen setup ---
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# --- Create the snake ---
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

head = segments[0]  # first segment = snake head

# --- Create food ---
food = Turtle("circle")
food.color("red")
food.shapesize(0.5, 0.5)  # smaller circle
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# --- Functions for controls ---
def go_up():
    if head.heading() != 270:
        head.setheading(90)

def go_down():
    if head.heading() != 90:
        head.setheading(270)

def go_left():
    if head.heading() != 0:
        head.setheading(180)

def go_right():
    if head.heading() != 180:
        head.setheading(0)

# --- Keyboard controls ---
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# --- Main game loop ---
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # move snake from tail to head
    for seg_num in range(len(segments) - 1, 0, -1):
        x = segments[seg_num - 1].xcor()
        y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x, y)
    head.forward(20)

    # --- Detect collision with food ---
    if head.distance(food) < 15:
        # move food to new random spot
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        # add new segment
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

    # --- Detect collision with wall ---
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):
        game_is_on = False
        print("Game Over! You hit the wall.")

    # --- Detect collision with tail ---
    for segment in segments[1:]:
        if head.distance(segment) < 10:
            game_is_on = False
            print("Game Over! You hit yourself.")

screen.exitonclick()
