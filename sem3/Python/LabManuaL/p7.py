arr = list()    
n = int(input("enter the number of element: "))

print("enter integers in array: ")

for i in range(int(n)):
    a = int(input("n: "))
    arr.append(a)
    
print('Array: ', arr)

# print("largest no is: ", max(arr))

def largest(arr):
    d = max(arr)
    # print("largest no is: ", d)
    return d

# largest(arr) 
print("largest no: ", largest(arr))