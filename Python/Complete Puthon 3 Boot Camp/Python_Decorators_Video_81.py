##Python_Decorators_Video_81
##The decorator uses the @ operator allowing the addition of more functionality to an existing function
#
#def func():
#    return 1
#
#print(func())
#
###### Assigning a function to a variable #### 
#def hello():
#    return "Hello"
#print(hello())
##Setting greet to be hello
#greet = hello
#print(greet())
##deleting hello 
#del hello
#print(greet())
##print(hello()) # will present an issue as hello no longer exists 
#
###### Passing/ calling functions within another function #### 
##refer to scope and nested statement lecture 
#
#def hello2(name='Jose'):
#    print('The hello2() funciton has been exicuted')
#    
#    def greet2 ():
#        return '\t This is the greet2() function inside hello2'
#    def welcome():
#        return '\t This is welcome inside hello2'
#    
#    print(greet2())
#    print(welcome())
#    print('This is the end of the hello2() function')
#    # retruning the greet2 and welcome functions based on a condition
#    
#    if name == 'Jose':
#        return greet2
#    else:
#        return welcome
#hello2()
#my_new_func = hello2()
#print(my_new_func())
#
###### Setting a function as an argument #####
#
#def hello3():
#    return ' Hi Jose'
#def other(some_def_function):
#    print('Other code runs here')
#    print('\t'+some_def_function())
#other(hello3)

#### Creating a decorator ####

def new_decorator(original_function):
    print('\n'*1)
    def wrap_func():
        print('Some extra code before original function')
        
        original_function()
        
        print('Some extra code after the original function')
        print('\n'*1)
        
    return wrap_func

def func_needs_decorator():
    '''
    This is passed as the original function in the above function
    '''
    print('I want to be decorated!!')
    
decorated_func = new_decorator(func_needs_decorator)
decorated_func()


### A shorter way ###
#Using the @ function I can run the new decorater function pasing in the holy function into the original functions place
@new_decorator
def holy():
    print('I want to be short!!')
holy()