#Oject orientated programing Inheritance and Polymorphism

########################   Inheritance   ######################
#Inheritance forms new classes using existing classes 

#Creating the base class
class Animal():
    
    def __init__(self):
        print("Animal Created")
        
    def who_am_i(self):
        print ("I am an animal")
        
    def eat(self):
        print("I am eating")

#Test Animal class
#myanimal = Animal()
#myanimal.eat()
#myanimal.who_am_i()
        
#################################################################
#Creating a new class that inherits the animal class 

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
        
    #Over righting the who am i method from the base class Animal
    def who_am_i(self):
        print("I am a dog")
    #Adding methods 
    def bark(self):
        print("Woof!!")

#Test Dog class with animal class inherited.         
my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()
#################################################################

########################   Polymorphism   ######################
#Refers to when 2 differnt classes share the same method name (speak)

class Dog2 ():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says Woof!!"
    
class Cat2 ():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says meaw!!"
    
niko=Dog2("Nico")
felix = Cat2("Felix")

#Testing Polymorphism classes individually 
print(niko.speak())
print(felix.speak())

#Demonstrating polymorphism using a for loop 

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())
    
#Demonstrating polymorphism using a Function
    
def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)

######################   Polymorphism using abstract classes and inheritance   ##################

class Animal3():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog3(Animal3):
    def speak(self):
        return self.name + " says woof!!"
    
class Cat3(Animal3):
    def speak(self):
        return self.name + " says meaw!!"
    
fido=Dog3("Fido")
isis=Cat3("Isis")
print(fido.speak())
print(isis.speak())   