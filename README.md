# 🐍 Python Modules — Explained for Beginners
# Author: Rezvan Panah
# Year: 2025
# Language: Python 3.10+
# ---------------------------------------------
# This guide contains simple and practical examples of Python’s
# most commonly used built-in modules.
# Each section explains what the module does, why it’s useful,
# and includes working examples you can run directly.
# ---------------------------------------------


# =============================================
# 1️⃣ Math Module — math
# =============================================
import math

print("Example 1: Math Module")
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)
print("""
💡 Explanation:
The math module provides mathematical functions and constants.
- math.sqrt(x): Returns the square root of x.
- math.pi: Represents the constant π (pi).
""")
print("=" * 60)


# =============================================
# 2️⃣ Random Module — random
# =============================================
import random

print("Example 2: Random Module")
print("Random integer between 1 and 10:", random.randint(1, 10))
colors = ["red", "green", "blue"]
print("Random choice from list:", random.choice(colors))
print("""
💡 Explanation:
The random module is used to generate random numbers or select random items.
- randint(a, b): Returns a random integer between a and b.
- choice(list): Returns a random element from a list.
""")
print("=" * 60)


# =============================================
# 3️⃣ Datetime Module — datetime
# =============================================
import datetime

print("Example 3: Datetime Module")
now = datetime.datetime.now()
print("Current date and time:", now)
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)
print("""
💡 Explanation:
The datetime module handles dates and times.
- datetime.now(): Returns the current date and time.
- You can access parts like year, month, and day individually.
""")
print("=" * 60)


# =============================================
# 4️⃣ OS Module — os
# =============================================
import os

print("Example 4: OS Module")
cwd = os.getcwd()
print("Current working directory:", cwd)
print("""
💡 Explanation:
The os module lets you interact with your operating system.
- os.getcwd(): Returns the current working directory of your project.
""")
print("=" * 60)


# =============================================
# 5️⃣ Sys Module — sys
# =============================================
import sys

print("Example 5: Sys Module")
print("Python version:", sys.version)
print("""
💡 Explanation:
The sys module provides system-specific parameters and functions.
- sys.version: Shows the version of Python currently being used.
""")
print("=" * 60)


# =============================================
# 6️⃣ JSON Module — json
# =============================================
import json

print("Example 6: JSON Module")
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print("JSON string:", json_str)
parsed = json.loads(json_str)
print("Parsed data:", parsed)
print("""
💡 Explanation:
The json module converts between Python objects and JSON strings.
- json.dumps(): Converts Python data to JSON.
- json.loads(): Converts JSON back to a Python dictionary.
""")
print("=" * 60)


# =============================================
# 7️⃣ Statistics Module — statistics
# =============================================
import statistics

print("Example 7: Statistics Module")
numbers = [10, 20, 30, 40, 50]
print("Mean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("""
💡 Explanation:
The statistics module provides functions for mathematical statistics.
- mean(): Calculates the average value.
- median(): Finds the middle value in a dataset.
""")
print("=" * 60)


# =============================================
# 8️⃣ Custom Module — Example
# =============================================
print("Example 8: Custom Module")
print("To create a custom module, follow these steps:\n")

print("""
1️⃣ Create a new Python file, for example `greetings.py`
----------------------------------------------------------
def say_hello(name):
    return f"Hello, {name}!"

2️⃣ Import and use it in another file
------------------------------------
import greetings
print(greetings.say_hello("Rezvan"))
""")

print("""
💡 Explanation:
You can create your own module by writing reusable code in a separate file.
Then import it into any project using the 'import' statement.
""")
print("=" * 60)


# =============================================
# ⚙️ HOW TO RUN
# =============================================
print("""
▶️ How to Run:
-------------
Save this file as 'modules_demo.py' and run it in your terminal:

    python modules_demo.py

All examples will execute automatically and display outputs with explanations.
""")

# =============================================
# 🎯 SUMMARY TABLE
# =============================================
print("""
📘 Summary of Modules
---------------------
| Module       | Purpose                      | Example               |
|---------------|------------------------------|------------------------|
| math          | Mathematical operations      | math.sqrt(16)          |
| random        | Random numbers & selections  | random.choice(list)    |
| datetime      | Date and time handling       | datetime.now()         |
| os            | Operating system access      | os.getcwd()            |
| sys           | System info (Python version) | sys.version            |
| json          | Encode/Decode JSON data      | json.dumps(data)       |
| statistics    | Mean, median calculations    | statistics.mean(list)  |
| custom module | Reusable user-defined code   | import greetings       |
""")

# =============================================
# 📎 AUTHOR INFO
# =============================================
print("""
👩‍💻 Created by: Rezvan Panah
📅 Year: 2025
💬 Language: Python 3.10+
🎯 Purpose: To teach Python’s built-in modules in a clear, beginner-friendly way.
💖 Support & Feedback:
If you found this helpful:
- ⭐ Star this repository
- 🗨️ Share it with others learning Python
- 💬 Leave feedback or suggestions

Your support motivates more free educational content! 🌍
""")
