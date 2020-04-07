#Challenging problems

#------------Task 1
#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    
    code = [0,0,7,"x"]
    """The function will look for the 007 value"""
    
    for num in nums:
        if num == code[0]:
            code.pop(0)
    
    return len(code) == 1
        
print(spy_game([1,2,4,0,0,7,5]))

#------------Task 2
#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    #Check for 0 and 1 input by convention they are not primes
    if num <2:
        return 0
    
    #input >=2
    primes =[2]
    x = 3 
    
    while x <= num :
        #checking if x is prime. 
        for y in range (3,x,2):
            if x % y == 0 :
                x +=2
                break
        else:
            primes.append(x)
            x +=2
    print(primes)
    print(len(primes))

count_primes(100)

#------------Task 3
#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4] ,'I':[4,1,1,1,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print_big('D')
