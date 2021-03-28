txt = "Hello world!"  # input()

l = 0
u = 0
for i in txt:
    if(i.islower() == True):
        l += 1
    elif(i.isupper() == True):
        u += 1
print(f'UPPER CASE {u} LOWER CASE {l}')