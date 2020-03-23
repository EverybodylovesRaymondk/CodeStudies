#Python Opperators 
# The Range operator
mylist = [1,2,3]
#This will return all the numbers from 0 to 10 in a step size of 2
for num in range(0,10,2):
    print(num)
    
# Enumerate thi will return a tuple of the variable created e.g. (0 , "a") with tuple unpacking i can return the index and the value seperatly and print them as lines
word = "abcde"
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
    
#The ZIP Function. 
#Zip will combine lists up until the last element of teh shortest list only
mylist1=[1,2,3,4,5,6]
mylist2=["a","b","c"]
mylist3=[100,200,300]

for item in zip(mylist1,mylist2,mylist3):
    print(item)

# The IN operator
    #Checing if x is in the list and printing the boolean result. 
print("x" in ["x","y","z"])

#Min and max of a list
mynumlist=[10,20,30,40,100]
print(min(mynumlist))
print(max(mynumlist))

#The Random library
#Shuffeling 
#the shuffle function will shuffle the order of a list
from random import shuffle
myrandomlist=[1,2,3,4,5,6,7,8,9,10]
shuffle(myrandomlist)

#Selecting random int using the random library 
from random import randint
# This will return a random int from 0 to 100
print(randint(0,100))

#User input and casting it to a data type other than a string
result = float(input("Enter your number here :  "))