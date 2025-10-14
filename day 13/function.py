def my_function():
    for i in range(1,20):
        if i==20:
            print("you got it")
            
my_function()

#this does not give the result as the range does not include 20 so to get 20
#we need to take the range range (1,21) like 

def my_function():
    for i in range(1,21):
        if i==20:
            print("you got it")
            
my_function()

#and we get output you got it 