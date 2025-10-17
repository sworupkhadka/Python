#an attribute is a variable that belongs to an object or a class.
# Attributes are used to store data or properties related to the object.

class Student:
    college_name = "ABC college"  # Class attribute (shared by all students)

    def __init__(self, name, marks):  # Constructor
        self.name = name             # Object (instance) attribute
        self.marks = marks           # Object (instance) attribute

    def welcome(self):               # Method
        print("welcome student", self.name)

    def get_marks(self):             # Method
        return self.marks

s1 = Student("karan", 97)           # Create an object s1
s1.welcome()                         # Call the welcome() method
print(s1.get_marks())                # Call get_marks() method and print marks

