
txt = 'without,hello,bag,world' # input()

li = list(txt.split(","))

li.sort()

listToStr = ' '.join(map(str, li))

print(listToStr)