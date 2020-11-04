##Panda playPython
#
#import pandas as pd
#import math
#
##print(pd.__version__)
##
##file=pd.DataFrame(pd.read_excel('PlayPython.xlsx'))
##print(file['X'][0])
#
#
#class BMI():
#
#    def calculate():
#        weight = float(input("What is your weight in Kg : "))
#        height = float(input("How tall are you in m : "))
#
#        bmi = round((weight / (math.pow(height,2))),1)
#
#        if bmi<18.5:
#            return "Underweight " + str(bmi)
#        elif bmi >=18.5 and bmi <25:
#            return "Normal weigh " + str(bmi)
#        elif bmi >= 25 and bmi < 30:
#            return "Overweight " +  str(bmi)
#        elif bmi > 30 :
#            return "Obese " + str(bmi)
#
#print(BMI.calculate())

import webbrowser
url = ['https://soundcloud.com/stream','https://www.youtube.com/watch?v=OH35NiBsqOs&list=RD5RHlrQGCuJQ&index=8&ab_channel=NewAgeWave']

for u in url :
    open_google = webbrowser.get('windows-default').open(u)