# Named Tuple video 90
#Creating a normal tuple
t = (1,2,3)
print(t[0])

#creating a named tuple
from collections import namedtuple
#Creating the tuple "Dog" with names and value parameters (age,breed,name)
Dog = namedtuple('Dog','age breed name')

sam = Dog(age=2,breed='lab',name='Sammy')

print(sam.age)
print(sam.name)
print(sam.breed)