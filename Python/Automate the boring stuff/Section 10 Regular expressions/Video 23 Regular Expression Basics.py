import re

message = 'Call me 415-555-0110 tomorrow , or 415-555-9999'

#Creating a pattern \d will find digits in a string
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#Findall will retrun a list of every match made to the pattern definded above
mo = phoneNumRegex.findall(message)

#Printing the results of the list above
for i in mo:
    print(i)