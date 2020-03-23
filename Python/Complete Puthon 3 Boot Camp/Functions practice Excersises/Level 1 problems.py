#----------------Level 1 Problems-----------
#------------Task 1
#Write a function that capitalizes the first and fourth letters of a name
def old_macdonald (name):
    name_list= name.split()
    if (len(name_list[0])>3):
        return name_list[0][:3].capitalize() + name_list[0][3:].capitalize()
    else:
        return False
print(old_macdonald("macdonald"))

#------------Task 2
#MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
   return " ".join(text.split()[::-1])

print(master_yoda("I am home"))

#------------Task 3
#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(x):
    value=int(round(x,0))
    if (abs(100 - value) <=10) or (abs(200 - value) <=10):
        return True
    else:
        return False
print(almost_there(150))