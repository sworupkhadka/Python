'''Python OOP, __del__ is a destructor method —
it’s a special method that gets called automatically when an object is about to be destroyed
 (i.e., when it’s no longer in use or explicitly deleted).'''

class Student:
    def __init__(self,name):
        self.name=name

s1=Student("sworup")
print(s1.name)                    #here the name is printed normally it gives sworup

#now let us use del keyword
del s1
print(s1.name)                   #now this gives error as s1 is already deleted
