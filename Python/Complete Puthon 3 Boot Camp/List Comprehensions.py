#List Comprehensions
mystring = "Hello"
#creating a list of the leters in the mystring variable using for loop
mylist=[]
for letter in mystring:
    mylist.append(letter)

#The same results above can be achived using the following code 
    
mystring2="Hello _ 2 "
mylist2=[letter for letter in mystring2]

#usint list comprehension to create a list of number for a range of values
mynumlist=[num for num in range(0,11)]

#Performing opperations on variable in list comprehensions e.g creating a list of the squared number for a range of values
mynumlist= [num **2 for num in range (0,11)]

#Creating list comprehensions with conditions e.g creating list of number for a range of values where the value is an equal number 
mynumlist=[num for num in range(0,11) if num%2==0]

#Using list comprehension to conver values in a list 
celcuis = [0,10,20,34.5]
fahrenheit =[((9/5)*temp+32) for temp in celcuis]

#Using list comprehension with if / else to find create a list of values or odd values for a range of values 

ifelse=[x if x%2==0 else "ODD" for x in range(0,11)]
print(ifelse) 