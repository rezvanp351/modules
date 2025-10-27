# main.py
# Using the custom module greetings.py

# Option A: import whole module
import greatings
print(greatings.greet("Hassan"))
print(greatings.polite_greet("Zara", "Ms."))

# Option B: import specific functions
from greatings import greet
print(greet("Omid"))

# Option C: import with alias
import greatings as gr
print(gr.greet("Laila"))
