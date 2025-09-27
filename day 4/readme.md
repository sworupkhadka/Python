# Python Random Module and Basic List Operations

This README demonstrates the usage of Python's `random` module, list operations, and a simple Rock-Paper-Scissors game with input handling.

---

## Table of Contents

* [Importing Modules](#importing-modules)
* [Random Number Generation](#random-number-generation)

  * [Random Integers](#random-integers)
  * [Random Floats](#random-floats)
  * [Coin Toss Simulation](#coin-toss-simulation)
  * [Random Selection from a List](#random-selection-from-a-list)
* [List Operations](#list-operations)

  * [Accessing Elements](#accessing-elements)
  * [Modifying Elements](#modifying-elements)
  * [Extending Lists](#extending-lists)
  * [Index Errors](#index-errors)
  * [Nested Lists](#nested-lists)
* [Rock-Paper-Scissors Game](#rock-paper-scissors-game)
* [String Cleaning: `.strip()` and `.lower()`](#string-cleaning-strip-and-lower)

---

## Importing Modules

```python
import random      # Standard module for random numbers
import my_module   # Custom module

print(my_module.my_favorite_number)
```

---

## Random Number Generation

### Random Integers

```python
random_integer = random.randint(1, 10)  # 1 to 10 inclusive
print(random_integer)
```

### Random Floats

```python
random_number_0_to_1 = random.random()  # 0.0 <= x < 1.0
print(random_number_0_to_1)

random_float = random.uniform(1.0, 10.0)  # 1.0 <= x <= 10.0
print(random_float)
```

### Coin Toss Simulation

```python
random_integer = random.randint(0, 1)
if random_integer == 0:
    print("heads")
else:
    print("tails")
```

### Random Selection from a List

```python
friends = ["a", "b", "c", "d", "e"]
random_choice = friends[random.randint(0, 4)]
print(random_choice)
```

---

## List Operations

### Accessing Elements

```python
states_of_nepal = ["gandaki", "bagmati", "sudurpaschim"]
print(states_of_nepal[0])  # gandaki
print(states_of_nepal[-1]) # sudurpaschim (last element)
```

### Modifying Elements

```python
states_of_nepal[1] = "bungamati"
print(states_of_nepal[1])  # bungamati
```

### Extending Lists

```python
states_of_nepal.extend(["lumbini", "karnali"])
print(states_of_nepal)
```

### Index Errors

```python
no_of_states = len(states_of_nepal)
print(states_of_nepal[no_of_states-1])  # last element
```

### Nested Lists

```python
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][2])  # Tomatoes
print(dirty_dozen[1][3])  # Celery
```

---

## Rock-Paper-Scissors Game

```python
import random

print("Welcome to Rock-Paper-Scissors!")
print("Type 'q' to quit.")

choices = ['rock', 'paper', 'scissors']
while True:
    user_choice = input("Choose rock, paper or scissors: ").strip().lower()
    if user_choice == 'q' or user_choice == 'quit':
        print("Goodbye!")
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")
```

---

## String Cleaning: `.strip()` and `.lower()`

* `.strip()` removes leading and trailing spaces or newlines.
* `.lower()` converts all characters to lowercase.
* Combined, they help handle user input consistently:

```python
user_input = "   RoCk  "
cleaned = user_input.strip().lower()
print(cleaned)  # Output: "rock"
```

This ensures comparisons are **case-insensitive** and **space-insensitive**.
