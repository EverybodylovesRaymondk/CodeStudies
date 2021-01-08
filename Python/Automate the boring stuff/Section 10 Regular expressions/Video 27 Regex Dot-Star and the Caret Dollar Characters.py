import re

#The ^ when used at the start of a regex expression indicates that the match must be at the start of the expression

helloRegex1 = re.compile(r'^Hello')
msg1 = 'Hello he said'
mo1 = helloRegex1.search(msg1)

try:
    print('mo1 = ' + mo1.group())
except:
    print('Match not found')


#The $ when used at the end of a regex expression indicates that the match must be at the start of the expression

helloRegex2 = re.compile(r'world!$')
msg2 = 'Hello world!'
mo2 = helloRegex2.search(msg2)

try:
    print('mo2 = ' + mo2.group())
except:
    print('Match not found')

#The . refers to eny character excluding the new line 

atRegex = re.compile(r'.at')
msg3 = 'The cat in the hat sat on the flat mat.'
mo3 = atRegex.findall(msg3)

try:
    print('mo3 = ' + str(mo3[:]))
except:
    print('Match not found')


#The .* refers to eny character for any amount of characters excluding the new line
#Creating a regex to extract any and any number of characters between two set patterns (First Name : and Last Name: )

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
msg4 = 'First Name: Al Last Name: Sweigart'
mo4 = nameRegex.findall(msg4)

try:
    print('mo4 = ' + str(mo4[:]))
except:
    print('Match not found')


#The re.DOTALL argument will include new lines when using the .* 

prime = 'Serve the public.\nProtect the guilty.\nUpload the law'

dotStar = re.compile(r'.*',re.DOTALL)
mo5 = dotStar.search(prime)
print(mo5.group())

# the re.IgnoreCase(re.I) is used to make the regex expression case in sensative
vowelRegex3 = re.compile(r'[aeiou]',re.I)
msg6 = 'All , why does you programming book tak about RoboCop so much?'
mo6 = vowelRegex3.findall(msg6)
print('mo6 = ' + str(mo6))