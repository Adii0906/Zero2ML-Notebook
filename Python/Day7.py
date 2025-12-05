# ========================
# DAY 7 — OS, JSON, COLLECTIONS
# ========================
print("DAY 7 — OS, JSON & Collections Module")


import os
import json
from collections import Counter, defaultdict


print("Current Directory:", os.getcwd())
print("Files:", os.listdir())


# JSON example
user = {
"name": "Elliot",
"batch": 2025,
"skills": ["Python", "Streamlit", "Automation"]
}


with open("user.json", "w") as f:
	json.dump(user, f, indent=4)


with open("user.json", "r") as f:
	print("Loaded JSON:", json.load(f))


# Collections module
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(words)
print("Word Count:", counter)


def_dict = defaultdict(int)
def_dict["views"] += 1
print("Defaultdict Example:", def_dict)


# Exercise: Explore deque from collections