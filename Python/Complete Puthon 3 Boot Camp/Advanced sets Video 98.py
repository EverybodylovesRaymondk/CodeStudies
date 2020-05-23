#Advanced sets

s = set()
s.add(1)
s.add(2)
print(s)

#Clearing all values from the set
s.clear()
print(s)
s ={1,2,3}

#copying a set
sc=s.copy()
print(sc)
s.add(4)
#Differnce method .  This will return the element that differ between s and sc
print(s.difference(sc))

#Differnce update method. will return the remaining characters in s1 after removing the onces found in s2
#i.e 1 is a common character and will be removed from s1 before returning the remaining of s1
s1={1,2,3}
s2={1,4,5}

# Discard method will discard a list item if it is part of the list
s1 = {1,2,3}
print(s1)
s1.discard(2)
print(s1)

#Intersection Method, will return elements that are shared between sets

s1 = {1,2,3}
s2 = {1,2,4}
x=s1.intersection(s2)
print(x)

#Intersection update , will update the original set (s1) with the intersection values of the comparison set i.e s1 will be set to {1,2)}
s1.intersection_update(s2)
print(s1)

#Isdisjoint method. will return true when 2 sets have no common values
s1={1,2}
s3={5}
print(s1.isdisjoint(s3))

#Comparing 2 sets and returning the values not found in both sets
s1={1,2}
s2={1,2,4}
print(s1.symmetric_difference(s2))

#Returning all elements in 2 different sets
x=s1.union(s2)
print(x)

#Updating one set to the values of another updating s1 with values from s2.
s1.update(s2)
print(s1)