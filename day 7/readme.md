# 🎮 Hangman Game (Python Terminal Version)

This is a simple **terminal-based Hangman game** built using Python.  
It uses ASCII art for the hangman stages and randomly selects a word for you to guess.

---

## 📂 Project Structure

hangman/
│
├── hangman.py # Main game logic
└── pics.py # ASCII art for hangman stages

yaml
Copy code

---

## 🧩 Features

- Simple and beginner-friendly code  
- Random word selection  
- Tracks guessed letters  
- Displays hangman progress with ASCII art  
- Win and lose conditions  
- Easy to modify and expand  

---

## ⚙️ How to Run

1. Make sure you have **Python 3** installed.  
   Check with:
   ```bash
   python3 --version
Clone or download this project folder.

Open a terminal in the project folder and run:

bash
Copy code
python3 hangman.py
🧠 How It Works
A random word is chosen from the list.

You guess letters one by one.

For every wrong guess, the hangman drawing progresses.

If you guess all letters, you win 🎉

If the hangman is complete, you lose 💀

🗂️ Example Gameplay
yaml
Copy code
Let's play Hangman!

 +---+
     |
     |
     |
    ===
Word: _ _ _ _ _ _

Guess a letter: a
❌ Wrong!

 +---+
 O   |
     |
     |
    ===
Word: _ _ _ _ _ _
📜 Code Files
🧠 hangman.py
Handles:

Word selection

Guess checking

Displaying hangman progress

Input validation

🎨 pics.py
Stores the ASCII art:

python
Copy code
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    ...
]
🚀 Future Improvements
Add difficulty levels (Easy, Medium, Hard)

Load words from a text file

Add score tracking

Convert into a GUI (Tkinter) or web version

💻 Author
Sworup Khadka
A fun and educational Python mini project 🎯

yaml
Copy code
