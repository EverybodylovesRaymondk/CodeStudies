#*args and **kwargs
# Using the *args parameter will allow the user to pass multiple parameters to the function
#Note the *args will be kept in a touple 
#Note the term args can be changed to anything e.g. *samples
def myfunc(*args):
    return (args)

print(myfunc(60,40,80,20))

#Using the **kwargs will allow the user to pass multiple parameter to the function 
#Note these parameters will create a dictionary
#The function will return the value assigned to the key word fruit
#Note the term kwargs can be changed to anything e.g. *samples

def myfunct(**kwargs):
    '''This function returns the value assigned to the keyword 'fruit' or that no fruit was found'''
    if "fruit" in kwargs:
        print("My fruit of couce is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")
myfunct(veggie="apple")

#Creating a function that uses both *args and **kwargs

def newfunc(*args,**kwargs):
    ''' The function will return the sum of the arguments and the element assigned to the key food '''
    print("I would like {} {}".format(sum(args[::]),kwargs["food"]))
    
newfunc(10,20,30,food="eggs")

