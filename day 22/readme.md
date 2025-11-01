## Pong Game (Python Turtle)

A fun and classic Pong Game built using the Python Turtle Graphics module.
Two players control paddles on opposite sides and try to bounce a moving ball — if one misses, the other scores a point.

---

### Features

Two-player paddle control (Left: W/S, Right: ↑/↓)    
Smooth ball movement and bouncing mechanics  
Live scoreboard updates for both players  
Ball resets automatically when a point is scored  
Simple and clean game design using only Python’s built-in turtle module  

---

### Concepts Used

Object-Oriented Programming with Turtle subclasses   
Collision detection using distance()   
Manual screen updates with tracer() and update()   
Keyboard event handling using onkey()   
Game loop with timing control via time.sleep()   

---




### Controls
Player	Move Up	Move Down  
🟦 Left Paddle	W	S  
🟥 Right Paddle	↑ (Up)	↓ (Down)    

---


##  Code Structure  
pong/  
 ├── main.py         # Main game loop and collision logic  
 ├── paddle.py       # Paddle class (movement and setup)  
 ├── ball.py         # Ball class (movement, bouncing, reset)  
 └── scoreboard.py   # Scoreboard class (tracks and displays scores)  

---
 ## Code Explanation   

----
### 1. Screen Setup     
screen = Screen()  
screen.setup(width=800, height=600)  
screen.bgcolor("black")  
screen.title("Pong Game")  
screen.tracer(0)  


Creates an 800×600 game window.  
screen.tracer(0) disables automatic animation updates — giving smoother control with screen.update() inside the game loop.  

---

## 2. Creating Paddles
r_paddle = Paddle((350, 0))      
l_paddle = Paddle((-350, 0))   


Each paddle is a Turtle object shaped like a rectangle.
Positions are passed in during creation, and they move vertically when keys are pressed.

---
## 3. Creating the Ball
ball = Ball()  


The ball moves diagonally by default.  
It has attributes x_move, y_move, and move_speed to control direction and speed.  

---
## 4. Keyboard Controls  
screen.listen()  
screen.onkey(r_paddle.go_up, "Up")  
screen.onkey(r_paddle.go_down, "Down")  
screen.onkey(l_paddle.go_up, "w")  
screen.onkey(l_paddle.go_down, "s")  


Listens for user input and moves each paddle accordingly.  

---

## 5. Main Game Loop
while game_is_on:  
    time.sleep(ball.move_speed)  
    screen.update()  
    ball.move()  


Keeps the game running continuously.  
time.sleep() controls the speed, and screen.update() redraws the frame each loop.

---
## 6. Ball Collision with Walls
if ball.ycor() > 280 or ball.ycor() < -280:  
    ball.bounce_y()  


When the ball hits the top or bottom walls, it reverses its vertical direction.  

---

## 7. Ball Collision with Paddles
if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \  
   (ball.distance(l_paddle) < 50 and ball.xcor() < -320):  
    ball.bounce_x()  
  

If the ball touches a paddle, it bounces in the opposite horizontal direction and speeds up slightly.

---
## 8. Scoring System
if ball.xcor() > 380:  
    ball.reset_position()  
    scoreboard.l_point()  
if ball.xcor() < -380:  
    ball.reset_position()  
    scoreboard.r_point()  
  

When the ball passes a paddle, it resets to the center and the other player gets a point.
The Scoreboard updates automatically.  

---

## 9. Scoreboard Display
self.goto(-100, 200)  
self.write(self.l_score, align="center", font=("Courier", 40, "normal"))  
self.goto(100, 200)  
self.write(self.r_score, align="center", font=("Courier", 40, "normal"))  
  

Displays the scores for both players on the screen.  

---

## 10. Exit
screen.exitonclick()  
Keeps the game window open until you click on it. 

---

## Dependencies

turtle → Built-in Python graphics module  
time → Used to control game speed  
No external libraries required ✅  

---
## Future Improvements

Add dashed center divider line  
Add Game Over or Winning Score screen  
Add sound effects when the ball hits a paddle or wall  
Add pause/restart functionality  

---
 

## Author
Sworup Khadka  
Made using Python Turtle Graphics as part of a fun learning project.