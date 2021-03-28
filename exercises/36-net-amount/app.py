txt = 'D 300 D 300 W 200 D 100'

total = 0
li = list(txt.split(" "))

i = 0
while i < len(li):
    if (li[i] == 'D'):
        total+=int(li[i+1])
    elif (li[i] == 'W'):
        total-=int(li[i+1])
    i+=1

print(total)