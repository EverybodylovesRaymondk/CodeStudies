	#----------List basics--------
my_list=[1,2,3]
my_list=["string",100,23.2,"hope"]

#Retuning the lenght of a list len(my_list)
print("my_list contains {} characters ".format(len(my_list)))

#Returning a specific element from the list my_list[3]
print("The third item on my list is {}  ".format(my_list[2]))

#Concatenating lists my_list + another_list
another_list=["new List",1,2,3,50]
print(my_list+another_list)

#Saving the concatenaed list now as a new variable
new_list = my_list+another_list

#Replacing a element in a list
new_list[0]="One as a word"