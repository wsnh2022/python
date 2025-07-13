# Python Basics Guide

<strong>📘 Table of Contents</strong>

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
* [17. Good Practices Summary](#17-good-practices-summary)

---

## 1. Getting Started: Syntax & Output

Use this to test your Python setup and understand the print statement—your basic tool to see what's happening in your code.

```python
print("Hello, World!")
name = "Alice"
age = 30
print(f"{name} is {age} years old.")
```

✅ **Good practice:** Use `f-strings` for readable formatting and debugging.

---

## 2. Variables and Data Types

Variables store values. Understanding types helps you predict behavior (e.g., how + works differently with strings and integers).

```python
name = "Alice"       # str
age = 30             # int
height = 5.5         # float
is_student = True    # bool
address = None       # NoneType
```

✅ **Good practice:** Use clear, descriptive variable names (`user_age` > `a`).

---

## 3. Strings: Basics to Methods 

### Useful string methods for **cleaning and transforming messy text data** a must-have skill for any data analyst or Python developer.

**Use case:** You’ll often clean raw input—whether from a file, user form, or scraped web page. These methods help standardize, format, and clean that data.

```python
text = "  Hello, Python!  "

print(text.strip())           # Removes leading/trailing spaces
print(text.lstrip())          # Removes leading spaces
print(text.rstrip())          # Removes trailing spaces

print(text.lower())           # hello, python!
print(text.upper())           # HELLO, PYTHON!
print(text.title())           # Hello, Python!
print(text.capitalize())      # First letter uppercase: "Hello, python!"

print(text.replace("Python", "World"))     # Replace text
print(text.replace(",", ""))               # Remove punctuation
```

### Useful for messy data:

```python
raw = "\n\n\t  john.DOE@example.COM  \t\n"
clean = raw.strip().lower()                # 'john.doe@example.com'
print(clean)
```

### Removing unwanted characters using `translate` + `str.maketrans`:

```python
messy = "Price: $5.00!"
table = str.maketrans('', '', "$!:")       # remove $, !, :
print(messy.translate(table))              # 'Price 500'
```

### Checking content:

```python
print("123abc".isalnum())         # True
print("hello".isalpha())          # True
print("123".isdigit())            # True
print("   ".isspace())            # True
```

### Splitting and joining:

```python
text = "one, two, three"
words = text.split(", ")          # ['one', 'two', 'three']
joined = "-".join(words)          # 'one-two-three'
print(joined)
```

✅ **Good practice:**

* Always strip and lowercase user input before comparisons.
* Use `.replace()` and `.translate()` to sanitize unwanted characters.
* Use `.split()` when reading CSV-style text manually.

---

## 4. Lists, Tuples, Sets, and Dictionaries

These are your go-to structures for storing and organizing data.

```python
# List: Ordered, mutable
colors = ["red", "blue"]
colors.append("green")

# Tuple: Ordered, immutable
point = (10, 20)

# Set: Unordered, no duplicates
unique_ids = {1, 2, 2, 3}

# Dictionary: Key-value pairs
person = {"name": "Alice", "age": 30}
```

✅ **Good practice:** Use dictionaries when data is labeled (e.g., user profiles).

---

## 5. Conditions and Loops

Control how your code behaves depending on data.

```python
# Conditional
if age >= 18:
    print("Adult")

# Loop
for color in colors:
    print(color)

# While loop
i = 0
while i < 3:
    print(i)
    i += 1
```

✅ **Good practice:** Avoid `while True` unless you're certain how you'll exit.

---

## 6. Functions & Parameters

Functions avoid repetition. They also make your code reusable and testable.

```python
def greet(name="Guest"):
    return f"Hello, {name}"

print(greet())
print(greet("Bob"))
```

✅ **Good practice:** Add default arguments and write functions for one clear purpose.

---

## 7. Comprehensions

These are short, clean ways to create lists or dictionaries from loops.

```python
squares = [x**2 for x in range(5)]
squares_dict = {x: x**2 for x in range(5)}
```

✅ **Good practice:** Use comprehensions for simple transformations, not complex logic.

---

## 8. Functional Tools: Lambda, Map, Filter

Use these when you're transforming or filtering data quickly, often in pipelines.

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
```

✅ **Good practice:** Keep lambdas short. For anything complex, use `def`.

---

## 9. Error Handling

Handle mistakes like missing files or invalid inputs without crashing the program.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero.")
```

✅ **Good practice:** Catch specific exceptions, not just `except:`.

---

## 10. File Operations

Reading and writing files is key in data projects (e.g., logs, CSVs).

```python
with open("log.txt", "w") as file:
    file.write("Start log")

with open("log.txt", "r") as file:
    print(file.read())
```

✅ **Good practice:** Use `with open()` to avoid leaving files open accidentally.

---

## 11. Modules & Imports

Break code into smaller reusable parts. Use Python's built-in tools or your own modules.

```python
import math
print(math.sqrt(16))  # 4.0
```

✅ **Good practice:** Only import what you need (`from math import sqrt` if you just need that).

---

## 12. Object-Oriented Programming

Use this for real-world modeling: users, animals, bank accounts, etc.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"

d = Dog("Buddy")
print(d.name, d.bark())
```

✅ **Good practice:** Keep class responsibilities small and use `self` clearly.

---

## 13. Python Extras: zip, enumerate, slicing

Quick tools for looping over or combining data structures.

```python
for i, color in enumerate(colors):
    print(i, color)

for name, age in zip(["A", "B"], [25, 30]):
    print(name, age)

print(colors[1:])  # Slicing
```

✅ **Good practice:** Use `zip` and `enumerate` instead of manually indexing.

---

## 14. Generators & Context Managers

Generators save memory. Context managers handle setup/cleanup (like file closing).

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)

class MyCtx:
    def __enter__(self): print("Enter"); return self
    def __exit__(self, *a): print("Exit")

with MyCtx():
    print("Inside")
```

✅ **Good practice:** Use `yield` to stream large datasets without memory issues.

---

## 15. Type Hints

Adds clarity and helps with editor suggestions or static checking.

```python
from typing import List

def total(values: List[int]) -> int:
    return sum(values)
```

✅ **Good practice:** Add type hints for functions in production or shared codebases.

---

## 16. Regex (Basics Only)

Use for validating or extracting text patterns (e.g., emails, numbers).

```python
import re
text = "abc123"
print(re.findall(r'\d+', text))  # ['123']
```

✅ **Good practice:** Use raw strings (`r"pattern"`) to avoid escaping nightmares.

---

## 17. Good Practices Summary

Here’s a snapshot of essential habits:

| Area              | Practice                               |
| ----------------- | -------------------------------------- |
| Naming            | Use `snake_case` and descriptive names |
| Functions         | Keep them small, focused               |
| Comments          | Explain “why,” not “what”              |
| Errors            | Handle only what you expect            |
| Imports           | Avoid unused or wildcard imports       |
| Readability       | Follow PEP8 (Python style guide)       |
| File/Resource Use | Always use `with` for files, sockets   |
| Complexity        | Avoid nested logic > 2 levels deep     |

---
