#orderDict Video 89
#This dictionary maintains the order of the vaues

#Creating a normal dictionary
normald={}
normald['a']=1
normald['b']=2
normald['c']=3
normald['d']=4
normald['e']=5
normald

for k,v in normald.items():
    print(k,v)

print('\n'*2)

#Creating order dictionary
from collections import OrderedDict

orderd=OrderedDict()
orderd['a']=1
orderd['b']=2
orderd['c']=3
orderd['d']=4
orderd['e']=5

for k,v in orderd.items():
    print(k,v)