try:
    file = open("a_file.txt")            # try opening file
    a_dictionary = {"key": "value"}      # simple dict
    print(a_dictionary["sdsfa"])         # will cause KeyError

except FileNotFoundError:
    file = open("a_file.txt", "w")       # create file if missing
    file.write("something")              # write default text

except KeyError as error_message:
    print(f"The key {error_message} does not exist")   # handle missing key

else:
    content = file.read()                # runs only if no error
    print(content)

finally:
    file.close()                         # always close file
    print("the file was closed")
    # raise KeyError                    # optional: raise your own error
