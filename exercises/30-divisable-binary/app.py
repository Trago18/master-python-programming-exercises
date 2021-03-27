
txt = '0100,0011,1010,1001' # input()

li = txt.split(",")
li = list(map(lambda b: int(b,2), li))
li = list(filter(lambda x: x%5 == 0, li))
li = list(map(lambda n: bin(n).replace("0b", ""), li))
listToStr = ','.join(map(str, li))

print(listToStr)