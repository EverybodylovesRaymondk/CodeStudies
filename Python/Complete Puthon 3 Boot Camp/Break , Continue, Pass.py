# Break , Continue, Pass

x=[1,2,3]
# using the pass , this is used to just skip out of the for loop  
for items in x:
    pass
print ("end of script")

# using the continue 
my_string = "Sammy" 
for letter in my_string:
    if letter == "a":
        continue
    print(letter)
    
for letter in my_string:
    if letter == "a":
        break
    print(letter)

#Using break function in a while loop 
x = 0

while x<5:
    if x==2:
        break
    print(x)
    x=x+1