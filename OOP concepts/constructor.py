#a constructor is a special type of method that is automatically called when an object of a class is created.
# Its main purpose is to initialize the object's attributes (i.e., set up the initial state of the object)
#all classes have a functon called init() which is always executed when the class is being initiated


#creating a class
class Student:
    def __init__(self,name,marks):
        self.name =name                                          # The 'name' attribute is set to the value passed
        self.marks= marks
        print("adding new students in database")                 # Prints message when a new student is created

s1 = Student("sworup",78)                           # Creates a new Student object and calls __init__
print(s1.name,s1.marks)                                           #Prints the 'name' attribute of s1

s2=Student ("saurav",90)
print(s2.name,s2.marks)                                          #all the data stored inside the class are called attributed in this case name




#there are 2 types of constructors in python they are
'''1) Default constructors:
      default constructor is a constructor that does not take any parameters (except self).
      It initializes the object with default values.
      def __init__ (self)
      passn
      
   2) Parameterized constructor:
      parameterized constructor is a constructor that takes arguments to initialize an object with specific values.
      just like above
      
    '''