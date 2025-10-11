Python Blackjack Game

This project is a simple command-line **Blackjack game** built in Python.  
It uses functions, loops, and conditional logic to simulate a realistic Blackjack match between the player and the computer (dealer).

---

## 📘 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Rules](#rules)
* [Code Structure](#code-structure)
* [How to Run](#how-to-run)
* [Example Gameplay](#example-gameplay)

---

## 🎯 Overview

The game allows the player to draw cards and try to get a score as close to **21** as possible without exceeding it.  
The computer automatically draws cards until its total is **17 or higher**.  
Special rules for **Blackjack** and **Ace adjustments** are handled within the logic.

---

## ⚙️ Features

* Random card drawing using Python’s `random` module  
* Score calculation with automatic Ace (11 → 1) adjustment  
* Computer (dealer) draws cards automatically until score ≥ 17  
* Clear win, lose, or draw result messages  
* Option to replay multiple rounds in one session  

---

## 🃏 Rules

* Each card has a value:  
  - Number cards (2–10): face value  
  - Face cards (J, Q, K): 10  
  - Ace (A): 11 or 1, depending on which is better for your hand  

* A hand with an Ace and a 10-value card (21 with two cards) is a **Blackjack**.  
* If your total exceeds 21, you **bust** and lose the game.  
* The dealer must keep drawing until their score reaches **17 or more**.

---

## 🧩 Code Structure

```python
deal_card()        # Returns a random card from the deck
calculate_score()  # Calculates score and handles Ace adjustments
compare()          # Compares user and computer scores
play_game()        # Runs the main game logic
The game flow:

Deal two cards to both player and computer.

Player chooses to draw (‘y’) or pass (‘n’).

Computer draws automatically until its score ≥ 17.

Final results are displayed.

▶️ How to Run
Make sure you have Python 3.7+ installed.

Save the file as blackjack.py.

Open your terminal in the project folder and run:


python3 blackjack.py
Follow the on-screen instructions:

Type 'y' to get another card
Type 'n' to pass

💻 Example Gameplay

Do you want to play a game of Blackjack? Type 'y' or 'n': y

Your cards: [10, 7], current score: 17
Computer's first card: 8
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 7], final score: 17
Computer's final hand: [8, 9, 3], final score: 20
You lose 
