#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
    
    first = num//10
    second = num%10
    return (str(second) + str(first))
    #return ((second*10) + first)

   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))

