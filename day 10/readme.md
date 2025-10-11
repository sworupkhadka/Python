# Python Functions and Calculator Project

This project demonstrates several Python concepts, including functions, multiple return values, leap year calculation, and a simple interactive calculator using functions and dictionaries.

---

## Table of Contents
- [1. Format Name Function](#1-format-name-function)
- [2. Function Composition](#2-function-composition)
- [3. Multiple Return Values](#3-multiple-return-values)
- [4. Leap Year Checker](#4-leap-year-checker)
- [5. Calculator Program](#5-calculator-program)

---

## 1. Format Name Function

This function formats a first name and last name into **title case** and prints the full name.

```python
def format_name(f_name, l_name):
    title_case_f = f_name.title()
    title_case_l = l_name.title()
    full_name = f"{title_case_f} {title_case_l}"
    print("Full Name in Title Case:", full_name)

format_name("sworup", "khadka")
Output:
Full Name in Title Case: Sworup Khadka



2. Function Composition

Demonstrates how the output of one function can be used as the input of another.

def function_1(text):
    return text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)

Output:
Hello



3. Multiple Return Values
Shows how a function can return multiple values, and how to unpack them.

def get_name_details(first_name, last_name):
    full_name = f"{first_name.title()} {last_name.title()}"
    initials = f"{first_name[0].upper()}.{last_name[0].upper()}."
    return full_name, initials

name, short = get_name_details("sworup", "khadka")
print("Full Name:", name)
print("Initials:", short)

Output:
Full Name: Sworup Khadka
Initials: S.K.



4. Leap Year Checker
Determines whether a given year is a leap year.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2024))  # True
print(is_leap_year(2025))  # False

Output:
True
False



5. Calculator Program
A simple interactive calculator that supports addition, subtraction, multiplication, and division. Uses a dictionary to map symbols to functions.

def add(n1, n2): 
    return n1 + n2
def subtract(n1, n2): 
    return n1 - n2
def multiply(n1, n2): 
    return n1 * n2
def divide(n1, n2): 
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))
    while should_accumulate:
        for symbols in operations:
            print(symbols)
        operator_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operator_symbol](num1, num2)
        print(f"{num1} {operator_symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue with {answer} or 'n' to start new calculation: ")
        if choice.lower() == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()

Features:
-Continuously calculate with the latest result.
-Restart the calculation when the user chooses 'n'.
-Supports multiple arithmetic operations using a dictionary.

Author
Sworup Khadka

Notes
-Make sure to run this code in a Python 3 environment.
-The calculator uses recursion to restart calculations, which is suitable for small sessions.