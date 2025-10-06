Hangman Game (Python Terminal Version)
<p align="center"> <strong>A simple terminal-based Hangman game built using Python</strong> </p>
This is a simple terminal-based Hangman game built using Python.
It uses ASCII art for the hangman stages and randomly selects a word for you to guess.

📂 Project Structure
text
hangman/
│
├── hangman.py  # Main game logic
└── pics.py     # ASCII art for hangman stages
🧩 Features
<ul> <li>Simple and beginner-friendly code</li> <li>Random word selection</li> <li>Tracks guessed letters</li> <li>Displays hangman progress with ASCII art</li> <li>Win and lose conditions</li> <li>Easy to modify and expand</li> </ul>
⚙️ How to Run
<ol> <li>Make sure you have <strong>Python 3</strong> installed.<br> Check with: <pre><code class="language-bash">python3 --version</code></pre> </li> <li>Clone or download this project folder.</li> <li>Open a terminal in the project folder and run: <pre><code class="language-bash">python3 hangman.py</code></pre> </li> </ol>
🧠 How It Works
<ul> <li>A random word is chosen from the list.</li> <li>You guess letters one by one.</li> <li>For every wrong guess, the hangman drawing progresses.</li> <li>If you guess all letters, you win 🎉</li> <li>If the hangman is complete, you lose 💀</li> </ul>
🗂️ Example Gameplay
text
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

<ul> <li>Word selection</li> <li>Guess checking</li> <li>Displaying hangman progress</li> <li>Input validation</li> </ul>
🎨 pics.py
Stores the ASCII art:

python
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
<ul> <li>Add difficulty levels (Easy, Medium, Hard)</li> <li>Load words from a text file</li> <li>Add score tracking</li> <li>Convert into a GUI (Tkinter) or web version</li> </ul>
💻 Author
<strong>Sworup Khadka</strong>

A fun and educational Python mini project 🎯