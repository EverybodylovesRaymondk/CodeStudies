#Error and exception handeling homework video 72
import math

#Problem 1 
try:
    for i in ['a','b','c']:
        print (i**2)
except:
    print("Only numbers allowed")
    
#Problem 2

try:
    x=5
    y=0
    z=x/y
    print(z)
except:
    print("Can't devide by 0")
    
#Problem 3

def ask_int():
    while True:
        try:
            number = int(input("Please give a number : "))
            print( math.pow(number,2))
        except:
            print("This is not a number")
            continue
        else:
            break
        
ask_int()