txt = '1,2,3,4,5,6,7,8,9'   # input()

li = list(txt.split(","))
new_list = list(filter(lambda x: int(x)%2 == 1, li))
new_list = ",".join(new_list)

print(new_list)