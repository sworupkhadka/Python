# Define the first function named 'function_1'
# It simply returns the text it receives (no changes)
def function_1(text):
    return text

# Define the second function named 'function_2'
# It converts the input text to title case (first letter of each word capitalized)
def function_2(text):
    return text.title()

# Call function_1 first with "hello" → returns "hello"
# Then pass that result into function_2 → converts to "Hello"
#in simple words output of function 1 is input of function 2
output = function_2(function_1("hello"))

# Print the final result to the console
print(output)
