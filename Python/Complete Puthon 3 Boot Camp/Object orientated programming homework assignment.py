#Object orientated programming homework assignment
#Importing math will allow you to use math.pi to get the entire pi value instead of having to set it in a class to 3.14
import math

class Line:
    
    def __init__(self, coord1,coord2):
        self.coord1=coord1
        self.coord2=coord2
        
    def distance(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        d = round((math.sqrt(((x2-x1)**2 + (y2-y1)**2))),2)
        return d
    
    def slope(self):
        x1,y1 = self.coord1
        x2,y2 = self.coord2
        m=round((((y2-y1)/(x2-x1))),2)
        return m

#Test line
myL=Line((3,2),(8,10))
print(myL.distance())
print(myL.slope())
        

class Cylinder:
            
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        vol = round(( math.pi * ((self.radius)**2) * self.height),2)
        return vol
    
    def SurfaceArea(self):
        SurfA = round(((2*(math.pi)*(self.radius)*(self.height)) + (2*(math.pi)*((self.radius)**2))),2)
        return SurfA
    
#Testing Cylinder Class
myS=Cylinder(2,3)
print(myS.volume())
print(myS.SurfaceArea())