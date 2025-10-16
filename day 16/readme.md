# Python OOP Project Examples

This repository contains several Python projects demonstrating **Object-Oriented Programming (OOP)** concepts, along with practical usage of modules like `turtle` and `prettytable`.  

---

## Table of Contents
1. [Coffee Machine Simulation](#coffee-machine-simulation)
2. [Turtle Graphics Example](#turtle-graphics-example)
3. [PrettyTable Example](#prettytable-example)
4. [Requirements](#requirements)
5. [How to Run](#how-to-run)

---

## Coffee Machine Simulation

This is a small simulation of a coffee machine using OOP principles.

**Modules Used:**
- `menu.py` → Handles available drinks
- `coffee_maker.py` → Manages ingredients and brewing
- `money_machine.py` → Handles transactions

**Example Code:**
```python
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
Features:

Shows a menu of drinks.

Checks if resources are sufficient.

Processes payment before brewing.

Prints reports for ingredients and money.

Turtle Graphics Example
A simple demonstration of using the turtle module with OOP:




from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
Features:

Moves a turtle forward.

Changes turtle color and shape.

Prints canvas height.

Waits for a click to close the window.

PrettyTable Example
Demonstrates creating and printing tables using PrettyTable:



from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "Address", "Height"]
table.add_row(["Sworup", 22, "Pokhara", 6.2])
table.add_row(["Aastha", 21, "Kathmandu", 5.5])
table.align = "l"

print(table)
Features:

Creates a formatted table.

Customizes column alignment.

Easily extendable for more data.




