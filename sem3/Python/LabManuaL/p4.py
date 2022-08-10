# factorial 

n = int(input("enter a number: "))

factorial = 1
if (n < 0):
    print("factorial doesn't exist for negetive numbers")
elif (n == 0):
    print("The factorial of 0 is 1")
else:
    for i in range(1, n+1):
        factorial = factorial * i
    print("the factorial of", n, "is", factorial)