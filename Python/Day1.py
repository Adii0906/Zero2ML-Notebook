print("DAY 1 — Python Basics")

# Variables and Data Types
name = "Jhon Doe"
age = 20
is_student = True
print(name, age, is_student)

# for loop in python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).   
for i in range(5):
    print("Loop", i)

# Functions in python is defined using the def keyword and ussed to encapsulate a block of code that performs a specific task.
def greet(name):
    return f"Hello {name}"
print(greet("World"))