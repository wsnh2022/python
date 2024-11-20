####################################################################################
# What I Learned on Day 4:
# 1. Python Imports:
#    - Using `import` to access external modules for additional functionalities.
#    - Organizing and reusing code with modules.
# 2. Random Module:
#    - Generating random integers, floats, and making random choices.
#    - Implementing simple games like Heads or Tails using randomness.
# 3. Lists:
#    - Basics of lists: creating, indexing, and storing elements.
#    - Converting data types to lists and handling mixed data types.
#    - Working with nested lists and accessing deep elements.
# 4. Projects:
#    - "Who Will Pay the Bill?" using random choice.
#    - Rock, Paper, Scissors game with ASCII art.
####################################################################################

## -------------------- Python Imports --------------------
# Access External Code:
# Import modules to access functions, classes, and variables defined in external files or packages.

# Code Organization:
# Helps group related functionalities for better management and reusability.

# Example: Importing a custom module and accessing its variable
# import test_function
# print(test_function.s1)  # Access variable from external files (output: {1, 2, 3, 4, 5, 6})

##############################################################################################

# ==============================
# RANDOM NUMBER GENERATION
# ==============================
import random

# Generate random integer between 1 and 10
random_integer = random.randint(1, 10)
print("Random Integer:", random_integer)

# Generate random decimal between 0 and 10
random_number_0_to_1 = random.random() * 10
print("Random Decimal:", random_number_0_to_1)

# Generate random float between 1 and 12
random_float = random.uniform(1, 12)
print("Random Float:", random_float)


# ==============================
# HEADS OR TAILS GAME
# ==============================

# Method 1: Using randint
random_sides = random.randint(0, 1)
if random_sides == 1:
    print("Heads")
else:
    print("Tails")

# Method 2: Using choice
coin = random.choice(['Heads', 'Tails'])
print(f"The coin landed on: {coin}")

#############################################################################################

# ====================================
# BASIC LIST CREATION AND INDEXING > documentation: https://docs.python.org/3/tutorial/datastructures.html
# ====================================

# Basic list with indices demonstration
##     Index:  0        1       2
fruits = ["cherry", "Apple", "Pear"]
##     Index: -3       -2      -1

## Forward indexing
print("Forward indexing:", fruits[0], fruits[1], fruits[2])
## Output: cherry Apple Pear

## Reverse indexing
print("Reverse indexing:", fruits[-1], fruits[-2], fruits[-3])
# Output: Pear Apple cherry

## Storing list element in a variable
another_fruit = fruits[0]
print("Stored element:", another_fruit)
# Output: cherry

# ====================================
# LIST CONVERSION
# ====================================

# Converting string to list
str_to_list = list('abc')
print("String to list:", str_to_list)  # Output: ['a', 'b', 'c']

# Converting tuple to list
tuple_to_list = list((1, 2, 3))
print("Tuple to list:", tuple_to_list)  # Output: [1, 2, 3]
##############################################################################################

## PROJECT - Who will pay the bill?
import random

friends = random.choice(["Emma", "Liam", "Olivia", "Noah", "Ava", "James", "Sophia", "Lucas", "Isabella", "Mason"])
print(friends)

friends_list = ["Emma", "Liam", "Olivia", "Noah", "Ava", "James", "Sophia", "Lucas", "Isabella", "Mason"]
print(len(friends_list))

# Indexerror - list index out of range error.
print((friends_list[10 - 1]))

# ====================================
# DIFFERENT TYPES OF LISTS
# ====================================

# List with mixed data types
mixed_list = [
    1,        # integer
    'abc',    # string
    1.23,     # float
    (3+4j),   # complex
    True      # boolean
]
print("Mixed list:", mixed_list)

# Empty list
empty_list = []
print("Empty list:", empty_list)

# ====================================
# NESTED LISTS
# ====================================

# Nested list structure
nested_list = [
    'a', 
    'b', 
    ['cc', 'dd', ['eee', 'fff']], 
    'g', 
    'h'
]

# Accessing nested elements
print("First level:", nested_list[2])        # Output: ['cc', 'dd', ['eee', 'fff']]
print("Second level:", nested_list[2][2])    # Output: ['eee', 'fff']
print("Third level:", nested_list[2][2][0])  # Output: eee

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [
    ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"],
    ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
]
print(dirty_dozen[1][1]) # Kale
#########################################################################

# Rock, Paper, Scissors: ASCII Art Game
# A fun, visual implementation of the classic hand game

import random

# ASCII art for hand signs
hands = {
    'rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    'paper': """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    'scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Tip:
# - .keys() returns a view of the dictionary's keys 
#   so we can convert it to a list for random.choice()
# - .get(key, default) safely retrieves a value:
#   - If 'key' exists, returns its value
#   - If 'key' doesn't exist, returns the default (here: 'Invalid choice!')

# Game logic
computer = random.choice(list(hands.keys()))
player = input("Enter rock, paper, or scissors: ").lower()

# Display choices
print(f"\nYou chose:\n{hands.get(player, 'Invalid choice!')}")
print(f"\nComputer chose:\n{hands[computer]}")

# Winning logic explanation:
# The line checks if (player, computer) matches any winning combination
# - 'rock' beats 'scissors'
# - 'paper' beats 'rock'
# - 'scissors' beats 'paper'
# By using a list of tuples, we create a simple, readable way to define wins
if player == computer:
    print("It's a tie!")
elif (player, computer) in [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]:
    print("You win!")
else:
    print("Computer wins!")