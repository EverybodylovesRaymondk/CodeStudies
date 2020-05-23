##Regular expressions Video 94
## This is text matching patterns
#
import re

# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

#Creating function to search the string of variable "text" for the item in the patterns list i.e term1 or term2

def text_search ():
    '''
    This function will search the string assigned to variable text for each sting as in the patterns list variable
    '''
    for pattern in patterns:
        print('Searching for "%s" in:\n "%s"\n' %(pattern,text))

    #Check for match
        if re.search(pattern,text):
            print('Match was found for "%s". \n'%(pattern))
        else:
            print('No Match was found.\n')

#splitting using regular expression

split_term = '@'

phrase = 'What is your email, is it hello@gmail.com?'

print(re.split(split_term,phrase))

#Finding all instances of the pattern and counting how many there are using the len function

print(len(re.findall('match','Here is one match,here is another match')))

#####Searching using metaCharacters######

#Repetition syntax

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(patterns,phrase))
        print('\n')

test_phrase = 'sss'
test_pattern = "s{7}"

multi_re_find(test_pattern,test_phrase)

#Exclusion syntax
#We can exclude the punctutation from the string using the ^ metacharacter followed by the vaules to be excluded
string='This is a string! But it has punctutation. How can we remove it?'
print(re.findall('[^!.?]+',string))