# Define basic arithmetic functions

def add(n1, n2):
    # Returns the sum of two numbers
    return n1 + n2

def subtract(n1, n2):
    # Returns the difference of two numbers
    return n1 - n2

def multiply(n1, n2):
    # Returns the product of two numbers
    return n1 * n2

def divide(n1, n2):
    # Returns the division of two numbers
    return n1 / n2


# Add the functions to a dictionary for easy lookup
# Keys are operator symbols, values are function references
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Main calculator function
def calculator():
    should_accumulate = True  # Controls the loop for continued calculation

    # Ask user for the first number
    num1 = float(input("What is the first number?: "))

    # Loop to allow repeated calculations
    while should_accumulate:

        # Display available operations
        for symbols in operations:
            print(symbols)

        # Ask user to pick an operation
        operator_symbol = input("Pick an operation: ")

        # Ask user for the second number
        num2 = float(input("What is the second number?: "))

        # Perform the chosen operation using the dictionary
        # operations[operator_symbol] returns a function reference
        # Then we call it with (num1, num2)
        answer = operations[operator_symbol](num1, num2)

        # Print the result
        print(f"{num1} {operator_symbol} {num2} = {answer}")

        # Ask user if they want to continue with the current result
        choice = input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ")

        if choice.lower() == "y":  # Continue with current result
            num1 = answer
        else:
            should_accumulate = False  # Exit the loop
            print("\n" * 20)          # Clear screen for new calculation
            calculator()               # Restart calculator from scratch


# Start the calculator program
calculator()
