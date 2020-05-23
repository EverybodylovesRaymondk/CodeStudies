#Timeit module video 93
#This module will give you a time in seconds that python takes go execute some function.
import timeit

#e,g. we want to find out how long it will take to  create the string '0-1-2-....99' ten thousand times.
x=timeit.timeit('"-".join(str(n) for n in range (100))',number = 10000)
print(x)