Here’s your refined **Python Programming Guide**. I’ve cleaned up the jargon, combined redundant sections, and ensured every heading is purposeful and intuitive. The structure is tighter now, with no loose ends or overlap.

---

# Python Programming Guide

<details>
<summary><strong>📘 Table of Contents</strong></summary>

* [1. Getting Started: Syntax & Output](#1-getting-started-syntax--output)
* [2. Variables and Data Types](#2-variables-and-data-types)
* [3. Strings: Basics to Methods](#3-strings-basics-to-methods)
* [4. Lists, Tuples, Sets, and Dictionaries](#4-lists-tuples-sets-and-dictionaries)
* [5. Conditions and Loops](#5-conditions-and-loops)
* [6. Functions & Parameters](#6-functions--parameters)
* [7. Comprehensions](#7-comprehensions)
* [8. Functional Tools: Lambda, Map, Filter](#8-functional-tools-lambda-map-filter)
* [9. Error Handling](#9-error-handling)
* [10. File Operations](#10-file-operations)
* [11. Modules & Imports](#11-modules--imports)
* [12. Object-Oriented Programming](#12-object-oriented-programming)
* [13. Python Extras: zip, enumerate, slicing](#13-python-extras-zip-enumerate-slicing)
* [14. Generators & Context Managers](#14-generators--context-managers)
* [15. Type Hints](#15-type-hints)
* [16. Regex (Basics Only)](#16-regex-basics-only)

</details>

---

## 1. Getting Started: Syntax & Output

```python
print("Hello, World!")                    # Basic output
name = "Alice"
age = 30
print(f"{name} is {age} years old.")     # Formatted output
```

---

## 2. Variables and Data Types

```python
name = "Alice"       # str
age = 30             # int
height = 5.5         # float
is_student = True    # bool
address = None       # NoneType
```

---

## 3. Strings: Basics to Methods

```python
greeting = "Hello, " + name       # Concatenation
print(greeting.strip())           # Removes leading/trailing spaces

text = "python programming"
print(text.upper())               # PYTHON PROGRAMMING
print(text.title())               # Python Programming
```

---

## 4. Lists, Tuples, Sets, and Dictionaries

### Lists

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.sort()
print(fruits[1:3])                # List slicing: ['banana', 'cherry']
```

### Tuples

```python
point = (10, 20)
print(point[0])                   # Access tuple element
```

### Sets

```python
unique = {1, 2, 3}
unique.add(4)
unique.remove(1)
```

### Dictionaries

```python
person = {"name": "Alice", "age": 30}
person["job"] = "Engineer"
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 5. Conditions and Loops

### Conditionals

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Ternary

```python
status = "Adult" if age >= 18 else "Minor"
```

### Loops

```python
for i in range(5):
    print(i)

count = 0
while count < 3:
    print(count)
    count += 1
```

---

## 6. Functions & Parameters

```python
def greet(name="Guest"):
    return f"Hello, {name}"

print(greet())          # Hello, Guest
print(greet("Bob"))     # Hello, Bob
```

---

## 7. Comprehensions

```python
squares = [x**2 for x in range(5)]
square_dict = {x: x**2 for x in range(5)}
```

---

## 8. Functional Tools: Lambda, Map, Filter

```python
add = lambda x, y: x + y

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
```

---

## 9. Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## 10. File Operations

```python
# Write
with open('data.txt', 'w') as f:
    f.write("Hello!")

# Read
with open('data.txt', 'r') as f:
    print(f.read())
```

---

## 11. Modules & Imports

```python
import math
print(math.sqrt(16))        # 4.0
```

---

## 12. Object-Oriented Programming

### Basic Class

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return "Woof!"

d = Dog("Buddy")
print(d.name, d.bark())      # Buddy Woof!
```

### Inheritance

```python
class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

p = Puppy("Max", "Beagle")
print(p.name, p.breed)       # Max Beagle
```

---

## 13. Python Extras: zip, enumerate, slicing

```python
# Enumerate
colors = ["red", "green"]
for idx, color in enumerate(colors):
    print(idx, color)

# Zip
names = ["Alice", "Bob"]
ages = [30, 25]
for name, age in zip(names, ages):
    print(name, age)

# List Slicing
my_list = [1, 2, 3, 4]
print(my_list[1:3])           # [2, 3]
```

---

## 14. Generators & Context Managers

```python
# Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)

# Context Manager
class MyCtx:
    def __enter__(self): print("Start"); return self
    def __exit__(self, *args): print("End")

with MyCtx():
    print("Inside")
```

---

## 15. Type Hints

```python
from typing import List, Dict, Optional

def greet(name: str) -> str:
    return f"Hello, {name}"

def stats(nums: List[int]) -> Dict[str, float]:
    return {"sum": sum(nums), "avg": sum(nums) / len(nums)}

def get_user(id: int) -> Optional[Dict[str, str]]:
    return {"id": str(id), "name": "Alice"}
```

---

## 16. Regex (Basics Only)

```python
import re
text = "There are 123 apples"
print(re.findall(r'\d+', text))     # ['123']
```

---
