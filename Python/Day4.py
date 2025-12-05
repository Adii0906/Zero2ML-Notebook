print("DAY 4 — Python Advanced Concepts")


# Enumerate
# Enumerate
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
	print(index, color)

# Zip
# Zip
names = ["A", "B", "C"]
marks = [90, 85, 70]
for n, m in zip(names, marks):
	print(n, m)

# Map & Filter
nums = [1, 2, 3, 4, 5]


# Map: square all numbers
sq = list(map(lambda x: x * x, nums))
print("Squares:", sq)


# Filter: even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)


# Generator



def number_generator():
	for i in range(5):
		yield i

print("Generator Output:")
print("Generator Output:")
for num in number_generator():
	print(num)

# Exercise: Create a generator that yields Fibonacci numbers up to 10

