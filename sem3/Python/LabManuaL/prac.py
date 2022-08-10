# recursive funtion 

a = int(input("enter a value to find factorial: "))

def fact(a):
    if (a == 0):
        return 1
    elif (a == 1):
        return 1
    else:
        return (a * fact(a - 1))
    
print("factorial of", a, "is: ", fact(a))