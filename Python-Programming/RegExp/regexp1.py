import re
gd = 'welcome to python programming with pravin'
sd = 'th'
match = re.finditer(sd, gd)
print('type of match=', type(match))
print('content of match=', match)
print('type of records in the match object')
for me in match:
    print(type(me))
