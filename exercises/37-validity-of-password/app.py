import re

password = 'ABd1234@1,aF1#,2w3E*,2We3345'
li = list(password.split(','))
values = []

for i in li:
    if not (6 < len(i) < 12):
        continue
    if not (re.search('[a-z]',i)):
        continue
    if not (re.search('[A-Z]',i)):
        continue
    if not (re.search('[0-9]',i)):
        continue
    if not (re.search('[$#@]',i)):
        continue
    values.append(i)

values = ','.join(values)
print(values)