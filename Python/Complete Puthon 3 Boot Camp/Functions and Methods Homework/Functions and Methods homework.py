#Functions and Methods homework

#---------Task 1: 
# Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    result = ((4/3)*(3.14)*(rad**3))
    return result

print(vol(2))

#---------Task 2:
#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    return num >= low and num <= high

print(ran_check(5,2,7))

#---------Task 3:
#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def upper_lower(string):
    '''This uses a dictionary of variables to track a value of those variables.
    Returning a count per variable of the upper and lowercase letters in the required string argument'''
    d={"Upper":0,"Lower":0}
    for i in string:
        if i.isupper():
            d["Upper"]+=1
            
        elif i.islower():
            d["Lower"]+=1
        else:
            pass
    print("Original : " , string)
    print("No. of Upper case characters : " , d["Upper"])
    print("No. of Loser case characters : " , d["Lower"])
    
#help(upper_lower)
upper_lower("THE lady IN the HOUSE")

#---------Task 4:
#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(y):
    x = []
    for i in y:
        if i not in x:
            x.append(i)
    return x
    
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5,6]))

#---------Task 5:
#Write a Python function to multiply all the numbers in a list.
def multiply(lst):
    x=1
    for i in lst:
        x = x * i 
    return x
  
print(multiply([1,2,3,-4]))

#---------Task 6:
#Write a Python function that checks whether a passed in string is palindrome or not.

def palindrome(s):
    lists=list(s.replace(' ' , ''))
    rlists=lists[::-1]
    print(lists)
    print(rlists)
    print(lists == rlists)
    print(len(rlists))
    
palindrome("nurses run")

#---------Task 7:
#Write a Python function to check whether a string is pangram or not.
import string

def ispangram(sinput ,  alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    print( alphaset <= set(sinput.lower()))
   
ispangram("This is a string")