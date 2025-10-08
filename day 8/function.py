def greet():                            #defining a function
    print("hello")
    print("how do u do")
    print("im fine")
    
greet()                                 #calling a function



def greet_with_name(name):
    print(f"hello {name}")
    print(f"how do u do {name}")
    print("im fine")
greet_with_name("sk")



#functions with more than 1 inputs
def greet_with(name, location):
    print(f"hello {name}")
    print(f"how is it like in {location}")
greet_with(name="sk", location="pokhara")

#or can just write
greet_with("sk", "Pokhara")   
#but this results in error if pokhara and sk positions are swapped
