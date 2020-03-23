#Function practice Excersises.
#------------Task 1 LESSER OF TWO EVENS: 
#Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_events(a,b):
    if a % 2 == 0 and b % 2 == 00:
        return min(a,b)
    else:
        return max(a,b)
    
print(lesser_of_two_events(2,4))

#------------Task 2 ANIMAL CRACKERS:
#Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    wordlist = text.split()
    if wordlist[0][0].lower() == wordlist[1][0].lower():
        return True
    else:
        return False

print(animal_crackers("This two worlds"))

#------------Task 3 MAKES TWENTY: 
#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(x,y):
    if x + y == 20:
        return True
    elif x == 20 or y == 20:
        return True
    else:
        return False
print(makes_twenty(2,10))

