# List Iteration
l = ["harshil", "jimmy$"]
for i in l:
    print(i)
    
# String Iteration
s = "har"
for k in s:
    print(k)
    
# dictonary Iteration
sac =   {
            'Gujarat' : 'Gandhinagar',
            'Maharashtra' : 'Mumbai',
            'Rajasthan' : 'Jaipur',
            'Bihar' : 'Patna'
        }
for s in sac:
    print(s)
    
# Iterating over dictionary
d = dict()
d['abc'] = 123
d['def'] = 456
for i in d :
    print("%s  %d" % (i, d[i]))
    
#Iterating over a set
print("\nSet Iteration")
set1 = {1,2,3}
for i in set1:
    print(i)