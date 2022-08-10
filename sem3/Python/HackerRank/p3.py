'''
The provided code stub reads two integers, a and b, 
Add logic to print two lines. The first line should contain the result of integer division, a // b. 
The second line should contain the result of float division, a / b.
'''

a = int(input("enter a: "))
b = int(input("enter b: "))

def intdiv():
    c = a // b
    return c

def floatdiv():
    d = a / b
    return d 

print(intdiv())
print(floatdiv())