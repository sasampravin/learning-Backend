import re
gd='python is an oop lang and python is also func programming lang'
sd='py'
match=re.search(sd,gd)
print('Given Data --->',gd)
if(match != None):
    print('"{}" value found and search is successful'.format(sd))
else:
    print('"{}" value not found search is unsuccessful'.format(sd))
