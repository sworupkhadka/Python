#  Python Turtle Graphics Projects

This repository contains fun and interactive Python Turtle graphics projects. These projects help you learn loops, functions, user input, event handling, and graphics programming while building creative visual games.

##  Turtle Race Game

###  Overview
A colorful and fun Turtle Race Game where you can bet on which turtle will win. Each turtle moves forward by a random distance, and the first one to cross the finish line wins!

###  Features
- Six turtles with unique colors and starting positions
- User bet input before the race begins
- Each turtle moves a random distance per turn
- The race ends automatically when a turtle reaches the finish line
- Displays winner result in the console

###  Concepts Used
- `for` loops for creating multiple turtles
- `random.randint()` for random distances
- `textinput()` for user betting choice
- `xcor()` for finish line detection
- Lists for storing turtle objects

###  Code Example
```python
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your choice", "Which turtle color will win? (Red, Orange, Black, Green, Blue, Indigo):")

colors = ["Red", "Orange", "Black", "Green", "Blue", "Indigo"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtles = []

for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_positions[i])
    turtles.append(tim)

is_race_on = bool(user_bet)

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle won the race.")
screen.exitonclick()


 Turtle Movement Controller
 Overview
A keyboard-controlled Turtle Game that lets you move the turtle freely across the screen using W, A, S, D keys. You can also clear the screen and reset the turtle's position using the spacebar.

 Features
Move the turtle forward, backward, left, and right

Clear and reset the drawing instantly

Learn how to use event listeners with the turtle module

 Controls
Key	Action
W	Move Forward
A	Turn Left
D	Turn Right
S	Move Backward
SPACE	Clear & Reset

 Concepts Used
Functions for modular movement logic

Keyboard event listeners using onkey() and listen()

Pen control with penup(), pendown(), and clear()

 Code Example
python
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

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
screen.onkey(move_forward, "w")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(move_backward, "s")
screen.onkey(clear, "space")
screen.exitonclick()


 Key Concepts Learned
Turtle Graphics: Drawing and animation with the turtle module

Loops & Iteration: Creating continuous movements and multiple turtles

Functions: Writing clean, reusable movement logic

Event Handling: Keyboard input using onkey() and listen()

Randomization: Using the random module for unpredictable movement

Object-Oriented Basics: Managing multiple Turtle objects

User Interaction: Accepting input using textinput()


 Author
Sworup Khadka
Part of the 100 Days of Python Bootcamp — exploring creative and interactive projects using Python Turtle Graphics.