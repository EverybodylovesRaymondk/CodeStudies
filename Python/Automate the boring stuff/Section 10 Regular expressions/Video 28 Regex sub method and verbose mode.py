import re
#The sub() method will substitude values found with a specified value

msg1 = 'Agent Alice gave the secret documents to Agent Bob who at dinner with agent Raymond'

namesRegex = re.compile(r'Agent \w+')
mo1 = namesRegex.findall(msg1)
mo2 = namesRegex.sub('REDACTED',msg1)

print(mo1)
print('SUB: ' + mo2)

#Creating regex to substitude a partial amount of the match

namesRegex2 = re.compile(r'Agent (\w)\w*')
mo3 = namesRegex2.sub(r'Agent \1****',msg1)
print('mo3= '+ mo3)

# Creating a regex expression with multiple match options and multiple second arguments

COMPLEX_PHONENUM = re.compile(r'''
           (\d\d\d-) #Area code (without () , with dash )
           | (\(\d\d\d\) ) # -or- area code with () and no dash
           \d\d\d # First 3 digits
           - # First dash
           \d\d\d\d #Last 4 digits''', re.I | re.DOTALL | re.VERBOSE
           )

print(COMPLEX_PHONENUM)