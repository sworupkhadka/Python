#static methods are those methods that dont use the self parameter they work at class level
#for that we use decorator i.ir @staticmethod

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

# Calling static method using class
print(Calculator.add(5, 10))  # Output: 15

# Calling static method using object
calc = Calculator()
print(calc.add(7, 3))          # Output: 10
