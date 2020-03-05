#For Loops
my_list=[1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(num)

#Retuning only the even numbers
for num in my_list:
    """check if number is even"""
    if num % 2 ==0:
        print("Even number : {}".format(num))
    else:
        print("Odd number : {}".format(num))

#Summating items in the lisit
list_sum = 0
for num in my_list:
    list_sum=list_sum + num
print(list_sum)

#For loops with strings
my_string="Hellow World"
for letter in my_string:
    print(letter)
    
#For loops for Tuples
tup=(1,2,3)
for item in tup:
    print(item)
    
#Tuple unpacking with for loop
my_tuple_list =[(1,2),(3,4,),(5,6),(7,8)]

for (a,b) in my_tuple_list:
    print(a)
    print(b)
    
#Iterating throug a dictionary with for loops retruning it as a tuple
d = {"k1":1,"k2":2,"k3":3}
for items in d.items():
    print(items)
    
#Using tuple unpacking we can return the values of the dictionary only 
for (key,value) in d:
    print(value)