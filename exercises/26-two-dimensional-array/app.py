
def myFunction(x,y):
    d1 = []
    for i1 in range(x):
        d2 = []
        for i2 in range(y):
            d2.append(i1*i2)
        d1.append(d2)
    print(d1)

myFunction(3,5)