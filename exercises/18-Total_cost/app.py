#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):

    dollars = n*d
    cents = n*c
    dollars = dollars + cents//100
    cents = cents%100

    return dollars, cents


#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(10,15,2))
