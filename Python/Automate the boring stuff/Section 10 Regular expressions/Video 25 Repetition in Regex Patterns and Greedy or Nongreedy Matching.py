import re

#The ? symbole is used to match the preceding group once or less

#creating a regex item to match Batman or Batwoman
batRegex1 = re.compile(r'Bat(wo)?man')

#Using the batRegex item to find Batman
msg1 ='The advanentures of Batman'
mo1 = batRegex1.search(msg1)
print('mo1 = '+mo1.group())

##Using the batRegex item to find Batwoman
msg2 ='The advanentures of Batwoman'
mo2 = batRegex1.search(msg2)
print('mo2 = '+mo2.group())

# The * symbole is used to match the preceding groupe 0 or more times 

batRegex2 = re.compile(r'Bat(wo)*man')

msg3 = 'The advanentures of Batwowowowowoman'
mo3 = batRegex2.search(msg3)
print('mo3 = '+mo3.group())

# The + symbole is used to match the preceding groupe 1 or more times

batRegex3 = re.compile(r'Bat(wo)+man')

msg4 = 'The advanentures of Batwoman'
mo4 = batRegex3.search(msg4)
print('mo4 = '+mo4.group())


# The {} symbole is used to match the preceding groupe a specific number of times

haRegex = re.compile(r'(Ha){3}')

msg5 = 'He said "HaHaHa"'
mo5 = haRegex.search(msg5)
print('mo5 = '+ mo5.group())


#Creating regex to match 3 phone number with optional area codes and comma seperation

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
msg6 = 'My numbers are 451-555-1234,555-4242,212-555-0000'
mo6 = phoneRegex.search(msg6)
for i in mo6.group().split(','):
    print('mo6 = ' + i)