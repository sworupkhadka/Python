'''This exercise is HARD 
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
You are going to create a list called result which contains the numbers that are common in both files. 
e.g. if file1.txt contained: 
1 
2 
3
and file2.txt contained: 
2
3
4
result = [2, 3]
IMPORTANT:  The output should be a list of integers and not strings!
Try to use List Comprehension instead of a Loop. '''


# Open and read all lines from file1.txt
with open("file1.txt") as file1:
    file1_data = file1.readlines()

# Open and read all lines from file2.txt
with open("file2.txt") as file2:
    file2_data = file2.readlines()

# Create a list of numbers common in both files (convert to int)
result = [int(num) for num in file1_data if num in file2_data]

print(result)
