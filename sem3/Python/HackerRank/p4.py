'''
task: 
    Given an integer, n, perform the following conditional actions:
    1: n odd then print weird
    2: if n even and range(2, 5) print not weird
    3: if n even and range(6, 20) print weird
    4: if n even and greater than 20 print not weird
'''

a = int(input("enter a number: "))

if(a % 2 != 0):
    print("weird")
elif(a % 2 == 0) or (2 < a < 5):
    print("not weird")
elif(a % 2 == 0) or (6 < a < 20):
    print("weird")
elif(a % 2 == 0) or (a > 20):
    print("not weird")