# Python List/Dictionary Comprehension
---

#### This repository contains Python exercises with explanations, inline comments, and examples covering:

- List comprehension
- Dictionary comprehension
- File handling
- Pandas DataFrame iteration

- NAO phonetic alphabet

---
## Table of Contents

- List Comprehension
- Dictionary Comprehension
- Squaring Numbers in a List
- Filtering Even Numbers from a List
- Data Overlap – Common Numbers from Two Files
- Dictionary Comprehension – Word Lengths
- Dictionary Comprehension – Celsius to Fahrenheit
- Pandas – Iterating Through DataFrame Rows
- NATO Phonetic Alphabet Exercise
---

## List Comprehension

**Definition:** Concise way to create lists in Python.

[expression for item in iterable if condition]


### Example: Squaring numbers
```
numbers = [1, 2, 3, 4, 5]                # Original list
squared_numbers = [n ** 2 for n in numbers]  # Square each number
print(squared_numbers)                   # Output squared 
```
```
Input	
[1,2,3,4,5]	

Output
[1,4,9,16,25]
```
---


## Dictionary Comprehension

**Definition:** Creates dictionaries concisely.
```
Syntax:
{key_expression: value_expression for item in iterable if condition}
```

#### Example: Word lengths
```
sentence = "What is Python"
result = {word: len(word) for word in sentence.split()}  # key=word, value=length
print(result)
```
```
Input	
"What is Python"	

Output
{'What':4,'is':2,'Python':6}
```
---
## Squaring Numbers in a List
```
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]  # Square each number
print(squared_numbers)
```
```
Input	
[1,1,2,3,5,8,13,21,34,55]	

Output
[1,1,4,9,25,64,169,441,1156,3025]
```
---
## Filtering Even Numbers from a List
```
list_of_strings = ['9','0','32','8','2','8','64','29','42','99']
numbers = [int(n) for n in list_of_strings]      # Convert strings to int
result = [n for n in numbers if n % 2 == 0]     # Keep even numbers
print(result)
```
```
Input	
['9','0','32','8','2','8','64','29','42','99']	

Output
[0,32,8,2,8,64,42]
```
---
## Data Overlap – Common Numbers from Two Files

```
with open("file1.txt") as file1:
    file1_data = file1.readlines()
with open("file2.txt") as file2:
    file2_data = file2.readlines()

# Find numbers present in both files and convert to integers
result = [int(num.strip()) for num in file1_data if num in file2_data]
print(result)

```
```
file1.txt		
3,6,5,8,33,12,7,4,72,2,42	

file2.txt 
3,6,13,5,7,89,12,3,33,34,1,344

Output
[3,6,5,33,12,7,42]
```
---
## Dictionary Comprehension – Word Lengths

```
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}  # key=word, value=length
print(result)
```
```
Input Sentence	
"What is the Airspeed Velocity of an Unladen Swallow?"	

Output
{'What':4,'is':2,'the':3,'Airspeed':8,'Velocity':8,'of':2,'an':2,'Unladen':7,'Swallow?':8}
```
--- 
## Dictionary Comprehension – Celsius to Fahrenheit
```
weather_c = {
    "Monday": 12, "Tuesday": 14, "Wednesday": 15,
    "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24
}
weather_f = {day: (temp_c*9/5)+32 for (day,temp_c) in weather_c.items()}  # Convert C → F
print(weather_f)
```
```
Input (Celsius)	
{"Monday":12,"Tuesday":14,...}	

Output (Fahrenheit)
{'Monday':53.6,'Tuesday':57.2,...}
```

---
## Pandas – Iterating Through DataFrame Rows
```
import pandas as pd

student_dict = {"student": ["sam","ram","hari"], "score": [20,30,40]}
student_data_frame = pd.DataFrame(student_dict)

for index,row in student_data_frame.iterrows():  # Loop rows
    print(f"Student: {row.student}, Score: {row.score}")
```
```
Input DataFrame	
student=['sam','ram','hari'], score=[20,30,40]	

Output
Student: ram, Score: 30
Student: hari, Score: 40
```
---
## NATO Phonetic Alphabet Exercise
```
nato_dict = {
    "A":"Alfa","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot",
    "G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima",
    "M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo",
    "S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey",
    "X":"X-ray","Y":"Yankee","Z":"Zulu"
}

word = input("Enter a word: ").upper()                     # Convert input to uppercase
phonetic_list = [nato_dict[letter] for letter in word]     # Convert letters → NATO codes
print(phonetic_list)

```
```
Input	
cat	

Output
['Charlie','Alfa','Tango']
```

### Author
**Sworup Khadka** – Python practice projects in File comprehension, Dictionary comprehension