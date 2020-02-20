#------------Working with strings index and slicing------------
newString="abcdefghijk"
#Returning a single character(The first Character) of the my_sting variable
print("Returning only the fitst character = " + newString[0])
#Returning the 8th character of the my_sting variable
print("Returning only the 8th chracter = " + newString[8])
#Returning the last letter of a string no matter what the length
print("Returning the last character of a string = " +newString[-1])
#Selecting a from a specific part of the string till the end
print("Returning all characters from index 2 till the end = " + newString[2:])
print("Returning all characters till index 3 = " + newString[:3])
print("Returning only a section of the string = " + newString[3:6])
print("Returning every second character in the entire string = " + newString[::2])
print("Returning every second character for a given section of the string = " + newString[2:7:2])
print("Returning the entire string in reverse = " + newString[::-1])