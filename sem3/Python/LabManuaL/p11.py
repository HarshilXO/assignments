a = input("enter emp name: ")
b = int(input("enter emp id: "))
c = int(input("enter emp salary: "))

def manager():              
    z = c + 5000
    print("Name: ", a)
    print("ID: ", b)
    return z

def generalmanager():
    print("Name: ", a)
    print("ID: ", b)
    x = c + 10000
    return x 

def ceo():
    print("Name: ", a)
    print("ID: ", b)
    y = c + 20000
    return y

def worker():
    print("Name: ", a)
    print("ID: ", b)
    u = c + 2000
    return u

d = str(input("enter designation: (m, g, c, w) "))
if(d == 'm'):
    print("increased salary: ", manager())

elif(d == 'g'):
    print("increased salary: ", generalmanager())

elif(d == 'c'):
    print("increased salary: ", ceo())

elif(d == 'w'):
    print("increased salary: ", worker())

else:
    print("invalid.")