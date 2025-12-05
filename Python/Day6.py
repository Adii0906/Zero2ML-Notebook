# ========================
# DAY 6 — FILE HANDLING & EXCEPTION HANDLING
# ========================
print("DAY 6 — File Handling & Exceptions")


# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Hello! This is a sample file.")


# Reading file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File Content:", content)


# Exception handling
# Exception handling
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Completed execution.")

# Exercise: Count number of words in any file