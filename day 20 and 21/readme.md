#  Snake Game (Python Turtle)

A fun and classic **Snake Game** built using the **Python Turtle Graphics** module.  
The player controls a snake that moves around, eats food, grows longer, and ends the game when it hits a wall or itself.

---

##  Features

- Smooth snake movement with arrow keys  
- Randomly spawning food  
- Snake grows longer after eating  
- Game ends when the snake collides with walls or itself  
- Simple design using only Python’s built-in `turtle` module  

---

##  Concepts Used

- **Object creation** with `Turtle()`  
- **For loops** to move segments  
- **Collision detection** using `distance()`  
- **Keyboard event handling** with `onkey()`  
- **Screen updates** using `tracer()` and `update()` for smooth animation  

---

##  How to Run

### 1. Clone or download the repository
```bash
git clone https://github.com/<your-username>/snake-game.git
cd snake-game
2. Run the game

python3 snake_game.py
 Make sure Python 3.8 or later is installed.

 Controls
Key	Action
⬆️	Move Up
⬇️	Move Down
⬅️	Move Left
➡️	Move Right

Code Explanation
Below is a breakdown of how the game works:

1. Screen Setup

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
Creates a 600x600 window with a black background.

screen.tracer(0) stops automatic updates — we manually refresh the screen for smooth animation.


2. Creating the Snake

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

head = segments[0]
Builds a snake from 3 square turtles.

Each segment is stored in a list segments.

The first segment is treated as the head.


3. Adding Food

food = Turtle("circle")
food.color("red")
food.shapesize(0.5, 0.5)
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))
Creates a small red circle as food.

Appears at a random location using random.randint().


4. Controlling the Snake

def go_up():
    if head.heading() != 270:
        head.setheading(90)
Defines functions to change direction.

Prevents the snake from going directly backward (to avoid instant collision).


screen.listen()
screen.onkey(go_up, "Up")
Listens for keyboard inputs and calls direction functions.


5. Main Game Loop

while game_is_on:
    screen.update()
    time.sleep(0.1)
Repeats forever until a collision occurs.

time.sleep(0.1) controls the speed.


6. Moving the Snake

for seg_num in range(len(segments) - 1, 0, -1):
    x = segments[seg_num - 1].xcor()
    y = segments[seg_num - 1].ycor()
    segments[seg_num].goto(x, y)
head.forward(20)
Moves each segment to the position of the one before it.

Then moves the head forward — creating smooth snake movement.


7. Detecting Food Collision

if head.distance(food) < 15:
    food.goto(random.randint(-280, 280), random.randint(-280, 280))
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    segments.append(new_segment)
If the head gets close to food, it’s “eaten.”

Food moves to a new random position.
A new segment is added to the snake’s tail.


8. Detecting Collisions

# Wall collision
if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
    game_is_on = False
    print("Game Over! You hit the wall.")

# Self collision
for segment in segments[1:]:
    if head.distance(segment) < 10:
        game_is_on = False
        print("Game Over! You hit yourself.")
Ends the game if the snake hits the wall or touches its own body.


9. Exit

screen.exitonclick()
Keeps the window open until the user clicks.  


Dependencies
turtle → built-in Python graphics module
random → for random food placement
time → controls game speed
No external libraries required 


Future Improvements
Add scoreboard
Add speed increase as the snake grows
Add start/restart screen
Add sound effects 




Author
Sworup Khadka
Made  using Python Turtle Graphics