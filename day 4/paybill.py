# here are 5 friends who need to pay bill generate a random name to pay bill

friends=["a","b","c","d","e"]

import random
random_integer = random.randint(0,4)
if random_integer == 0:
    print("a")
elif random_integer == 1:
    print("b")
elif random_integer == 2:
    print("c")
elif random_integer == 3:
    print("d")
else:
    print("e")
