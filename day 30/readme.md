#  Python Exception Handling Examples

This repository contains examples demonstrating exception handling in Python, including try, except, else, finally, raising custom exceptions, and handling common errors like FileNotFoundError, KeyError, and IndexError.

---

## Table of Contents
- File Handling with Exceptions
- Dictionary Key Handling
- List Index Handling
- Raising Custom Exceptions
- BMI Example with Validation

---
## File Handling with Exceptions
- Demonstrates opening a file that may not exist.
- Uses FileNotFoundError to create the file if it does not exist.
- Uses finally to ensure the file is always closed.

```
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdsfa"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("the file was closed")
```
---

## Dictionary Key Handling
- Handles missing dictionary keys using KeyError.
- Prevents crashes when accessing nonexistent keys.
```
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes += post["Likes"]
        except KeyError:
            pass
    return total_likes

print(count_likes(facebook_posts))
```

---

## List Index Handling
- Handles invalid list indices using IndexError.
- Prints a default output instead of crashing.
```
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")

make_pie(4)
```
---
## Raising Custom Exceptions
- Demonstrates raising an exception manually when a value is unrealistic.
- Example: limiting human height in BMI calculation.
```
height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 4:
    raise ValueError("Human height should be less than 4 meters")

bmi = weight / height ** 2
print(bmi)
```
---
### Notes
```
- try block: code that might raise an exception.
- except block: handles specific exceptions.
- else block: runs if no exception occurs.
- finally block: always runs (for cleanup like closing files).
- raise: manually triggers an exception.
```