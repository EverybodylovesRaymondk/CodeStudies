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
