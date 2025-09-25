# say roller coaster ride with age and hright but also ask if you want a photo 
# is yes then charge extra $3 on top

print("Welcome to the roller coaster ")
height = int(input("Please enter your height in cm: \n"))

if height >= 120:
    print("You can ride the rollercoaster")
    
    age = int(input("Enter your age: "))
    if  18 <= age < 45:
        bill=12
        print("your tickets are $12")
    elif age > 12 and age <= 18:  # elif instead of elseif
        bill=7
        print("your tickets are  $7")
    elif age <12 :
        bill=5
        print("your tickets are  $5")
    elif  45 <= age <= 55:
        bill=0
        print("your entry is free")

want_photo=input("do you want a photo taken > type y for yes n for no:\n")
if want_photo =="y":
    bill +=3       #add $3 to bill
    print(f"your final bill is ${bill}")       #fstring
    
    
else:
    print("You can't ride the rollercoaster")
