# factorial 

n = int(input("enter n: "))

fact = 1

if (n < 0):
    print("input should be +ve integer!")
elif(n == 0):
    print("factorial of 0 is 1.")

while (n > 0):
    fact = fact * n
    n = n - 1
    print("factorial = ", fact)