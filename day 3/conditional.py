print("welcome to the roller coaster ")
height=int(input("please enter your height in cm: \n"))

if height >= 120:
    print("you can ride the rollercoaster")
else:
    print("you cant ride te rollercoaster")


# use of different operations
# >= greater then equale to
# <= less then equal to 
# == equales to 
# not equale to 



# now say that there is a problem only thw ones with height greater then 120 can ride the rollercoaster
# ans if height is greather then 120 then they should be prices as per age greater then 12 say $10
# less then 12 then they shall be charged $5 to solve this 
# we take another if else statement within a if else like

#make note that python uses elif instead of elseif


print("Welcome to the roller coaster ")
height = int(input("Please enter your height in cm: \n"))

if height >= 120:
    print("You can ride the rollercoaster")
    
    age = int(input("Enter your age: "))
    if age > 18:
        print("You have to pay $12")
    elif age > 12 and age <= 18:  # elif instead of elseif
        print("You have to pay $7")
    else:
        print("You have to pay $5")

else:
    print("You can't ride the rollercoaster")
