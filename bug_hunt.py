# BUG: The opening string quotation mark was not closed.
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: The variable was written as "nmae" instead of "name".
print("Nice to meet you, " + name)

age = input("How old are you? ")

# BUG: age from input() is a string, so it must be converted to int before adding 1.
age = int(age)
print("Next year you will be " + str(age + 1))
