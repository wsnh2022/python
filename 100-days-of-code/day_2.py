####################################################################################
# What I Learned on Day 2:
# 1. Python Operators:
#    - Arithmetic operators for calculations and their precedence.
# 2. Index Slicing and Data Types:
#    - Extracting substrings using indexing and working with data types.
# 3. Mathematical Operations:
#    - Understanding PEMDAS (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction).
# 4. String Manipulation and Conversion:
#    - Converting between data types: strings, integers, and floats.
# 5. Projects:
#    - BMI Calculator: Calculate BMI from user input.
#    - Life in Weeks: Estimate weeks left to live based on age.
#    - Tip Calculator: Split a bill among friends and calculate tips.
####################################################################################

## ================== Python Operators ==================

# Arithmetic operators for basic calculations
print(2 + 3)                     # addition(+)
print(3 - 1)                     # subtraction(-)
print(2 * 3)                     # multiplication(*)
print(3 / 2)                     # division(/)
print(3 ** 2)                    # exponential(**)
print(3 % 2)                     # modulus(%)
print(3 // 2)                    # floor division operator(//)

# Checking data types using `type()`
print(type(10))                  # Int
print(type(734_529.678))         # Float (underscore for readability)
print(type(1 + 3j))              # Complex number
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name': 'Asabeneh'}))# Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

## -------- Index slicing strings from variables --------

strings = "Hello"
print(strings[0])  # First character (H)
print(strings[-1]) # Last character (o)
print(strings[4])  # Fifth character (o)
print(strings[0:5])# Substring (Hello)

# Quiz: Index mapping
street_name = "Abbey Road"
print(street_name[4] + street_name[7])  # Output: "yR"

# Integer vs String
print("123" + "456")  # String concatenation: 123456
print(123 + 456)      # Integer addition: 579

# Float
print(123.45)         # Float value with decimal point

# Boolean values
print(True)
print(False)

## -------- Conversions --------

my_chr = len(input("What is your name?\n"))
print(type(my_chr))          # Type is `int` (length of string)

# Convert between types
a = 123                    # int
a = str(123)               # Convert to string
a = float(123)             # Convert to float
print(type(a))

print(70 + float("100.5")) # Output: 170.5
print(str(100) + str(150)) # Output: 100150 (int to str)

## ================== PEMDAS ==================

# PEMDAS stands for:
# P: Parentheses () - Highest precedence; solve expressions inside parentheses first.
# E: Exponents ** - Solve powers or roots next.
# MD: Multiplication (*) and Division (/) - Process left to right at the same precedence level.
# AS: Addition (+) and Subtraction (-) - Lowest precedence, also left to right.

# Python strictly follows PEMDAS to evaluate mathematical expressions.
# Example to demonstrate PEMDAS:
print(3 * 3 + 3 / 3 - 3)  # Output: 7.0
# Breakdown:
# 1. Multiplication: 3 * 3 = 9
# 2. Division: 3 / 3 = 1
# 3. Addition: 9 + 1 = 10
# 4. Subtraction: 10 - 3 = 7

# Use parentheses to change the order of operations:
print(3 * (3 + 3) / 3 - 3)  # Output: 3.0
# Breakdown:
# 1. Parentheses: 3 + 3 = 6
# 2. Multiplication: 3 * 6 = 18
# 3. Division: 18 / 3 = 6
# 4. Subtraction: 6 - 3 = 3

# Reference:
# - PEMDAS is an acronym commonly taught in schools for understanding operator precedence.
# - In Python, operations at the same precedence level (e.g., Multiplication and Division) are evaluated **left to right**.

## ================== Challenges ==================

## Challenge 1: Add digits of a two-digit number
two_digit_number = input("Type a two-digit number: \n")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

## Challenge 2: BMI Calculator
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# Convert inputs and calculate BMI
bmi = int(weight) / (float(height) ** 2)
print(int(bmi))  # Display BMI as an integer

## ================== String Formatting and F-Strings ==================

# F-strings for formatted output
score, height, isWinning = 0, 1.8, True
print(f"Your score is {score}, your height is {height}, you are winning: {isWinning}")

## ================== Projects ==================

## Project 1: Life in Weeks
age = input("What is your age? ")
years_left = 90 - int(age)
weeks_left = years_left * 52
print(f"You have {weeks_left} weeks left.")

## Project 2: Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate total bill and per-person share
total_tip = bill * (tip / 100)
total_bill = bill + total_tip
per_person = round(total_bill / people, 2)

print(f"Each person should pay: ${per_person}")
