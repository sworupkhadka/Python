# print("Welcome to treasure island your mission is to find the treasure")
# choice1=input("choose weather you want to go left ot right : L or R \n ")

# if choice1 == L:                     # ❌ L not in quotes (must be "L")
#     #continue
#     input("you have come to a lake there is a island in the middle of the lake choose weather you want to swim or wait for a boat: S or W \n ")
#     # ❌ You never saved this input into choice2, but you used it below
#     if choice2 =="W":                # ❌ choice2 not defined yet
#         #continue
#         print("you arrived to the house unharmed there is a house at the middle of the island with 3 doors yellow red and blue choose one :Y , B or R: \n")
#         # ❌ You never saved the door choice into choice3, but you used it below
#         if choice3=="R":             # ❌ choice3 not defined yet
#             print("you rntered thr eoom full of fire.game over")
#         elif choice3=="Y":
#             print("you found the treasure you win")
#         elif choice3=="B":
#             printf("you choose the room full of water you lose")  # ❌ Python has no printf()
#         else:
#             print("choose either B Y or R")
        
#     else:
#         print("you got attacked by a trout game over")
# if choice1 == R:                     # ❌ R not in quotes (must be "R")
#     print("you fell into a hole game over")
# else:
#     print("choose L or R")




#correct version 

print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice1 = input("Choose whether you want to go left or right: L or R \n")

if choice1 == "L":  # ✅ Quotes added
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. "
                    "Do you want to swim or wait for a boat? S or W \n")  # ✅ saved input into choice2

    if choice2 == "W":  # ✅ now choice2 exists
        choice3 = input("You arrived at the island unharmed. "
                        "There is a house with 3 doors: Yellow, Red, and Blue. "
                        "Choose one: Y, B, or R \n")  # ✅ saved input into choice3

        if choice3 == "R":
            print("You entered the room full of fire. Game Over.")  # ✅ spelling cleaned
        elif choice3 == "Y":
            print("You found the treasure! You win!")
        elif choice3 == "B":
            print("You chose the room full of water. You lose.")  # ✅ print() instead of printf()
        else:
            print("Choose either B, Y, or R.")
    else:
        print("You got attacked by a trout. Game Over.")

elif choice1 == "R":  # ✅ Quotes added
    print("You fell into a hole. Game Over.")
else:
    print("Please choose L or R.")

