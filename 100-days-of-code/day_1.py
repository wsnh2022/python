####################################################################################
# What I Learned on Day 1:
# 1. Print Modifiers:
#    - Using `print()` for output.
#    - Adding newlines, concatenating strings, and repeating strings.
# 2. Input Function:
#    - Accepting user input and concatenating it with other strings.
#    - Converting input to integers for calculations.
# 3. len() Function:
#    - Calculating the length of strings using `len()`.
# 4. Variables and Value Swapping:
#    - Assigning variables and swapping their values using a temporary variable.
# 5. Project: Band Name Generator:
#    - Using input and string concatenation for a fun project.
####################################################################################

## ------------------------ lesson 1 ---------------------------------------
## ====== Print Modifiers

# Simple greeting using the print function
print("Hello World!")  # Displays a message on the console

# Advanced printing examples
print('Top "Heaven"\nMiddle "Earth"\nBottom "Hell"')  # Demonstrates escape sequences
print("Hello world\n" * 3)  # Prints "Hello world" three times
print("Hello" + "world")  # Concatenates strings without spaces
print("Hello" + " " + "world")  # Concatenates strings with spaces
print("Hello " + "world")  # Another way to concatenate strings with spaces

# Line continuation for better readability in long strings
long_string = "This is a very long string that \
continues on multiple lines for readability."
print(long_string)

## ------------------------ lesson 2 --------------------------------------
## ====== Input Function

# Greeting the user with their name using input
print("Hello " + input("What is your name?\n") + "!")

# Multiplying two numbers input by the user
n1 = int(input("Enter 1st number to multiply: "))
n2 = int(input("Enter 2nd number to multiply: "))
print(f"{n1} x {n2} = {n1 * n2}")  # Using f-strings for formatted output

## ------------------------ lesson 3 --------------------------------------
## ====== len() Function

# Finding the length of a string
print(len("Angela"))  # Outputs the length of the string "Angela"

# Prompting the user to input a string and finding its length
print(len(input("Type any text to find its length:\n")))

## ------------------------ lesson 4 --------------------------------------
## ====== Variables and Swapping Values

# Swapping values of two variables
glass1 = "milk"
glass2 = "juice"

# Using a temporary variable to swap
temp = glass1
glass1 = glass2
glass2 = temp

print("glass1 = " + glass1 + "\n" + "glass2 = " + glass2)

## ------------------------ Project: Band Name Generator -----------------

# Greeting the user
print("Welcome to the Band Name Generator!!!")

# Asking for user input to create a band name
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")

# Combining inputs to generate a band name
print("Your band name could be " + city + " " + pet)
