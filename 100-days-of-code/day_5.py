####################################################################################
# What I Learned on Day 5:
# 1. How to find the maximum value in a list using a loop.
# 2. How to calculate the sum of numbers in a range using a loop.
# 3. Understanding FizzBuzz logic with conditions in loops.
# 4. Creating a random password using character sets.
#    - Easy level: Concatenating random characters directly.
#    - Hard level: Shuffling a list of characters for randomness.
####################################################################################

####################################################################################
# LESSON 1: Find the maximum score in a list
####################################################################################

# Given student scores
student_score = [57, 85, 146, 136, 107, 120, 157, 168, 165, 114, 108, 99, 168, 57, 164, 68, 165, 50, 167, 116]

# Initialize the max_score variable
max_score = 0

# Iterate through the scores to find the maximum
for score in student_score:
    if score > max_score:
        max_score = score

print(f"The maximum score is: {max_score}")

####################################################################################
# LESSON 2: Sum of all numbers from 1 to 100
####################################################################################

# Initialize the total sum
total = 0

# Use a range to iterate through numbers
for number in range(1, 101):
    total += number

print(f"The total sum from 1 to 100 is: {total}")

####################################################################################
# LESSON 3: FizzBuzz from 1 to 100
####################################################################################

# Iterate through numbers from 1 to 100
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

####################################################################################
# LESSON 4: Generate a random password
####################################################################################

import random

# Define character sets for the password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
    'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

# Input for password composition
print('Welcome to the PyPassword Generator!')
the_letters = int(input('How many letters would you like in your password?\n'))
the_numbers = int(input('How many numbers would you like?\n'))
the_symbols = int(input('How many symbols would you like?\n'))

## =======================
## Easy Level: Concatenating characters directly
## =======================
password = ""

# Add random letters
for _ in range(the_letters):
    password += random.choice(letters)

# Add random numbers
for _ in range(the_numbers):
    password += random.choice(numbers)

# Add random symbols
for _ in range(the_symbols):
    password += random.choice(symbols)

print(f"Easy-level password: {password}")

## =======================
## Hard Level: Using a list and shuffling for randomness
## =======================
password_List = []

# Add random letters
for _ in range(the_letters):
    password_List.append(random.choice(letters))

# Add random numbers
for _ in range(the_numbers):
    password_List.append(random.choice(numbers))

# Add random symbols
for _ in range(the_symbols):
    password_List.append(random.choice(symbols))

# Print before shuffling
print(f"Password before shuffle: {''.join(password_List)}")

# Shuffle the password list for randomness
random.shuffle(password_List)

# Convert list to string for the final password
final_password = ''.join(password_List)
print(f"Your final shuffled password is: {final_password}")
