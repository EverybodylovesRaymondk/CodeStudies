import re

#Creating a straight forwared regex object

phoneRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
msg1 = 'Thee is so many numbers 451-555-0000 and also 451-333-6666 but then there is also 777-666-8888'
mo1 = phoneRegex1.findall(msg1)

for i in mo1:
    print('mo1 = ' + i)

#Creating a regex object with groups Note : when regex has groups the findall will return a list of touples 

phoneRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
msg2 = 'Thee is so many numbers 452-555-0000 and also 452-333-6666 but then there is also 777-666-8888'
mo2 = phoneRegex2.findall(msg2)

for i in mo2:
    print('mo2 = '+ str(i[:]))

#Creating your own character classes : This will find upper and lower case vowels

vowelRegex1 = re.compile(r'[aeiouAEIOU]')
msg3 = 'Robocop eats baby food'
mo3 = vowelRegex1.findall(msg3)

print('mo3 = '+ str(mo3))
    
#Creating your own character classes : This will find 2 consecutive upper/lower case vowel 

vowelRegex2 = re.compile(r'[aeiouAEIOU]{2}')
msg4 = 'Robocop eats baby food'
mo4 = vowelRegex2.findall(msg4)
print('mo4 = ' + str(mo4))


    
#Creating your own character classes : This will find all characters that is not a upper/lower case vowel including punctuation and digits

vowelRegex3 = re.compile(r'[^aeiouAEIOU]')
msg5 = 'Robocop eats baby food'
mo5 = vowelRegex3.findall(msg5)
print('mo5 = ' + str(mo5))