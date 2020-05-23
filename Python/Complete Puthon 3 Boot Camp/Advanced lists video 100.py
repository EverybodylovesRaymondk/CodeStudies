#Advanced lists video 100

l = [1,2,3]
#Adding a item to the list
l.append(4)
print(l)

#counting how many time a value is in the list
print(l.count(10))
print(l.count(4))

#Extending a list
x = [1,2,3]
x.append([4,5]) # will ad the list as a element in the existing list
print(x)
x = [1,2,3]
x.extend([4,5]) #will add 4 and 5 as elements in the list
print(x)

#Finding the index where a value is kept in a list
print(l.index(2))

#Adding a element to the list at a specific index
l.insert(2,'Inserted')
print(l)

#Removing the last element in a list
lastelement = l.pop()
print(lastelement)

#Removing a element at a specific index of the list
element2=l.pop(2)
print(element2)

#Removing the first occurance of a value in the list
l = [1,2,3,4,3]
l.remove(3)
print(l)

#Reversing a lists order
l.reverse()
print(l)

#Sorting a list
l.sort()
print(l)