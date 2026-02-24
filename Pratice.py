arr = [1, 2, 3, 4, 5]

print("Array:", arr)
print("Length of array:", len(arr))
print("Last index:", len(arr) - 1)

left= 0
right= len(arr)-1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)


arr = [1,2,3,4,5,6]
target = 6

n = len(arr)

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print("Target found at indices:", i, j)
            print("Values:", arr[i], arr[j])