'''private attributes and methods are used to hide data and internal logic from outside access — a concept called encapsulation. they are meant to be
used only within the class and are not accessible from outside the class

1. Private Attributes
A private attribute is one that cannot be accessed directly from outside the class.
It’s created by prefixing the attribute name with two underscores (__)

2. Private Methods
A private method is a method meant to be used only inside the class, not from outside.
You make a method private by starting its name with __ as well. '''



class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no              # public attribute
        self.__acc_pass = acc_pass        # private attribute

    def reset_pass(self):
        print(self.__acc_pass)            # access private attr inside class

acc1 = Account("10000", "abcd")
print(acc1.acc_no)                        # works (public)
print(acc1.reset_pass())                  # prints password then None



#in simpler code
class Person:
    __name = "anonymous"       # private class attribute

    def __hello(self):          # private method
        print("hello person")

    def welcome(self):          # public method
        self.__hello()         # calls the private method

p1 = Person()
print(p1.welcome())           # prints "hello person" then None (method has no return)

