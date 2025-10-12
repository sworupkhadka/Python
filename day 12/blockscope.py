#there is no block scope in python

game_level=3
enemies=["skeleton",  "zombies", "alien"]


def create_enemy(_):
    if game_level<5:
        new_enemy= enemies[0]
    
    print(new_enemy)            
#when inside a function he print statement should be 
# indented within the function