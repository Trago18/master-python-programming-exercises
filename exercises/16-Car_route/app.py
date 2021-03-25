#Complete the function to return the amount of days it will take to cover a route.
#HINT: You may need to import the math module for this exercise.

import math

def car_route(n,m):
    return 1+m//n


#Invoke the function with two intergers.
print(car_route(200,1000))