#range with a for loop

for number in range (1,10): #including 1 not 10
    print(number)  
    
#gives output 1 to 9
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# also we can use range function to print number in a predefined intervals like

for number in range (1, 11, 3):
    print(number)
    
# this gives output from 1 to 11 not including 11 in interval of 3 like
# 1
# 4
# 7
# 10


#sum of nos from 1 to 100
total=0
for number in range (1,101):
    total += number
print(total)
