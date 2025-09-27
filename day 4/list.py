
states_of_nepal=["gandaki", "bagmati", "sudurpaschim"]
print(states_of_nepal[0])
print(states_of_nepal[1])
print(states_of_nepal[2])

# output
# gandaki
# bagmati
# sudurpaschim

# if you use [-1] then you get the last item in the list ]

print(states_of_nepal[-1])

# output
# gandaki
# bagmati
# sudurpaschim
# sudurpaschim


# also can edit data say 

states_of_nepal[1]="bungamati"
print(states_of_nepal[1])

# output
# gandaki
# bagmati
# sudurpaschim
# sudurpaschim
# bungamati

# to extend the list use 
states_of_nepal.extend(["lumbini", "karnali"])
print(states_of_nepal)

# output
# gandaki
# bagmati
# sudurpaschim
# sudurpaschim
# bungamati
# ['gandaki', 'bungamati', 'sudurpaschim', 'lumbini', 'karnali']


# #index errors
# print(states_of_nepal[6])

# this gives error as there are only 5 lists given so it gives
#  print(states_of_nepal[6])
#           ~~~~~~~~~~~~~~~^^^
# IndexError: list index out of range


# so to solve this and get last state name of the list we can also use 


no_of_states= len(states_of_nepal)
print(states_of_nepal[no_of_states-1])

# output
# karnali