
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi<18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
elif 25 <= bmi < 29.9:
    print("overweight")

    