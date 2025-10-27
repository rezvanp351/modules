# ==============================================
# Python Modules — Educational Examples
# Author: Rezvan Panah
# ==============================================

# Math Module: sqrt, pi
def math_module_usage():
    import math
    print("Square root of 16:", math.sqrt(16))
    print("Value of pi:", math.pi)


# Random Module: randint, choice
def random_module_usage():
    import random
    print("Random integer between 1 and 10:", random.randint(1, 10))
    colors = ["red", "green", "blue"]
    print("Random choice from list:", random.choice(colors))


# Datetime Module: current date and time
def datetime_module_usage():
    import datetime
    now = datetime.datetime.now()
    print("Current date and time:", now)
    print("Current year:", now.year)
    print("Current month:", now.month)
    print("Current day:", now.day)


# OS Module: working directory
def os_module_usage():
    import os
    cwd = os.getcwd()
    print("Current working directory:", cwd)


# Sys Module: Python version
def sys_module_usage():
    import sys
    print("Python version:", sys.version)


# JSON Module: encode/decode
def json_module_usage():
    import json
    data = {"name": "Alice", "age": 25}
    json_str = json.dumps(data)
    print("JSON string:", json_str)
    parsed = json.loads(json_str)
    print("Parsed data:", parsed)


# Statistics Module: mean, median
def statistics_module_usage():
    import statistics
    numbers = [10, 20, 30, 40, 50]
    print("Mean:", statistics.mean(numbers))
    print("Median:", statistics.median(numbers))


# Custom Module: demonstration
def custom_module_usage():
    print("Create a custom module (e.g., greetings.py) and import functions.")
