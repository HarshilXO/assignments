pi = 3.14

a = int(input("enter length: "))
b = int(input("enter breadth: "))
c = int(input("enter height: "))
d = int(input("enter radius: "))

def circle():
    e = pi * d * d
    return e
    
print("area of circle: ", circle())

def rectangle():
    f = a * b
    return f
    
print("area of rectangle: ", rectangle())

def square():
    g = a * a
    return g
    
print("area of square: ", square())

def triangle():
    h = a * b * c
    return h
    
print("area of triangle: ", triangle())