#------------------Statements Assessment Test-----------------------

#-------Task 1: Using the for and split() create a statement that will print out words starting with S

st="Print only the words that start with s in this sentence"

#Splitting the string into a list of words

stringlist=st.split()

#Looping through the list of words in the list and looking for words starting with s to print them
for word in stringlist:
    if word[0]=="s":
        print(word)
        
#--------Task 2 : using range print all the even number from 0 to 10
even_numbers =[x for x in range(0,11) if x%2==0]
print(even_numbers)

#--------Task 3 : Use list comprehension to create a list of all the numbers between 1 and 50 that are evenly divisible by 3
numberD3=[num for num in range(0,51) if num%3==0]

#--------Task 4 : Go through the string below and if the length of a word is even print "even!"
st2 = 'Print every word in this sentence that has an even number of letters'

for word in st2.split():
    if len(word)%2 == 0 :
        print(word + " <--has an even amount of characters")
    else:
        print(word+ " <--has an odd amount of characters")
        
#--------Task 5 : Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,101):
    if num %3 == 0 and num % 5 == 0:
        print(str(num) + " (FizzBuzz)")
    elif num % 3 == 0:
        print(str(num) + " (Fizz)")
    elif num % 5 == 0 :
        print (str(num) + " (Buzz)")
    else:
        print(num)

#--------Task 6 : Use List Comprehension to create a list of the first letters of every word in the string below:

st3='Create a list of the first letters of every word in this string'

firstd=[word[0] for word in st3.split()]