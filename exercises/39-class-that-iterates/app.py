def generator(limit):
    num=0
    while num<limit:
        num+=1
        if num%7==0:
            yield num

x=generator(100)

for i in x:
    print(i)
