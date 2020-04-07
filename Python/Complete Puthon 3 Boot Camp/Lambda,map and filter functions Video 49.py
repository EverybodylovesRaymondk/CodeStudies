#Lambda,map and filter functions
#-----Map function 
def square(num):
    return num**2
my_nums = [1,2,3,4,5]
#using the map functi. n I can call the square funtion and use the my_nums variable to perform the function of the square funtion on 
for item in map(square,my_nums):
    print(item)
#using the maps function I can return a list of the results of the square function
my_list = list(map(square,my_nums))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return "EVEN"
    else:
        return mystring[0]

names=["Andy", "Eve","Sally"]

print(list(map(splicer,names)))

#-----Filter function 
#This requires functions that returns boolean values

def check_even(num):
    return num%2==0

mynums=[1,2,3,4,5,6]
my_filter=list(filter(check_even,mynums))


#-----lambda function 
#Standard function. 
def Ssquare(num):
    result = num ** 2
    return result
#Lambda version of Ssquare function 
lambda num : num **2

#A lambda expression can be assigned to variables 
sqr=lambda num: num ** 2

#Using the lambda function with map
print(list(map(lambda num : num**2 , my_nums)))

#Using the lambda function with filter
print(list(filter(lambda num:num%2 ==0, my_nums)))

#Returning the first character of teh names variable using lambda 
print(list(map(lambda letter:letter[0],names)))

#Returning the reverse of every name in the names variable using lambda expression 

print(list(map(lambda reversename : reversename [::-1],names)))