Day 5
<h3>## 🐍 For Loops, Ranges, and Basic Aggregations</h3>

This README explains how to use for loops, the range() function, and how to compute sums and maximums from lists.
It also covers the FizzBuzz exercise which combines loops and conditionals.

Table of Contents

For Loops

Iterating over Lists

Using Loop Variables in Expressions

Summing Values

Using sum()

Using Loops

Finding Maximums

Using max()

Using Loops

Using range() in Loops

Basic Ranges

Ranges with Steps

Sum of Numbers 1–100

FizzBuzz Game

For Loops
Iterating over Lists

A for loop lets you go through each item in a list:

fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)


Output:

apple
peach
pear

Using Loop Variables in Expressions

You can also use the loop variable inside your code block:

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")


Output:

apple
apple pie
peach
peach pie
pear
pear pie

Summing Values
Using sum()

The built-in sum() adds up all numbers in a list:

students_score = [100, 50, 100, 120]
total_score = sum(students_score)
print(total_score)


Output:

370

Using Loops

You can also sum values manually with a loop:

sum_scores = 0
for score in students_score:
    sum_scores += score
print(sum_scores)


Output:

370

Finding Maximums
Using max()

The built-in max() returns the largest value in a list:

print(max(students_score))


Output:

120

Using Loops for Max

You can also find the max value manually:

max_score = 0
for score in students_score:
    if score > max_score:
        max_score = score
print(max_score)


Output:

120

Using range() in Loops
Basic Ranges

The range() function generates numbers. By default, the end number is not included:

for number in range(1, 10):  # includes 1 but not 10
    print(number)


Output:

1
2
3
4
5
6
7
8
9

Ranges with Steps

You can specify a step to skip numbers:

for number in range(1, 11, 3):
    print(number)


Output:

1
4
7
10

Sum of Numbers 1–100

Using a loop to sum numbers from 1 to 100:

total = 0
for number in range(1, 101):
    total += number
print(total)


Output:

5050

FizzBuzz Game

The FizzBuzz challenge prints numbers from 1 to 100 but:

“Fizz” if divisible by 3

“Buzz” if divisible by 5

“FizzBuzz” if divisible by both 3 and 5

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


Sample Output:

1
2
Fizz
4
Buzz
Fizz
...
14
FizzBuzz
...