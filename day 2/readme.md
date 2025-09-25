# Day 2  

<h3>## 🐍 Python Basics & Calculations</h3>  

This README explains some basic Python operations including:  

> **Topics Covered**
> - BMI Calculation
> - Rounding Numbers
> - Assignment Operators
> - Type Checking & Conversion
> - F-Strings
> - Arithmetic Operators
> - Strings & Indexing
> - Tip Calculator

---

<h3>BMI Calculation & Rounding</h3>


height = 1.65
weight = 84
bmi = weight / (height**2)
print(bmi)          # 30.844124123424
print(int(bmi))     # 30
print(round(bmi))   # 31
print(round(bmi,2)) # 30.84

---

<h3>Assignment Operators</h3>
score = 1
score += 1
print(score)  # 2

score = 1
score -= 1
print(score)  # 0

score = 1
score *= 1
print(score)  # 1

score = 1
score /= 1
print(score)  # 1.0

---

<h3>Type Checking & Conversion</h3>
# Type Checking
print(type("hello"))  # <class 'str'>
print(type(123))      # <class 'int'>
print(type(3.142))    # <class 'float'>
print(type(True))     # <class 'bool'>

---

# Type Conversion
print("123" + "456")           # 123456
print(int("123") + int("456")) # 579

---

<h3>Using len() with Strings</h3>
name = input("Enter your name:\n")
length = len(name)
print("Number of letters in your name: " + str(length))

---

<h3>F-Strings (Formatted Strings)</h3>
score = 0
height = 1.9
winning = True

print(f"Your score is {score}, height is {height}, and winning is {winning}")


---
<h3>Arithmetic Operators</h3>
print(123 + 456)  # 579
print(7 - 3)      # 4
print(3 * 2)      # 6
print(6 / 3)      # 2.0 (always float)
print(6 // 3)     # 2 (integer division)
print(5 // 3)     # 1
print(5 ** 2)     # 25 (power)

---


PEMDAS / BODMAS Example

print(3 * (3 + 3) / 3 - 3)  # 3.0

---

<h3>Strings & Indexing</h3>
print("hello"[0])  # h
print("hello"[4])  # o
print("123" + "456") # 123456

<h3>Large Numbers & Floats</h3>
print(123_456_789) # 123456789
print(123,456,789) # 123 456 789
print(3.1475)      # float

<h3>Booleans</h3>
print(True)
print(False)

---

<h3>💰 Tip Calculator</h3>
print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $ \n"))
tip = int(input("What percentage tip would you like to give? 10, 15, 20: \n"))
people = int(input("How many people do you want to split the bill between? \n"))

bill_with_tip = bill + (tip / 100 * bill)
per_person = bill_with_tip / people

print(f"Each person has to pay: ${per_person}")

---