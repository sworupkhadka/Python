#modifying global scope

#global variable
enemies = 1

#defining a function
def increase_enemies():           
    #to be able to modify global variables we need to specify that we are 
    #using one  like
    global enemies
    enemies += 1
    print(f" enemies inside the function are {enemies}")
    
#calling the function 
increase_enemies()       
print(f"enemies outside the functions are {enemies}")