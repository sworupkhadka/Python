# 🧠 Python OOP Project — True/False Quiz Game

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python through a fun and interactive **True/False Quiz Game**.  
It uses multiple modules (`question_model`, `quiz_brain`, `data`, `main`) to show how classes and objects can work together to create a functional program.

---

## 📚 Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Core Files](#core-files)
4. [Features](#features)
5. [Example Gameplay](#example-gameplay)
6. [Requirements](#requirements)
7. [How to Run](#how-to-run)
8. [Author](#author)

---

## 🧩 Overview

The Quiz Game presents a series of **True/False** questions to the user.  
Each question is stored as a `Question` object, and the game is controlled by the `QuizBrain` class.

The program:
- Displays one question at a time  
- Checks the user’s answer  
- Keeps and displays the score after each question  
- Ends when all questions are answered  

---

## 🗂️ Project Structure

quiz-game/
│
├── data.py # Contains all question data
├── main.py # Main file that starts the quiz
├── question_model.py # Defines the Question class
└── quiz_brain.py # Handles quiz logic and scoring


---

## ⚙️ Core Files

### `question_model.py`
Defines the `Question` class that stores a question and its correct answer.

```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
data.py
Contains the quiz question data as a list of dictionaries.


question_data = [
    {"text": "The sky is blue.", "answer": "True"},
    {"text": "There are 25 hours in a day.", "answer": "False"},
    {"text": "Python is a programming language.", "answer": "True"},
    {"text": "The Earth is flat.", "answer": "False"},
    {"text": "2 + 2 equals 4.", "answer": "True"}
]
quiz_brain.py
Manages the quiz logic — moves through questions, checks answers, and tracks the score.


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("✅ You got it right!")
            self.score += 1
        else:
            print("❌ That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
main.py
The main file that builds the question list and starts the quiz.


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(q["text"], q["answer"]) for q in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("🎉 You've completed the quiz!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")
🌟 Features
Fully OOP-based design

Clean and modular structure

Dynamic score tracking

Easy to expand — just add more questions in data.py

🧠 Example Gameplay

Q.1: The sky is blue. (True/False): True
✅ You got it right!
Your current score is: 1/1

Q.2: The Earth is flat. (True/False): False
✅ You got it right!
Your current score is: 2/2

🎉 You've completed the quiz!
Your final score: 2/2
💻 Requirements
Python 3.x

No external libraries needed

▶️ How to Run
Clone or download this project.

Open the project folder in your terminal or IDE.

Run the command:
python3 main.py
Type True or False when prompted for each question.