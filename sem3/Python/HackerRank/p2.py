'''
Task:
    The provided code stub reads two integers from STDIN, a and b. 
    Add code to print three lines where:
    1: The first line contains the sum of the two numbers.
    2: The second line contains the difference
        of the two numbers (first - second).
    3: The third line contains the product of the two numbers.
'''

a = int(input("enter a: "))
b = int(input("enter b: "))

def sum():
    c = a + b
    return c

def sub():
    d = a - b
    return d

def product():
    e = a * b
    return e

print(sum())
print(sub())
print(product())