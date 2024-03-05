## ------------------------ lesson 1 --------------------------------------------------
# ====== Print Modifiers

print('hai yogi are you excited for 100 days of coding !!!')

##--- Print Modifiers with Examples 
print('She said: "Hello" and then left.')  # Example 2 Working Code ✅

# --- with Examples
print("A 'single quote' inside a double quote")
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote") 

#To Avoid repeated prints into next lines use backslash
print("hai\nhai\nhai") 

# This will print with an extra space before the exclamation mark.
print("i " + 'love ' + '"you" ' + '!!!' + "\n💗\n💗\n💗")  


# ------------------------ lesson 2 --------------------------------------
# ====== debugging practice

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')                   #Concatnate using space before double quotes
print("New lines can be created with a backslash and n.")
print("hello " + input("what is your good name sir !!!\nplease type here:"))


# ------------------------ lesson 3 --------------------------------------
# ====== input function

print(input("What is your name?")) #❌
print(input()) #✅ 

practice 1
n1 = int(input())
n2 = int(input())
print(n1 * n2)


# ------------------------ lesson 4 --------------------------------------
# ====== len function
practice finding string length using len function
numOfLetters = len("Angela")
print(numOfLetters)
# or
print(len(input()))



# ------------------------ lesson 5 --------------------------------------
#lesson 5 ======= variables

# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
###################################
# Write your code below this line 👇

# -------- Solution --------
# Solution is Create a third variable to help switch the values in a, b using 3rd variable c
c = a
a = b
b = c
# --------------------------

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


# project 1 - Brand name generator
# 1. Create a greeting for your program
print("Welcome to the band name Generater !!!")
# 2. Ask the user for the city they group up in
city = input('Enter the city you grown up in:')
# 3. ask the user for the name of the pet
pet = input('Enter the name of your pet: ')
# 4. Combine the name of their city and pet and show them their band name.
print("your band name is " + city + " " + pet)


############## DAY 2 #################

# ------------------------ lesson 5 --------------------------------------
# lesson 6 ======= DATA TYPES

string, integer, float_num, booleantrue, booleanfalse = 'abc', 123_456_789, 1.23456, True, False  
print(string, integer, float_num, booleantrue, booleanfalse)

find 4 data types using type function
print(type(string), type(integer), type(float_num), type(booleantrue), type(booleanfalse))

two_digit_number = input() # input is 32
print(type(two_digit_number)) # find the data type for testing purpose    
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Mathematical operations

# PEMDAS python order of priority is
# P_arentheses     : ()
# E_xponents       : **
# M_ultiplication  : *
# D_ivision        : /
# A_ddition        : +
# S_ubtraction     : -

# based on pemdas method natural output is 7.0
print(3 * 3 + 3 / 3 - 3) 

# but now Desried output is 3.0 try it
print(3 * (3 + 3) / 3 - 3)

# BMI calculater project
formula is bmi = weight (kg) / height² (meter²)

### student workout Solution
# ======== project 2 - BMI calculater
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# 5.11 foot in meters = 1.557

## Output with float
print(float(weight) / (float(height) * float(height)))

## Output without float
float_num = float(weight) / (float(height) ** 2) 
print(int(float_num))

### teacher final Solution
height = input()
weight = input()
# Your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)

# ------------------------ lesson 6 --------------------------------------
 number manupulation
print(round(8/3)) # Round without decimal places
print(round(8/3, 2)) # Round with 2 decimal places
print(round(2.666666, 2)) # Round with 2 decimal places

floor division method - floating number output is 2
print(8 // 3)

# ======== project 3 - life in weeks
### student workout Solution
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
weeks_in_year = int(365 / 7)
balance_age = 90 - int(age)
left_weeks = balance_age * int(weeks_in_year)

print(f"You have {left_weeks} weeks left.")
# input: 15
# output: You have 3900 weeks left.


### teacher final Solution
age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")

## ======== project 4 - Tip calculater
bill = float(input())
tip = float(input())
No_of_Splits = float(input())

final_amount = (bill / No_of_Splits) * tip

print(round(final_amount, 2))


