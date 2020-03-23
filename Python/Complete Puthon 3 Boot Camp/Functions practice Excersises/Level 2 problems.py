#----------------Level 2 Problems-----------
#------------Task 1 
#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(0, len(nums)-1):
      
        # nicer looking alternative in commented code
        if nums[i] == 3 and nums[i+1] == 3:
    
        #if nums[i:i+2] == [3,3]:
            return True  
    
    return False

print(has_33([1,3,3,3]))

#------------Task 2
#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(value):
    my_string=''
    for i in value:
        my_string += i*3
    return my_string

print(paper_doll('Mississippi'))

#------------Task 2
#BLACKJACK: Given three integers between 1 and 11, 
#Condition 1 :if their sum is less than or equal to 21, return their sum. 
#Condition 2 : If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
#Condition 3 : Finally, if the sum (even after adjustment) exceeds 21, return 'BUST 

def blackjack(n1 , n2 , n3):
    
    if sum((n1,n2,n3))<=21:
        return sum((n1,n2,n3))
    
    elif sum((n1,n2,n3)) <= 31 and 11 in (n1,n2,n3): # condition 2 is met by checking if the sum of the elements + 10 is less than 31 (21+10) and if 11 is a element. 
        return sum((n1,n2,n3))-10
    else:
        return "Bust"
print(blackjack(9,9,9))

#------------Task 3
#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers

