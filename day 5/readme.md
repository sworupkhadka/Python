<h2>Day 5</h2>
<h5>  For Loops, Ranges, and Aggregations</h5>

---
This README demonstrates the use of for loops in Python, iterating over lists, using the range() function, calculating sums and maximum values, and implementing the classic FizzBuzz game.

---

Table of Contents

---
For Loops

Iterating over Lists

Using Loop Variables in Expressions

Summing Values

Using sum()

Using Loops


Finding Maximum Values

Using max()

Using Loops for Max

Using range() in Loops

Basic Ranges

Ranges with Steps

Sum of Numbers 1–100

FizzBuzz Game

For Loops
Iterating over Lists

For loops allow you to go through each item in a list:

fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)


Output:

apple
peach
pear

Using Loop Variables in Expressions

You can also use the loop variable to create new outputs:

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

The built-in sum() function adds up all numbers in a list:

students_score = [100, 50, 100, 120]

total_score = sum(students_score)
print(total_score)


Output:

370


Note: sum() is the fastest and simplest way to add up all values in an iterable.

Using Loops

You can also calculate the sum manually with a loop:

sum_scores = 0
for score in students_score:
    sum_scores += score
print(sum_scores)


Output:

370

Finding Maximum Values
Using max()

The built-in max() function returns the largest value in a list:

print(max(students_score))


Output:

120

Using Loops for Max

We can also determine the maximum manually:

max_score = 0
for score in students_score:
    if score > max_score:
        max_score = score
print(max_score)


Output:

120


Tip: Start max_score with 0 or the first element of the list to avoid errors.

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