#CollectionModue Counter video 87
#Counter
#A counter is dictionary that caounst hashful objects
from collections import Counter

#l = [1,1,1,1,1,5,5,5,6,68,4,58,4,6,6,6,7,1,2,3,]
#print(Counter(l)) # will return how many times each number is in the list l
#
#s = 'assssbabbbavavavafdads'
#print(Counter(s))

#Counting how many times a word is in a sentecne

s2 = 'How many times does each word show up in this sentence word word shoe up up'
word = s2.split()
print(Counter(word))

# Performing functions with counter

c = Counter(word)
#print out of the 2 most common words is the s2
print(c.most_common(2))
#Printing the total amount of words of a s2
print(sum(c.values()))