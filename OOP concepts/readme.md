# Object-Oriented Programming (OOP) in Python

---
## Table of Contents

-Introduction  
-Core Concepts   
-Classes and Objects  
-Attributes   
-Method  
-Static Methods   
-Abstraction  
-Encapsulation  

---


## Introduction
Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects, which are instances of classes. It helps in creating modular, reusable, and maintainable code.

---

## Key Components

-Class: Blueprint for creating objects   
-Object: Instance of a class  
-Attributes: Properties/data of the object  
-Methods: functions that define behavior  
-Constructor: Special method to initialize objects (__init__)  

---
## Core Concepts
The four main principles of OOP are:  
Encapsulation:  
Bundling data and methods that work on that data

Abstraction:  
Hiding complex implementation details

Inheritance:  
Creating new classes from existing ones

Polymorphism:  
Using a unified interface for different data types

---
## Classes and Objects
Basic Class Definition  


class Student:  
    # Class Attribute (shared by all students)  
    school = "ABC School"
    # Constructor (initializes instance attributes)    
    def __init__(self, name, age):  
        self.name = name   # Instance attribute  
        self.age = age     # Instance attribute  
        print(f"{self.name} has been added to {Student.school} database.")  
    def greet(self):  
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")  
 

Creating Objects
s1 = Student("Sworup", 20)  
s2 = Student("Aastha", 19)  

Accessing Attributes and Methods  
print(s1.name)        # Output: Sworup  
s1.greet()            # Output: Hello, my name is Sworup and I am 20 years old.  

---
## Key Takeaways  
Use classes to model real-world entities  
Constructors set up initial values for objects  
Attributes store data about object  
Methods define behavior for objects

---
## Attributes

---
## Class Attributes  
Belong to the class itself  
Shared by all objects of that class

class Student:  
    school = "ABC School"  # class attribute  

s1 = Student()  
s2 = Student()  

print(s1.school)  # Output: ABC School  
print(s2.school)  # Output: ABC School  

---
## Instance Attributes  
Belong to specific objects
Each object can have different values  


class Student:  
    def __init__(self, name):  
        self.name = name  # instance attribute  

s1 = Student("Sworup")  
s2 = Student("Aastha")  

print(s1.name)  # Output: Sworup  
print(s2.name)  # Output: Aastha  

---
## Methods

---
## Instance Methods  
Most common type of method   
Take self as first parameter   
Can access and modify object attributes    


class Student:  
    def __init__(self, name):  
        self.name = name  
    def introduce(self):    
        return f"My name is {self.name}"    

---
## Static Methods
Static methods belong to a class rather than an instance and don't have access to self or class attributes.

class Calculator:  
    @staticmethod  
    def add(a, b):  
        return a + b  

## Calling static method  
print(Calculator.add(5, 10))  # Output: 15  

calc = Calculator()  
print(calc.add(7, 3))         # Output: 10  


When to Use Static Methods  
When the method doesn't need self or instance attributes  
For utility functions logically related to the class  


---
## Abstraction  
Abstraction means hiding internal details and showing only essential functionality.  

class Car:  
    def __init__(self):  
self.acc = False  
        self.brk = False  
        self.clutch = False
    def start(self):  
        self.clutch = True  
        self.brk = True  
        print("Car started successfully!")  

car1 = Car()  
car1.start()  # User doesn't need to know about clutch and brake mechanics

---
### Abstraction Benefits  
Simplifies complex systems  
Reduces complexity for users  
Allows implementation changes without affecting users
  

---
## Encapsulation
Encapsulation protects object data by controlling access through methods.


class BankAccount:  
    def __init__(self, balance):    
        self.__balance = balance  # Private attribute  
    def get_balance(self):  
        return self.__balance  
    def deposit(self, amount):  
        if amount > 0:  
            self.__balance += amount  
            return True  
        return False    
    def withdraw(self, amount):  
        if 0 < amount <= self.__balance:  
            self.__balance -= amount  
            return True  
        return False
account = BankAccount(1000)  
print(account.get_balance())  # Output: 1000  
account.deposit(500)  
print(account.get_balance())  # Output: 1500  

---
### Encapsulation Benefits  
Data Protection: Prevents accidental modification  
Controlled Access: Validation through methods  
Maintainability: Internal changes don't affect external code  

