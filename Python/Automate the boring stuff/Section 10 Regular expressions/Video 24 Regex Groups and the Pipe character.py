import re 

msg1='My number is 415-555-4242'
#Creating a regex object using the () to specify groups. 
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

#Searching the string and creating a match object
mo = phoneNumRegex.search(msg1)
#Returning group 1 of the matched object
print (mo.group(1))

#Returning group 2 of the matched object
print(mo.group(2))


#To find actual () in the string it needs to be escape coded 

msg2='My number is (415) 555-4242'

phoneNumRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo2 = phoneNumRegex2.search(msg2)
print(mo2.group())


# Using the pipe operator will allow you to search with a prefix for many words.(Note: Case sensativity is applicable when creating the regex object)

Batmsg = 'The batmobile lost a wheel' 
batRegex = re.compile(r'BAT(MAN|MOBILE|COPTER|BAT)')
mo3 = batRegex.search(Batmsg.upper())
print(mo3.group())