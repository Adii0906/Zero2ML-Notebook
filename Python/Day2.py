# ========================
# DAY 2 — STRING METHODS & USER INPUT
# ========================
print("\nDAY 2 — String Methods & User Input")


# Taking input from the user
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")


# Basic string methods
text = "python programming"
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Replace:", text.replace("python", "AI"))
print("Split:", text.split())
print("Starts with 'py'?:", text.startswith("py"))
print("Ends with 'ing'?:", text.endswith("ing"))


# String slicing
sample = "HelloPython"
print("First 5 chars:", sample[:5])
print("Last 3 chars:", sample[-3:])
print("Middle slice:", sample[2:7])


# Exercise:
# 1. Take user input for a sentence and count vowels
# 2. Check if the entered string is a palindrome