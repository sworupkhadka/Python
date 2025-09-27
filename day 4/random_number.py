#most widely method used in python to generate random number is 
#say btn 0 to 1

import random

# Most widely used method to generate random number between 0 and 1
random_number_0_to_1 = random.random()  # 0.0 ≤ x < 1.0
print(random_number_0_to_1)

# For a floating point number between 1.0 and 10.0
random_float = random.uniform(1.0, 10.0)
print(random_float)


#heads or tails
random_integer = random.randint(0,1)
if random_integer ==0:
    print("heads")
else :
    print("tails")




# output
# 0.2934852051055844
# 8.330870946471272
# heads
