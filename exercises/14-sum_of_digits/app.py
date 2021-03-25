#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  return  num//100 + (num%100 - num%10)//10 + num%10

#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))