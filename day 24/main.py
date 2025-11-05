# Reading from a file
with open("my_file.txt") as file:
    # "/users/sworup/desktop/my_file.txt" path when the file is in desktop
    contents = file.read()
    print(contents)
# This prints "hello my name is sworup" which are contents in diff file my_file.txt


# Writing to a file
with open("my_file.txt", mode="w") as file:
    # w is write (default is read)
    # r is read which is default
    # a is append
    file.write("new text")
# This removes old text which was "hello my name is sworup" and just prints "new text"


# Appending to a file
with open("my_file.txt", mode="a") as file:
    file.write(" hello")
# This appends to existing text - result: "new text hello"


# Be sure to comment out part 1 of reading from a file while write and append
# and whenever want to work on read comment out write and append