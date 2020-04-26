#My Program

#Calling code from myModule.py

from myModule import my_func

my_func()

#Importing a specific module  from a package 
from MyMainPackage import some_main_script

#Test of some_main_script main package
some_main_script.report_main()


#Importing a specific module  from a sub package 
from MyMainPackage.SubPackage import MySubScript

#Test of MySubScript from sub package
MySubScript.sub_report()