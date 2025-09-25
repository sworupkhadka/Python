<h2>Day 3</h2>
<h3> Conditional Statements, Logical Operations, Code Blocks & Scopes</h3>

---
This README explains Python concepts related to conditional statements, logical operators, scopes, and nested if-else blocks.

---
<h3>Topics Covered</h3>

---
BMI Check with Conditions

Conditional Statements (if, elif, else)

Logical Operators (>=, <=, ==, !=)

Nested If-Else (Rollercoaster Example)

Modulo Operator (%)

Odd & Even Number Check

Pizza Order Calculator

Treasure Island Mini Game

---
<h3>BMI Check with Conditions</h3>
weight = 85
height = 1.85
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight") <
elif 18.5 <= bmi < 25:
    print("normal weight")
elif 25 <= bmi < 29.9:
    print("overweight")

---


<h3>Rollercoaster Height Check<
print("welcome to the roller coaster ") 
height = int(input("please enter your height in cm: \n"))

if height >= 120:
    print("you can ride the rollercoaster")
else:
    print("you cant ride the rollercoaster")

---

<h3>Logical Operators</h3>

>= greater than or equal to

<= less than or equal to

== equals to

!= not equal to

---
<h3>Nested If-Else (Rollercoaster with Age Pricing)</h3>
print("Welcome to the roller coaster ")<br>
height = int(input("Please enter your height in cm: \n"))<br>

if height >= 120:<br>
    print("You can ride the rollercoaster")<br>
    
    age = int(input("Enter your age: "))<br>
    if age > 18:<br>
        print("You have to pay $12")<br>
    elif age > 12 and age <= 18:  # python uses elif instead of elseif<br>
        print("You have to pay $7")<br>
    else:
        print("You have to pay $5")<br>
else:
    print("You can't ride the rollercoaster")<br>

    ---


<h3>Rollercoaster with Photos & Special Age Pricing</h3>
print("Welcome to the roller coaster ")<br>
height = int(input("Please enter your height in cm: \n"))<br>
if height >= 120:<br>
    print("You can ride the rollercoaster")<br>
    age = int(input("Enter your age: "))
    if 18 <= age < 45:
        bill = 12
        print("your tickets are $12")
    elif age > 12 and age <= 18:
        bill = 7
        print("your tickets are $7")
    elif age < 12:
        bill = 5
        print("your tickets are $5")
    elif 45 <= age <= 55:
        bill = 0
        print("your entry is free")

    want_photo = input("do you want a photo taken? type y for yes n for no:\n")
    if want_photo == "y":
        bill += 3       # add $3 to bill
    print(f"your final bill is ${bill}")       # fstring
    
else:
    print("You can't ride the rollercoaster")


---

<h3>Modulo Operator</h3>

Gives the remainder of division.

Examples:

print(10 % 2)  # 0
print(10 % 3)  # 1

---

<h3>Odd or Even Number Check</h3>
n = int(input("enter a number:\n"))<br>
if n % 2 == 0:<br>
    print("the number is even")<br>
else:<br>
    print("the number is odd")<br>

---

<h3>💰 Pizza Order Calculator</h3>
print("Welcome to Domino's")
size = input("What size of pizza do you want? S, M or L:\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N:\n")

bill = 0  # initialize bill

price as per size
if size == "S":<br>
    bill += 15<br>
elif size == "M":<br>
    bill += 20<br>
elif size == "L":<br>
    bill += 25<br>
else:<br>
    print("Please type S, M or L")<br>

adding pepperoni
if pepperoni == "Y":<br>
    if size == "S":<br>
        bill += 2   <br>
    else:<br>
        bill += 3 <br>  

adding extra cheese
if extra_cheese == "Y":  <br>
    bill += 1<br>
print(f"Your final bill amount is ${bill}")


---
<h3>🏝 Treasure Island Mini Game</h3>
print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice1 = input("Choose whether you want to go left or right: L or R \n")<br>

if choice1 == "L":<br>
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. "
                    "Do you want to swim or wait for a boat? S or W \n")<br>
    if choice2 == "W":
        choice3 = input("You arrived at the island unharmed. "
                        "There is a house with 3 doors: Yellow, Red, and Blue. "
                        "Choose one: Y, B, or R \n")

        if choice3 == "R":
            print("You entered the room full of fire. Game Over.")
        elif choice3 == "Y":
            print("You found the treasure! You win!")
        elif choice3 == "B":
            print("You chose the room full of water. You lose.")
        else:
            print("Choose either B, Y, or R.")
    else:
        print("You got attacked by a trout. Game Over.")
elif choice1 == "R":<br>
    print("You fell into a hole. Game Over.")<br>
else:<br>
    print("Please choose L or R.")<br>