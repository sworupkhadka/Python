'''inheritance is a mechanism that allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass).
It’s used to reuse code and create a hierarchy of classes.

Key Points:
-Child class inherits all attributes and methods from parent class.
-You can override parent methods in the child class.
-Supports single, multiple, and multilevel inheritance in Python'''

'''Single Inheritance
A child class inherits from one parent class only.
 Reuse parent class code in a child class.'''

# Parent class
class Animal:
    def eat(self):
        print("Animal is eating")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()   # inherited from Animal
d.bark()  # defined in Dog


'''Multilevel Inheritance
A class inherits from a child class, which itself inherits from a parent class.
Creates a chain of inheritance.'''

class Grandparent:
    def show_grandparent(self):
        print("I am the grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am the parent")

class Child(Parent):
    def show_child(self):
        print("I am the child")

c = Child()
c.show_grandparent()  # inherited from Grandparent
c.show_parent()       # inherited from Parent
c.show_child()        # defined in Child


'''Multiple Inheritance
A child class inherits from more than one parent class.
Combine functionalities from multiple parent classes.'''

class Father:
    def skills_father(self):
        print("Father skills: Gardening")

class Mother:
    def skills_mother(self):
        print("Mother skills: Cooking")

class Child(Father, Mother):
    def skills_child(self):
        print("Child skills: Programming")

c = Child()
c.skills_father()   # from Father
c.skills_mother()   # from Mother
c.skills_child()    # from Child