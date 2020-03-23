#Functions

def name_function():
    '''
    DOCSTING: INFORMATION ABOUT FUNCTION
    '''
    print("hello")
name_function()
help(name_function)

# Creating a function with a optional parameter 
def say_hello(name="NAME"):
    ''' This function requires a name as input'''
    print("hello " + name)
help(say_hello)
say_hello()

#Creating a function and saving its result as a variable

def add(n1,n2):
    return n1+n2

total=add(1,5)
print(total)

#Creating a function to check for a word in a string

def word_check(mysting):
    return "dog" in mysting.lower()

print(word_check("The Dog did doggy style"))

#Creating a function to generate pig latin

def pig_latin(word):
    first_letter = word[0]
#check if the firs letter is a voul
    if first_letter in 'aeiou':
        pig_word = word + "ay"
    else:
        pig_word = word[1:] + first_letter + "ay"
    return pig_word

print (pig_latin("word"))