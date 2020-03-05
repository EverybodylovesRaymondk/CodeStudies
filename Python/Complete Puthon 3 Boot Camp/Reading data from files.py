#Reading the text fill from its location
#the file path must contain the \\ after each directory 
file = open("C:\\Users\\raymondk\\Desktop\\Study\\Python\\Complete Puthon 3 Boot Camp\\Note Books\\Complete-Python-3-Bootcamp-master\\00-Python Object and Data Structure Basics\\test.txt")

#Creating a variable with the file contents 
content=file.readlines()

##Printing an element by index number
print(content[1])

file.close()

#adding lines to the file 
with open("C:\\Users\\raymondk\\Desktop\\Study\\Python\\Complete Puthon 3 Boot Camp\\Note Books\\Complete-Python-3-Bootcamp-master\\00-Python Object and Data Structure Basics\\test.txt" , mode="w") as new_file:
    new_file.write("First line\nSecond Line\nThis is a new line")
    
#Using the "With" fuction allows python to open the file execute the code block after the ":" and then close the file. 
with open("C:\\Users\\raymondk\\Desktop\\Study\\Python\\Complete Puthon 3 Boot Camp\\Note Books\\Complete-Python-3-Bootcamp-master\\00-Python Object and Data Structure Basics\\test.txt") as new_file:
    new_content =new_file.readlines()
    print(new_content)
    
#Creating a new file and writing to it. If the file does not exist the python will create it. 
with open("C:\\Users\\raymondk\\Desktop\\Study\\Python\\Complete Puthon 3 Boot Camp\\Note Books\\Complete-Python-3-Bootcamp-master\\00-Python Object and Data Structure Basics\\Raymond's file.txt", mode="w") as f:
    f.write("I created this file just now!\nand its good\nSo good\nThis is a usefull link to more python practice problems : http://codingbat.com/python")