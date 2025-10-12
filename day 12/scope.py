enemies = 1

def increase_enemies():                         #defining a function
    enemies = 2
    print(f" enemies inside the function are {enemies}")
increase_enemies()                              #calling the function 
print(f"enemies outside the functions are {enemies}")



#local slope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()

# print(potion_strength)
#this will give error ad the potion_strength is local scope 

#global scope
player_health=10

def drink_potion():
    potion_strength=2
    print(player_health)
drink_potion() 


