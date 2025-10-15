from menu import MENU

# Machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

def print_report():
    
    # Prints the current resource levels and money earned.
    
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def is_resource_sufficient(drink):
    
    # Checks if there are enough ingredients to make the drink.
    
    for item in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    
    # Returns the total amount of money from coins inserted.
    
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


def make_coffee(drink):
    
    # Deducts the required ingredients from the resources.
    
    for item in MENU[drink]['ingredients']:
        resources[item] -= MENU[drink]['ingredients'][item]
    print(f"Here is your {drink} ☕. Enjoy!")

# ------------------------------
# Main Coffee Machine Loop
# ------------------------------
while True:
    choice = input("What would you like? (espresso/latte/cappuccino/report/exit): ").lower()

    if choice == "report":
        print_report()
    elif choice == "exit":
        print("Turning off the coffee machine. Goodbye!")
        break
    
    
    elif choice in MENU:
        drink = choice
        if is_resource_sufficient(drink):
            payment = process_coins()
            cost = MENU[drink]['cost']

            if payment < cost:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = round(payment - cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                resources['money'] += cost
                make_coffee(drink)
    else:
        print("Invalid choice. Please try again.")
