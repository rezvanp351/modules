# main_from_import.py
# Using 'from ... import ...' to import specific functions

# Import only add and multiply functions
from math_utils import add, multiply

x = 10
y = 5

print("Add:", add(x, y))        # 15
print("Multiply:", multiply(x, y))  # 50

# Note: subtract and divide are NOT imported here
# print(subtract(x, y))  # ❌ This would raise NameError
