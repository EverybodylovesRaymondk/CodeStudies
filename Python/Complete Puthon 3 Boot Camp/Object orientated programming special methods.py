#Object orientated programming special methods
#Allows the use of existing functions within a custom class e.g. len or str 

class Book():
    
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages
        
    #The __str__ method defines what will be returned when print is called on a instance of the book class
    def __str__(self):
        return "Title:{} \nAuthor:{}".format(self.name,self.author)
    
    #The __len__ method defines what will be retruned if the len function is called on a instance of the book class
    def __len__(self):
        return self.pages
    
    #The __del__ method will difine what happens when a instance of the book class is deleted
    def __del__(self):
        print("A book instance has been deleted")
    

b=Book('Raymond','Kriel',200)
print(b)
print(len(b))
del(b)