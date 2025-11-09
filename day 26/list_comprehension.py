#list comprehension 

num=[1,2,3]
new_numbers=[n+1 for n in num]
print(new_numbers)


#finding square of numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n** 2 for n in numbers ]
print(squared_numbers)


#filtering out even nos 
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n%2 == 0]
print(result)