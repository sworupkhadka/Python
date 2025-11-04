# Turtle Crossing Game
A classic arcade-style game built with Python's Turtle graphics where you help a turtle safely cross a busy road filled with moving cars.

---

## Game Description
In this exciting game, you control a turtle trying to cross from the bottom to the top of the screen while avoiding randomly moving cars. Choose your difficulty level and test your reflexes!

---
## Features
- Multiple Difficulty Levels: Easy, Medium, and Hard  
- Smooth Controls: Responsive keyboard controls  
- Collision Detection: Real-time collision detection with cars  
- Win/Lose Conditions: Clear victory and game over states  
- Randomized Gameplay: Cars move at random speeds and positions  
- Visual Feedback: Clear messages for game outcomes  

---
## How to Play
Objective  

Guide your turtle from the bottom of the screen to the top without colliding with any cars.

### Controls
- W Key or ↑ Arrow: Move turtle UP  
- S Key or ↓ Arrow: Move turtle DOWN

### Game Rules
- The turtle starts at the bottom center of the screen  
- Cars move horizontally across the screen at different speeds  
- If the turtle collides with any car: GAME OVER    
- If the turtle reaches the top of the screen: YOU WIN!      


### Difficulty Levels
Easy: Slower moving cars  
Medium: Moderate car speed  
Hard: Fast moving cars   

---
## Run the game:
- Turtle module (comes built-in with Python)  
- Running the Game    
- Clone or download the game files  
- Navigate to the game directory    


python3 file_name.py

---

## Game Code Structure

---
# Main components:
- Player Turtle: User-controlled character
- Cars: Multiple obstacles moving horizontally
- Game Loop: Manages car movement and collision detection
- Difficulty System: Adjusts car speeds based on user choice
- Win/Lose Conditions: Checks for collisions and successful crossing

---
## Key Functions 
- go_up() / go_down(): Player movement functions  
- check_collision(): Detects turtle-car collisions  
- check_win(): Checks if turtle reached the top  
- display_message(): Shows game over/win messages 
- move_cars(): Main game loop controlling car movement 
---

## Game Mechanics
### Car Behavior
- Cars move horizontally at random speeds
- Cars wrap around the screen when they reach the edges
- Each car has a random color and starting position
- Speed ranges vary by difficulty level

---
## Collision System
- Uses distance-based collision detection (25-pixel threshold)
- Real-time collision checking during each game loop iteration
- Immediate game over on collision

---
## Win Condition
- Turtle must reach y-coordinate > 250
- Win message displays upon successful crossing

---
## Troubleshooting
### Common Issues
- Game doesn't start: Ensure you're using Python 3.x
- Controls not working: Make sure to click on the game window first
- Import errors: Check that all files are in the same directory

---
## Performance Tips
- Close other applications for smoother gameplay
- Ensure your Python environment is up to date

---
## File Structure

turtle_crossing/   
├── turtle_crossing_game.py  # Main game file  
├── README.md               # This file  
└── requirements.txt        # Python dependencies  

---
## Customization
### You can easily modify the game by changing these variables:

- colors: Car colors  
- y_positions: Car lane positions  
- min_speed/max_speed: Difficulty settings  
- Collision distance threshold  
- Screen size and dimensions

---
## Contributing
- Feel free to fork this project and submit pull requests for:
- New features
- Bug fixes
- Performance improvements
- Additional difficulty levels

---
##  License
This project is open source and available under the MIT License.

---
## Acknowledgments
Built with Python's Turtle graphics library  
Inspired by classic arcade games  
Thanks to the Python community for excellent documentation  