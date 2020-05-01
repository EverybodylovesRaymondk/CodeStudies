#Generators Video 83
#Allowing the generation of value over time. The   statment is used to achive this
#range() is an example of a generator
#Generator functions require itterations
#Generator functions are memory efficient

#Example funciton ###

def create_cubes(n):
    result=[]
    for x in range(n):
        result.append(x**3)
    return result
#The issue here is python now keeps the entire result list in memory
print(create_cubes(10))

#Using generator ###

def create_cubes2(n):
    for x in range(n):
        yield x**3

print(create_cubes2(10 )) # This will not print the list it requires itteration
#Creating the itteration for the generatoer function create_cubes2
for x in create_cubes2(10):
    print(x)

##Calculating the Fibonatchi sequence with geneator functions##
def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b
for number in gen_fibon(10):
    print(number)

#Using the Next fuction with genarator functions
def simple_gen():
    for x in range(3):
        yield x
g=simple_gen()
print(next(g))
print(next(g))
print(next(g))
#print(next(g)) # at this point the range is depleted an the next itteration of g can't be returned (StopIteration)

# Using the iter function to create a itteable instance of a variable

s = 'Hello'
s2 = iter(s)
print(next(s2))