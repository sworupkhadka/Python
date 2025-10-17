'''Abstraction in Python (or programming) means hiding the complicated details and showing only what is necessary to the user.
You only see what the object can do, not how it does it.
Focus is on “what”, not “how”.

Example:
When you start a car, you just press the start button.
You don’t need to know how the engine, clutch, or brakes work internally
✅ Abstraction = hiding complexity and showing only the essential features.'''


class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.brk=True
        print("car started ....")

car1=Car()
car1.start()