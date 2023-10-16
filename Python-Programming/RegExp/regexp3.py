import re
gd='welcome to python programming with pravin, python is an oop language and python is also functional programming language'
sd='on'
mat=re.finditer(sd,gd)
print('match entries in the match object')
noc=0
for me in mat:
    print('start index:{} end index:{} and value:{}'.format(me.start(),me.end(),me.group()))
    noc=noc+1
print('number of occurence of the word "{}" is --->'.format(sd),noc)
