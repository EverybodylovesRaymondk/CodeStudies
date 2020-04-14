#Object orientated programing Video 60

#Creating a class or object
class Sample():
    pass

#Creating an instance of that Class
my_sample = Sample()

print(type(my_sample))

#Creating a class or object with atributes 

class Dog():
    #Creating Class object attributes
    #These attributes are the same for all instances of the class /  object. 
    species = "Mammal"
#The __init__ method provides atributes for the class dog. 
    def __init__(self,breed,name):
#Takes the argument breed from above and assigns it to the attribute .breed,Allowing you to call the function e.g dog.breed and get the argument value
        self.breed = breed
        self.name = name
# a self defined methond can be called but has to be executed using () e.g. my_dog.bark()
    def bark(self,number):
        '''
        Will have the dog bark its own name and an outside argument number
        '''
        print("Woof! My name is {} and the number is {}".format(self.name,number))

my_dog=Dog(breed='Lab',name='Sammy')

print(type(Dog))

print(my_dog.breed + " "+ my_dog.name )
my_dog.bark(15)

#Creating new class for Circle
class Circle():
    #Class object attribute
    pi = 3.14
    
    def __init__(self,raduis=1):
        self.raduis=raduis
    #Method to calculate the circumference 
    def get_circumference(self):
        return self.raduis * Circle.pi * 2 #a class object atribute can be called using the class name . atribute name convention
    
my_circle=Circle(30)
print(my_circle.pi)
print(my_circle.raduis)
print(my_circle.get_circumfrence())