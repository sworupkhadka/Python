programming_dictionary = {
    "Bug": "this ia s bug",
    "Function" : "part of a code",
    "Loop" : "do a part over and over again"
}

print(programming_dictionary["Bug"])



#to add a data into a dictionary we can do it by

programming_dictionary["Snippet"] = "a specific part of code"
#this adds the Snippet to the dictionary

print(programming_dictionary)


#we can wipe out a entire dictionary we can using empty_dictionary{} like

# programming_dictionary={}       
# #this empties out the dictionary  
# print(programming_dictionary)


#to edit an item in a dictionary 
programming_dictionary["Bug"]= "a moth in your computer"             #this overwrites the text this is a bug
print(programming_dictionary)


#loop through a dictionary 
for thing in programming_dictionary:
    # print(thing)                             #gives keys bug, function, loop, snippet
#to get the values too we can use 
    print(thing)
    print(programming_dictionary[thing])