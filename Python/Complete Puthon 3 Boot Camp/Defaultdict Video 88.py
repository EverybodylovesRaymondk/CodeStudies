#Defaultdict Video 88
#A default dictionary will never return a key error if the key is not found it will return the default value
from collections import defaultdict
#Example of a nomral dictionary
normald = {'k1':1}
#print(normald['k1'])
#print(normald['k2']) # this will return a KeyError

#Example of default dictionary
defd = defaultdict(object)
defd['one']
for item in defd:
    print(item)

dlamda = defaultdict(lambda: 'na')
#Printing key "one" because it is not assigned a value it wil be set to the default of 0
print(dlamda['one'])
#Printing key "two" because it is assigned a value it will print the value
dlamda['two']=2
print(dlamda['two'])
#Printing the entire default dictionary will return the key 'one' as 'na' and 'two' as 2 based
print(dlamda)