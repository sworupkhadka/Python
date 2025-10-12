# Number Guessing Project

A simple Python game where the computer randomly selects a number between 1 and 100, and the player tries to guess it. The game includes difficulty levels (`easy` and `hard`) that determine the number of attempts the player has.

---

## Scope

### Global Scope

#### 🧠 Definition
Global scope means the part of your program where a variable is **accessible everywhere** —  
from the top of your code, inside functions, and even after functions are called.

A **global variable** is created outside any function and belongs to the global scope.

---
#### 🧾 Example 1: Global Variable
```python
# Global variable (belongs to global scope)
player_health = 10

def show_health():
    print("Inside function:", player_health)

show_health()
print("Outside function:", player_health)

Output:
Inside function: 10
Outside function: 10

✅ The variable player_health is global, so both the function and the main program can use it.



🧾 Example 2: Local vs Global Scope

score = 100  # Global variable

def play_game():
    score = 50  # Local variable (only inside function)
    print("Inside function:", score)

play_game()
print("Outside function:", score)

Output:
Inside function: 50
Outside function: 100

⚡ Python treats the score inside the function as local because it’s defined there. The global score remains unchanged.



🧾 Example 3: Modifying Global Variables Using global Keyword

health = 10  # Global variable

def drink_potion():
    global health      # Tell Python we’re using the global variable
    health += 5        # Modify the global variable
    print("Inside function:", health)

drink_potion()
print("Outside function:", health)

Output:
Inside function: 15
Outside function: 15

✅ The global keyword lets you update the same variable that exists in the global scope.



Local Scope
🧠 Definition
A local scope is the area inside a function where variables are created and used.
A variable defined inside a function is called a local variable — it only exists while the function runs and cannot be accessed outside that function.


🧾 Example

def drink_potion():
    potion_strength = 2   # local variable
    print(potion_strength)

drink_potion()

Output:
2

⚠️ If you try this:

print(potion_strength)

You’ll get:
NameError: name 'potion_strength' is not defined
Because potion_strength does not exist outside the function — it’s limited to the local scope.



Block Scope
What “Block Scope” Means
In many programming languages (like C, C++, or JavaScript), a block — code between {} — creates its own mini-scope.
Variables declared inside {} exist only inside that block.
They disappear when you leave the block.


✅ Example in JavaScript:

javascript
Copy code
if (true) {
  let name = "Sworup";
}
console.log(name); // ❌ Error: name is not defined
Because let name is block-scoped — only visible inside the if block.


Python is Different
Python uses indentation, not {} braces — and it does not create a new scope for if, for, or while blocks.
Only functions, classes, and modules create new scopes.



🧾 Example 1: if Block

if True:
    message = "Hello, Sworup!"  # created inside the if block

print(message)  # ✅ Works fine in Python


Conclusion
-Global scope: variables accessible everywhere.
-Local scope: variables exist only inside a function.
-Block scope: Python does not have block scope for if, for, or while blocks. -Only functions, classes, and modules create new scopes.