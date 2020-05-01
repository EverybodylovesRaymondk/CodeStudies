#Generator homework
import math
import random
####Problem 1#####

print("Problem 1")

def genarator1(n):
    for num in range(n):
        yield int(math.pow(num,2))

for x in genarator1(int(input("Enter number: "))):
    print(x)

print('\n' + 'Problem 2')

####Problem 2#####
def genarator2(low,high,n):
    for num in range(n):
        yield random.randint(low,high)

for xx in genarator2(low = int(input("Enter min value: ")),
                     high = int(input("Enter max value:")),
                     n=int(input("How many results: "))):
    print(xx)

print('\n' + 'Problem 3')

####Problem 3#####
s = 'hello'
its = iter(s)
print(str(next(its))+'\n'+ next(its))

print('\n' + 'Extra credit')

#### Extra Credit ####
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)