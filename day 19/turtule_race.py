from turtle import Turtle, Screen
import random

# Screen setup
screen = Screen()
screen.setup(width=500, height=400)

# Ask user for a bet
user_bet = screen.textinput("Make your choice", "Which turtle color will win? (Red, Orange, Black, Green, Blue, Indigo):")

colors = ["Red", "Orange", "Black", "Green", "Blue", "Indigo"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtles = []

# Create turtles
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_positions[i])  # start position
    turtles.append(tim)

is_race_on = False

if user_bet:
    is_race_on = True

# Start race
while is_race_on:
    for turtle in turtles:
        # Move each turtle forward randomly
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        # Check if turtle reached finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color.lower() == user_bet.lower():
                print(f"You've won!  The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost  The {winning_color} turtle won the race.")

screen.exitonclick()
