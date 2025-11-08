#  Learning Pandas
This repository contains Python practice exercises covering data handling with pandas, creating and saving CSV files, and interactive graphics with Turtle. These projects were developed during learning sessions in November 2025.

---

## Table of Contents

- Pandas: Accessing and Analyzing Data
- Creating DataFrames from Scratch
- Saving and Loading CSV Files
- US States Game with Turtle
- Common Issues & Fixes

---
## Pandas: Accessing and Analyzing Data
- Example: Reading a CSV
```
import pandas as pd
data = pd.read_csv("weather_data.csv")
print(data)                # prints entire dataset
print(data["temp"])        # prints the 'temp' column
```
---
## Convert DataFrame to dictionary
```
data_dict = data.to_dict()
print(data_dict)
```

---
## Convert column to list
```
temp_list = data["temp"].to_list()
print(temp_list)
```

## Basic statistics
```
average = sum(temp_list)/len(temp_list)
print(average)

print(data["temp"].mean())   # using pandas method
print(data["temp"].max())    # maximum temperature
```
---

## Accessing Rows
---
### Get row where day is Monday
```
monday = data[data.day == "Monday"]
print(monday)
```
### Get row with max temperature
```
print(data[data.temp == data.temp.max()])
```
### Convert Celsius to Fahrenheit

```
farenhite = monday.temp * 9/5 + 32
print(farenhite)
```
---

## Creating DataFrames from Scratch
```
import pandas as pd

data_dict = {
    "students": ["amy", "ram", "shyam"],
    "scores": [30, 40, 50],
    "age": [21, 22, 22]
}

df = pd.DataFrame(data_dict)
print(df)

# Save to CSV
df.to_csv("new_data.csv", index=False)
```
---
## Notes:
```
pd.DataFrame(data_dict)                  converts a dictionary of lists into a table.
index=False                             prevents pandas from adding an extra index column 
```
---

### Saving and Loading CSV Files
### Reading a CSV:
```
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
```

### Saving a DataFrame:
```
df.to_csv("squirrel_count.csv", index=False)
```

### Common mistake:
```
df.to_csv = ("squirrel_count.csv")  # ❌ This overwrites the function

```
#### Use parentheses to call the function:
```
df.to_csv("squirrel_count.csv")
```
---
### US States Game with Turtle
##### Setup:
```
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

t = turtle.Turtle()
t.hideturtle()
t.penup()

Game Loop:
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )
    if answer_state is None:  # exit option
        break

    answer_state = answer_state.title()
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Arial", 10, "normal"))

screen.exitonclick()
```
---

### Notes:

- .title() ensures capitalization matches CSV.

- Use one Turtle object to write all states.

- Check column names in CSV (state, x, y) match your code.

- Common Issues & Fixes

- ModuleNotFoundError: No module named 'pandas'

- Ensure virtual environment is activated:

- source env/bin/activate

---

### Install pandas:

#### Terminal 
```
python -m pip install pandas
```
#### Run script using environment Python:
```
python main.py
pip command not found
```
#### Use Python to call pip:
```
python3 -m ensurepip --upgrade
python3 -m pip install pandas
```

### Author

Sworup Khadka – Python practice projects in data handling, CSVs, and interactive graphics with Turtle.