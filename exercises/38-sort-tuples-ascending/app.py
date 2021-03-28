from operator import itemgetter, attrgetter

t = []

s = 'Tom,19,80\nJohn,20,90\nJony,17,91\nJony,17,93\nJson,21,85'
s = list(s.split('\n'))
for i in s:
#while True:
    #s = input()

    t.append(tuple(i.split(',')))

print(sorted(t, key=itemgetter(0,1,2)))