
txt = 'hello world and practice makes perfect and hello world again' # input()

li = txt.split(" ")
li.sort()

for i in li:
    if (li.count(i) == 2):
        li.remove(i)

listToStr = ' '.join(map(str, li))

print(listToStr)