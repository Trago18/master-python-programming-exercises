txt = "hello world! 123"  # input()

l = 0
d = 0
for i in txt:
    if(i.isalpha() == True):
        l += 1
    elif(i.isdecimal() == True):
        d += 1
print(f'LETTERS {l} DIGITS {d}')