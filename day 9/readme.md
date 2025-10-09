# Python Dictionaries and Nested Collections

This README provides an overview of Python dictionaries, nested dictionaries, lists, and practical examples including loops, modifications, and applications.

---

## Table of Contents

* [Introduction](#introduction)
* [Creating Dictionaries](#creating-dictionaries)
* [Accessing Dictionary Values](#accessing-dictionary-values)
* [Modifying Dictionaries](#modifying-dictionaries)
* [Looping Through Dictionaries](#looping-through-dictionaries)
* [Nested Dictionaries](#nested-dictionaries)
* [Dictionaries with Lists](#dictionaries-with-lists)
* [Practical Examples](#practical-examples)
* [Bidding Program Example](#bidding-program-example)

---

## Introduction

A **dictionary** in Python is an unordered collection of key-value pairs.  
- Keys must be **unique** and **immutable** (strings, numbers, tuples).  
- Values can be of any data type, including lists, dictionaries, or objects.

Syntax:
```python
my_dict = {"key1": "value1", "key2": "value2"}
Creating Dictionaries


Empty Dictionary
empty_dict = {}


Dictionary with Initial Values
programming_dictionary = {
    "Bug": "this is a bug",
    "Function": "part of a code",
    "Loop": "do a part over and over again"
}


Accessing Dictionary Values
print(programming_dictionary["Bug"])  # Output: this is a bug
Modifying Dictionaries


Add a new item
programming_dictionary["Snippet"] = "a specific part of code"
print(programming_dictionary)


Edit an item
programming_dictionary["Bug"] = "a moth in your computer"
print(programming_dictionary)


Wipe out a dictionary
programming_dictionary = {}
print(programming_dictionary)  # Output: {}


Looping Through Dictionaries
for key in programming_dictionary:
    print(key)                 # Prints keys
    print(programming_dictionary[key])  # Prints corresponding values



Example: Student Grades
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)'


Nested Dictionaries
capitals = {
    "france": "paris",
    "india": "delhi"
}

students = {
    "Harry": {"Math": 88, "Science": 92},
    "Ron": {"Math": 78, "Science": 85}
}

print(students["Harry"]["Math"])  # Output: 88

Dictionaries with Lists
travel_log = {
    "france": ["paris", "lille", "dijon"],
    "germany": ["berlin", "munich"]
}

# Access Lille
print(travel_log["france"][1])  # Output: lille

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])  # Output: D




## Practical Example: Silent Bidding Program
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of Rs {highest_bid}")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("Enter your name:\n")
    price = int(input("What is your bid (in Rs):\n"))
    bids[name] = price

    should_continue = input("Are there any new bidders? Type 'yes' or 'no':\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)


**Summary**
-Dictionaries store key-value pairs efficiently.
-Values can be primitive types, lists, or even other dictionaries.
-Nested dictionaries and lists allow for complex, structured data.
-Looping, modifying, and accessing dictionaries is intuitive and flexible.
-Practical examples like student grades and bidding programs show real-world use cases.