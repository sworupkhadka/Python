sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)


'''.split()  is used to split a string into a list of words (or parts)
sentence = "I love Python"
words = sentence.split()
print(words)
output
['I', 'love', 'Python']'''