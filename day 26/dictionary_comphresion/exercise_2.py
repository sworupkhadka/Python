weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)



'''Create a dictionary comprehension:
day → key (day of the week)
temp_c → value (temperature in Celsius)
weather_c.items() → gets each (key, value) pair from weather_c
(temp_c * 9/5) + 32 → converts Celsius to Fahrenheit
for (day, temp_c) in weather_c.items()
weather_c.items() → returns all key-value pairs from the dictionary as tuples:

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}'''
