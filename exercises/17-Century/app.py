#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.

import math

def century(year):
    return  year//100 + math.ceil((year%100)/100)


#Invoke the function with any given year. 
print(century(2000))