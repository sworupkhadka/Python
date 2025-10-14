#  Day 13: Debugging in Python

##Objective
Today we learned how to **debug Python programs** — that means finding and fixing bugs (errors) in our code so that it runs correctly and produces the expected output.

##  What We Practiced
- Reading and understanding **error messages** in Python.  
- Using **print statements** to trace code execution.  
- Identifying **logical errors** (code runs but gives wrong results).  
- Step-by-step fixing instead of rewriting the whole program.

##  Example: Fixing FizzBuzz
We debugged a program that was supposed to print numbers from 1 to `x` with these rules:
- Print `"Fizz"` if the number is divisible by 3.  
- Print `"Buzz"` if divisible by 5.  
- Print `"FizzBuzz"` if divisible by both 3 and 5.

###  Original Buggy Code
```python
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])
✅ Debugged and Fixed Code
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

✅ Debugged and Fixed Code
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

Key Takeaways

-Debugging is like detective work — look for clues in error messages
-Always test your code with different inputs.
-Fix one problem at a time instead of rewriting everything.
-Logical bugs don’t always throw errors — sometimes you have to think through the logic carefully.

Summary

By the end of this lesson, we learned how to:
-Read and interpret Python errors
-Identify logical and syntax mistakes.
-Fix our code systematically.
-Gain confidence in debugging our own programs!


