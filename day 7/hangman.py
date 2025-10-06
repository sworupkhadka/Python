word_list=["aardvark","baboon","camel"]

import random
chosen_word=random.choice(word_list)        #choosing a word from above
print(chosen_word)                          #printing the choice


placeholder=""                              #empty string


word_length=len(chosen_word)                #choose a word and give ____as per word length
for position in range(word_length):
    placeholder += "_"
    print(placeholder)

guess=input("guess a letter:").lower()     #let user guess a word in the letter
print(guess)

display=""

for letter in chosen_word:                 #check is the letter guessed is right or wrong
    if letter == guess:
        display += letter
    else:
        display += "_"
        
print(display)