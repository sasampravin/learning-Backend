import re
gd='I would like to create one youtube channel with name python programming with pravin'
sd='it'
match=re.finditer(sd,gd)
print('type of match=',type(match))
print('content of match=',match)
print('records of search data in the given data is.....')
for me in match:
    print(me)
    
