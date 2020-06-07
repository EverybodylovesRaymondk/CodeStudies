#Advanced Strings Vidoe 97
s = 'hello world'
#Changing cases
print(s.capitalize())
print(s.upper())

# Finding / counting letters
print(s.find('o')) # Will return the index of the first occurance of o
print(s.count('o'))

#Formatting
print(s.center(20,'z')) #will senter the string s between z's with a total lenght of 20 characters.
print(s + '\tHi') #using \t will print out a tab between the string and the next string 'Hi'
s='hello'
print(s.isalnum())
print(s.endswith('o')) # checking if s ends with letter o