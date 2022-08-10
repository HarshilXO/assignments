n = int(input("enter number of elements: "))
arr = list()

for i in range(n):
    arr.append(int(input()))

print("array: ", arr)
print("sum = ", sum(arr))