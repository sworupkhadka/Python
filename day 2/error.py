# use of type error, type checking and type conversion 

len("12345")      #gives error if no ""
#length function doesnt want to work with integer so length function expects datatype
# so this gives error 

#so we pass it as string using ""
len ('12345')


#TYPE CHECKING 

print(type("hello"))
#this gives data type op" <class 'str'>

print(type(123))
#op:<class 'int'>

print(type(3.142))
#op:<class 'float'>

print(type(True))
#op:<class 'bool'>


#TYPE COVERSION

print("123" + "456")
#gives output 123456

print(int("123")+int("456"))
#this gives sum 579


#exercise

# print("number of letters in your name : " + len(input("enter your name:\n")))
# this gives error as:
#     print("number of letters in your name : " + len(input("enter your name:\n")))
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TypeError: can only concatenate str (not "int") to str

name=input("enter your name:\n")
length=len(name)

print(type(name))           #str
print(type(length))         #int

#we cannot concatenate int and string so we use type conversion 

print("number of letters in your name: " + str(length))




