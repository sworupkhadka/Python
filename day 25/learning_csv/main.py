import pandas as pd  # import pandas

# ----------------------------
# Section 1: Read CSV data
# ----------------------------
data = pd.read_csv("weather_data.csv")

# Convert DataFrame to dictionary
data_dict = data.to_dict()
print(data_dict)

# Convert column to list
temp_list = data["temp"].to_list()
print(temp_list)

# ----------------------------
# Section 2: Basic stats
# ----------------------------
# Average temperature
average = sum(temp_list) / len(temp_list)
print(average)

# Using pandas mean()
print(data["temp"].mean())

# Maximum temperature
print(data["temp"].max())

# ----------------------------
# Section 3: Accessing columns
# ----------------------------
print(data["condition"])
print(data.condition)

# ----------------------------
# Section 4: Accessing rows
# ----------------------------
# Rows where day is Monday
print(data[data.day == "Monday"])

# Row with max temperature
print(data[data.temp == data.temp.max()])

# Convert Monday temp to Fahrenheit
monday = data[data.day == "Monday"]
celcius = monday.temp
farenhite = (celcius * 9/5) + 32
print(farenhite)

# ----------------------------
# Section 5: Create DataFrame from scratch
# ----------------------------
students_dict = {
    "students": ["amy", "ram", "shyam"],
    "scores": [30, 40, 50],
    "age": [21, 22, 22]
}

students_data = pd.DataFrame(students_dict)
print(students_data)

# Save to CSV
students_data.to_csv("new_data.csv")
