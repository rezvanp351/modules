# ==============================================
# Python Modules — Educational Examples
# Author: Rezvan Panah
# ==============================================

"""
This file demonstrates how to use different built-in Python modules.
Each example includes a demonstration and explanation below it.
All examples execute automatically.
"""


# ----------------------------------------------
# 1. Math Module: sqrt, pi
# ----------------------------------------------
import math

print("Example 1: Math Module")
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)
print("""
Explanation:
The math module provides mathematical functions such as sqrt() for square root
and constants like math.pi for the value of π (pi).
""")
print("=" * 50)


# ----------------------------------------------
# 2. Random Module: randint, choice
# ----------------------------------------------
import random

print("Example 2: Random Module")
print("Random integer between 1 and 10:", random.randint(1, 10))
colors = ["red", "green", "blue"]
print("Random choice from list:", random.choice(colors))
print("""
Explanation:
The random module is used to generate random numbers or select random items.
- randint(a, b): returns a random integer between a and b.
- choice(list): returns a random element from a list.
""")
print("=" * 50)


# ----------------------------------------------
# 3. Datetime Module: current date and time
# ----------------------------------------------
import datetime

print("Example 3: Datetime Module")
now = datetime.datetime.now()
print("Current date and time:", now)
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)
print("""
Explanation:
The datetime module handles dates and times.
- datetime.now(): returns the current date and time.
- You can access parts like year, month, and day individually.
""")
print("=" * 50)


# ----------------------------------------------
# 4. OS Module: working directory
# ----------------------------------------------
import os

print("Example 4: OS Module")
cwd = os.getcwd()
print("Current working directory:", cwd)
print("""
Explanation:
The os module lets you interact with your operating system.
- os.getcwd(): returns the current working directory of your project.
""")
print("=" * 50)


# ----------------------------------------------
# 5. Sys Module: Python version
# ----------------------------------------------
import sys

print("Example 5: Sys Module")
print("Python version:", sys.version)
print("""
Explanation:
The sys module provides system-specific parameters and functions.
- sys.version: shows the version of Python currently being used.
""")
print("=" * 50)


# ----------------------------------------------
# 6. JSON Module: encode/decode
# ----------------------------------------------
import json

print("Example 6: JSON Module")
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print("JSON string:", json_str)
parsed = json.loads(json_str)
print("Parsed data:", parsed)
print("""
Explanation:
The json module converts between Python objects and JSON strings.
- json.dumps(): converts Python data to JSON.
- json.loads(): converts JSON back to a Python dictionary.
""")
print("=" * 50)


# ----------------------------------------------
# 7. Statistics Module: mean, median
# ----------------------------------------------
import statistics

print("Example 7: Statistics Module")
numbers = [10, 20, 30, 40, 50]
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("""
Explanation:
The statistics module provides functions for mathematical statistics.
- mean(): calculates the average value.
- median(): finds the middle value in a dataset.
""")
print("=" * 50)


# ----------------------------------------------
# 8. Custom Module: demonstration
# ----------------------------------------------
print("Example 8: Custom Module")
print("To create a custom module, follow these steps:")
print("1. Create a new Python file (e.g., greetings.py).")
print("2. Define functions inside it (e.g., def say_hello(name): ...).")
print("3. Import it using 'import greetings' in another file.")
print("4. Then call greetings.say_hello('Rezvan').")
print("""
Explanation:
You can create your own module by writing reusable code in a separate Python file.
Then import it into any project using the 'import' statement.
""")
print("=" * 50)
