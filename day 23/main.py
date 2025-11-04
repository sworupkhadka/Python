from turtle import Turtle, Screen
import random

# Initialize turtle and screen
player_turtle = Turtle()
screen = Screen()

# --- Screen setup ---
screen.setup(width=500, height=500)
screen.title("turtle crossing")
screen.tracer(0)  # Turn off automatic screen updates

user_bet = screen.textinput("Make your choice", "Choose a difficulty level (easy/medium/hard):")

# Set car speed based on user choice
if user_bet and user_bet.lower() == "easy":
    min_speed = 3
    max_speed = 8
elif user_bet and user_bet.lower() == "medium":
    min_speed = 6
    max_speed = 12
elif user_bet and user_bet.lower() == "hard":
    min_speed = 8
    max_speed = 14
else:
    min_speed = 4
    max_speed = 8

# Player turtle setup
player_turtle.hideturtle()
player_turtle.left(90)
player_turtle.shape("turtle")
player_turtle.penup()
player_turtle.goto(0, -230)
player_turtle.showturtle()

# Car setup
colors = ["red", "orange", "black", "green", "blue", "purple"]
y_positions = [-120, -80, 0, 40,  120,  200]
cars = []                                        # Creates an empty list called 'cars' and in line 48 cars.append(car) Add car to the list Now cars contains: [car1, car2, car3, car4, car5, car6]

for i in range(6):
    car = Turtle(shape="square")
    car.shapesize(1, 2)
    car.color(random.choice(colors))
    car.penup()
    car.goto(x=random.randint(-200, 250), y=y_positions[i])
    cars.append(car)

is_race_on = True
game_over = False


def go_up():
    if not game_over:
        player_turtle.forward(10)
        check_win()


def go_down():
    if not game_over:
        player_turtle.backward(10)


def check_collision():
    """Check if player collides with any car"""
    for car in cars:
        if player_turtle.distance(car) < 25:
            return True
    return False


def check_win():
    """Check if player reached the top of the screen"""
    if player_turtle.ycor() > 250:
        return True
    return False


def display_message(message):
    """Display game over or win message"""
    message_turtle = Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.color("black")
    message_turtle.goto(0, 0)
    message_turtle.write(message, align="center", font=("Arial", 24, "bold"))


screen.listen()
screen.onkey(key="w", fun=go_up)
screen.onkey(key="s", fun=go_down)
screen.onkey(key="Up", fun=go_up)
screen.onkey(key="Down", fun=go_down)


def move_cars():
    global is_race_on, game_over

    if is_race_on:
        for car in cars:
            # Move each car forward
            rand_distance = random.randint(min_speed, max_speed)
            car.forward(rand_distance)

            # Reset car position if it goes off screen
            if car.xcor() > 250:
                car.goto(-250, car.ycor())
            elif car.xcor() < -250:
                car.goto(250, car.ycor())

        # Check for collisions
        if check_collision():
            is_race_on = False
            game_over = True
            display_message("GAME OVER")

        # Check for win
        if check_win():
            is_race_on = False
            game_over = True
            display_message("YOU WIN!")

        screen.update()
        if is_race_on:
            screen.ontimer(move_cars, 50)


# Start the game
move_cars()
screen.exitonclick()