print("Welcome to Domino's")

size = input("What size of pizza do you want? S, M or L:\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N:\n")

bill = 0  # initialize bill

# price as per size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Please type S, M or L")

# adding pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2   
    else:
        bill += 3   

# adding extra cheese
if extra_cheese == "Y":  
    bill += 1

print(f"Your final bill amount is ${bill}")
