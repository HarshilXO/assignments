'''
determine leapyear or not; if yes -> boolean true otw boolean false.
uisng function.
'''
a = int(input("enter integer to find it's leapyear or not: "))

def leapyear():
    if (a % 4 == 0):
        print(True)
    else:
        print(False)
        
leapyear()  