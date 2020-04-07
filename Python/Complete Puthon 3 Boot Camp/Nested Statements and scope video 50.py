#Nested Statements and scope video 50
x = 25 
def printer():
    x = 50
    return x
print(x)
# At this point x wil remain 25 as the function printer only assigns the value of 50 to x within itself (locally) withougt affecting the global x variable

#Retruning the x value within ghe function printer
print(printer())

#Python variable hierarcy (LEGB Rule) in order of lowest to highest/ python looks from lowest to hightest. 
#L : Local - names assigned within a function (def of lambda).
#E : Enclosing Finction Local - names defined inside a function having another funcion within it
#G : Global - names defined at the top level of the module file or declared globaly in a function (def)
#B : Build in- names preassignded in the build in names e.g. open, range etc shown with syntax highlights 


#Python will use the local variable("I am a local") first, then the enclosing ("Sammy"), and then only the global ("This is a global string") when executing code using the same variable name (name)

#global 
name = "THIS IS A GLOBAL STRING"

def greet():
    # Enclosing
    name = "Sammy"
    def hello():
        #Local
        name = "I am a local" 
        print("Hello "+ name)
    hello()
greet()

#Affecting the global name / variable using local name/variables WARNING: Using the global key word inside a function will affect the global variable and must be done cautiously. 

y=50

def func():
    global y #this will result in the y variable declared globally being effected by the function
    print(f'y is {y}')
    #Local reassignment
    y = 200
    print ( f"I just locally changed GLOBAL y to {y}")
func()
print(y)

