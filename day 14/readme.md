# Higher or Lower Game

## Overview
This is a Python-based **Higher or Lower** game.  
The game compares **follower counts of famous people**, and the player guesses who has more followers. The game continues **until the player guesses wrong**.

---

## How the Game Works
1. **Two people are selected** randomly from the dataset:
   - `choice_a` is the first person.
   - `choice_b` is randomly selected but **cannot be the same as `choice_a`**.
     ```python
     choice_a = random.choice(data)
     choice_b = random.choice([item for item in data if item != choice_a])
     
     
    –List comprehension:
    This creates a new list containing all items from data except choice_a.
    How it works step by step:

    - for item in data → goes through each element in data.

    - if item != choice_a → only includes the item if it is not equal to choice_a.

    - Result: a list of all possible choices excluding the one already chosen as choice_a.
     ```
   - Alternatively, you can use:
     ```python
     choice_a, choice_b = random.sample(data, 2)
     ```
2. **Display their information**:
   - Name
   - Description
   - Country
3. **User guesses**:
   - Type **'A'** or **'B'** for who has more followers.
4. **Check the guess**:
   - Compare the follower counts of `choice_a` and `choice_b`.
   - If correct:
     - Score increases by 1.
     - The winner becomes the new `choice_a`.
     - A new `choice_b` is selected for the next round. make sure choice_b and choice_a are not same 
   - If incorrect:
     - The game ends and the **final score** is displayed.

---

## Python Concepts Used
- **Lists and Dictionaries** – store and access game data.
- **Random Module** – pick random choices (`random.choice()` or `random.sample()`).
- **While Loops** – continue the game until the user guesses wrong.
- **Conditional Statements** – check the correctness of user guesses.
- **Input Handling** – read and process user input.
- **f-strings** – format and display output clearly.

---

## Example Gameplay
Compare A: Cristiano Ronaldo, a Footballer, from Portugal
Compare B: Lionel Messi, a Footballer, from Argentina
Who has more followers? Type 'A' or 'B': A
🎉 Correct guess! Your score: 1