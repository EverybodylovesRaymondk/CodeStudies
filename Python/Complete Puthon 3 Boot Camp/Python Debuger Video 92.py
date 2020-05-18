#Python Debuger Video 92
import pdb

x=[1,3,4]
y=2
z=3

result = y + z
print(result)

--pdb.set_trace() #will open the debuch section in the console
result2 = y + x # this line will give an error
print(result2)