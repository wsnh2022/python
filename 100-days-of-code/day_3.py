####################################################################################
# What I Learned on Day 3:
# 1. Control Flow and Conditional Operators:
#    - Using `if`, `else`, and `elif` for decision-making.
#    - Comparison operators: `<`, `>`, `<=`, `>=`, `==`, and `%` (modulo for remainder).
# 2. Nested if Statements:
#    - Embedding conditional checks within other `if` blocks.
#    - Building complex logic for projects like ticket pricing.
# 3. Logical Operators:
#    - `and`, `or`, `not` for combining multiple conditions.
# 4. Projects:
#    - Odd or Even Checker: Using modulo to determine parity.
#    - BMI Calculator 2.0: Classifying BMI categories.
#    - Leap Year Checker: Following leap year rules with nested conditions.
#    - Pizza Order Program: Calculating the final bill based on user choices.
#    - Love Calculator: Determining compatibility with string counts.
#    - Treasure Island: A text-based adventure game using conditional flow.
####################################################################################

## -------------------- Control Flow with if/else --------------------
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
########################################################################################################################

## -------------------- Nested if Statements and elif --------------------
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?: "))
    if age <= 12:
        print("Ticket price is $5.")
    elif age <= 18:
        print("Ticket price is $7.")
    else:
        print("Ticket price is $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
########################################################################################################################

## -------------------- Comparison Operators --------------------
# Comparison operators are used to compare two values:
# %  -> Modulus (remainder after division)
# >  -> Greater than
# <  -> Less than
# >= -> Greater than or equal to
# <= -> Less than or equal to
# == -> Equal to

########################################################################################################################

## -------------------- PROJECT - Odd or Even --------------------
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
#######################################################################################################################

## -------------------- PROJECT - BMI Calculator 2.0 --------------------
height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kg: "))
bmi = round(weight / (height ** 2), 2)

'''
BMI Categories:
- Underweight: BMI < 18.5
- Normal weight: 18.5 ≤ BMI ≤ 24.9
- Overweight: 25 ≤ BMI ≤ 29.9
- Obese: BMI ≥ 30
'''

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are Underweight.")
elif 18.5 <= bmi <= 24.9:
    print(f"Your BMI is {bmi}, you have Normal weight.")
elif 25 <= bmi <= 29.9:
    print(f"Your BMI is {bmi}, you are Overweight.")
elif 30 <= bmi <= 34.9:
    print(f"Your BMI is {bmi}, you are Obese.")
else:
    print(f"Your BMI is {bmi}, you are Clinically Obese.")
#######################################################################################################################

## -------------------- PROJECT - Leap Year Checker --------------------
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")
########################################################################################################################

## -------------------- PROJECT - Python Pizza --------------------
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    bill += 2 if size == "S" else 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
########################################################################################################################

## -------------------- PROJECT - Love Calculator --------------------
print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like Coke and Mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
########################################################################################################################

## -------------------- PROJECT - Treasure Island --------------------
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. Do you want to 'wait' for a boat or 'swim' across? ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
########################################################################################################################
