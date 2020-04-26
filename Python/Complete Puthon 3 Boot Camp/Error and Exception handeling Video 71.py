#Error and Exception handeling Video 71

#Creating an error 
def add(n1,n2):
    print(n1+n2)
    

try:
    number1=10
    number2=input("Please give a numner: ") # by making number an input it is a string, without casting this to int, it will create a typeError
    result = add(number1,number2)
except TypeError: #defining the actual error will allow you to have error specific excepts 
    #Statement to print when there is an error 
    print("Hey looks like you are not adding correctly")
else:
    print("Add went well")
    print(result)
finally:
    print("You should consider casting the input to the correct data type")
    
#Using while loops to keep asking untill there is no exceptions 
    
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number : "))
        except:
            print("That is not a number RTFQ!!")
            continue
        else:
            print("input {} is a number".format(result))
            print(result**2)
            break
        finally:
            print ("End")
ask_for_int()