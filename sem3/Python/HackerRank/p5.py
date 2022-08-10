'''
the provided code stub reads and integer, n, from STDIN. for all
    non-negetive integers i < n; print i^2.
'''

n = int(input("enter an integer: "))

for i in range(0, n, 1):      # o = starting point, n means terms
    print(i * i)