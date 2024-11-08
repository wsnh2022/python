# Python Programming Guide

<details>
<summary>Table of Contents</summary>

- [1. Basic Syntax and Output](#1-basic-syntax-and-output)
- [2. Variables and Data Types](#2-variables-and-data-types)
- [3. String Operations](#3-string-operations)
- [4. Collection Operations](#4-collection-operations)
- [5. Control Flow](#5-control-flow)
- [6. Functions](#6-functions)
- [7. Data Structures](#7-data-structures)
- [8. Comprehensions](#8-comprehensions)
- [9. Higher-Order Functions](#9-higher-order-functions)
- [10. Modules and Packages](#10-modules-and-packages)
- [11. Error Handling](#11-error-handling)
- [12. File Handling](#12-file-handling)
- [13. Object-Oriented Programming (OOP)](#13-object-oriented-programming-oop)
- [14. Additional Must-Learn Fundamentals](#14-additional-must-learn-fundamentals)
- [15. Type Hints and Type Checking](#15-type-hints-and-type-checking)
- [16. Context Managers](#16-context-managers)

</details>

<details>
<summary>1. Basic Syntax and Output</summary>

### Simple Output

```python
print("Hello, World!")  # Displays: Hello, World!
```

### String Formatting

```python
name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Displays: Alice is 30 years old.
```

</details>

<details>
<summary>2. Variables and Data Types</summary>

### Variable Declarations

```python
name = "Alice"                      # String
age = 30                           # Integer
height = 5.5                       # Float
is_student = True                  # Boolean
address = None                     # NoneType
```

### Collections

```python
favorite_colors = ["red", "blue", "green"]  # List
person = {"name": "Alice", "age": 30}       # Dictionary
unique_numbers = {1, 2, 3}                  # Set
coordinates = (10.0, 20.0)                  # Tuple
```

</details>

<details>
<summary>3. String Operations</summary>

### String Manipulation

```python
greeting = "Hello, " + name         # Concatenation
print(greeting)                     # Displays: Hello, Alice
```

### String Methods

```python
message = "  Hello, World!  "
print(message.strip())              # Displays: Hello, World!
```

</details>

<details>
<summary>4. Collection Operations</summary>

### List Operations

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")                # Adds item
fruits.remove("banana")              # Removes item
print(fruits)                        # ['apple', 'cherry', 'date']
```

### Dictionary Operations

```python
person["job"] = "Engineer"           # Adds key-value pair
print(person.get("job"))            # Accesses value
```

### Set Operations

```python
unique_numbers.add(4)                # Adds item
unique_numbers.remove(1)             # Removes item
print(unique_numbers)                # {2, 3, 4}
```

</details>

<details>
<summary>5. Control Flow</summary>

### Conditional Statements

```python
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
```

### Ternary Operator

```python
is_adult = "Yes" if age >= 18 else "No"
print(is_adult)                      # Yes
```

### Loops

<details>
<summary>For Loop</summary>

```python
for i in range(5):
    print(i)                         # 0 1 2 3 4
```
</details>

<details>
<summary>While Loop</summary>

```python
count = 0
while count < 5:
    print(count)                     # 0 1 2 3 4
    count += 1
```
</details>

</details>

<details>
<summary>6. Functions</summary>

### Basic Function

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))                # Hello, Alice!
```

### Default Parameters

```python
def greet_with_default(name="Guest"):
    return f"Hello, {name}!"

print(greet_with_default())          # Hello, Guest!
print(greet_with_default("Bob"))     # Hello, Bob!
```

</details>

<details>
<summary>7. Data Structures</summary>

### Lists

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.sort()
print(fruits)  # ['apple', 'banana', 'cherry', 'date']
```

### Dictionaries

```python
person = {"name": "Alice", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")         # name: Alice \n age: 30
```

### Tuples

```python
point = (10, 20)                     # Immutable collection
print(point[0], point[1])            # 10 20
```

</details>

<details>
<summary>8. Comprehensions</summary>

### List Comprehensions

```python
squared_numbers = [x ** 2 for x in range(5)]
print(squared_numbers)                # [0, 1, 4, 9, 16]
```

### Dictionary Comprehensions

```python
squares = {x: x ** 2 for x in range(5)}
print(squares)                        # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

</details>

<details>
<summary>9. Higher-Order Functions</summary>

### Lambda Functions

```python
add = lambda x, y: x + y
print(add(2, 3))                     # 5
```

### Map and Filter

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(squared, even_numbers)          # [1, 4, 9, 16] [2, 4]
```

</details>

<details>
<summary>10. Modules and Packages</summary>

```python
import math
print(math.sqrt(16), math.pi)         # 4.0 3.141592653589793
```

</details>

<details>
<summary>11. Error Handling</summary>

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

</details>

<details>
<summary>12. File Handling</summary>

```python
# Writing to file
with open('example.txt', 'w') as file:
    file.write("Hello, file!")

# Reading from file
with open('example.txt', 'r') as file:
    print(file.read())               # Hello, file!
```

</details>

<details>
<summary>13. Object-Oriented Programming (OOP)</summary>

### Classes and Objects

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", 4)
print(my_dog.name, my_dog.age, my_dog.bark())  # Buddy 4 Woof!
```

### Inheritance

```python
class Puppy(Dog):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

my_puppy = Puppy("Max", 1, "Beagle")
print(my_puppy.name, my_puppy.breed)  # Max Beagle
```

</details>

<details>
<summary>14. Additional Must-Learn Fundamentals</summary>

<details>
<summary>Enumerate</summary>

```python
colors = ["red", "blue", "green"]
for index, color in enumerate(colors):
    print(index, color)               # 0 red \n 1 blue \n 2 green
```
</details>

<details>
<summary>Zip</summary>

```python
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(name, age)                  # Alice 30 \n Bob 25 \n Charlie 35
```
</details>

<details>
<summary>String Methods</summary>

```python
message = "  Hello, World!  "
print(message.strip())                # Hello, World!
```
</details>

<details>
<summary>Generators</summary>

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)                     # 5 4 3 2 1
```
</details>

<details>
<summary>Additional String Methods</summary>

```python
text = "python programming"
print(text.upper())                   # PYTHON PROGRAMMING
print(text.lower())                   # python programming
print(text.title())                   # Python Programming
```
</details>

<details>
<summary>List Slicing</summary>

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])                  # [2, 3, 4]
```
</details>

<details>
<summary>Basic Regular Expressions</summary>

```python
import re
pattern = r'\d+'                     # Matches one or more digits
text = "There are 123 apples"
result = re.findall(pattern, text)
print(result)                        # ['123']
```
</details>

</details>

<details>
<summary>15. Type Hints and Type Checking</summary>

```python
from typing import List, Dict, Optional, Union

def greet(name: str) -> str:
    return f"Hello, {name}"

def process_numbers(numbers: List[int]) -> Dict[str, float]:
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers)
    }

def get_user(user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    # Could return None or a user dictionary
    return {"name": "Alice", "id": user_id}
```

</details>

<details>
<summary>16. Context Managers</summary>

```python
# Custom context manager
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

# Using context manager
with MyContextManager():
    print("Inside context")

# File handling with context
with open('file.txt', 'w') as f1, open('other.txt', 'r') as f2:
    f1.write(f2.read())
```

</details>
