# ========================
# DAY 3 — PYTHON DATA STRUCTURES
# ========================
print("\nDAY 3 — Python Data Structures")


# Working with Strings
text = "Hello Python"
print(text.upper())
print(text.replace("Python", "Aditya"))


# Lists
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("Fruits:", fruits)


# List Comprehension
squares = [i * i for i in range(1, 6)]
print("Squares:", squares)


# Dictionary
student = {
"name": "Aditya",
"age": 20,
"course": "Python"
}
print(student)
print(student.keys())
print(student.values())


# Set
unique_nums = {1, 2, 3, 3, 2, 1}
print("Unique Set:", unique_nums)


# Exercise: Create a list of even numbers using list comprehension