from functools import reduce as r
print('ente list of values separeted by space')
l=[int(i) for i in input().split()]

print('big value:',int(r(lambda s,b: b if b>s else s,l)))
print('small value:',int(r(lambda s,b: s if s<b else b,l)))
