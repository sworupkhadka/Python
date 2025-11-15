# this is used when the value is not normal and you want to raise exception
#eg in bmi calculation say the tallest a person can be is 4 meters but the input is more them 4 meters this will be unrealistic so we use raise_exception method

height = float(input("Height:"))          # get height input
weight = int(input("Weight:"))            # get weight input

if height > 4:
    raise ValueError("human height should be less than 4 meters")  # unrealistic height

bmi = weight / height ** 2                 # calculate BMI
print(bmi)                                 # print BMI
