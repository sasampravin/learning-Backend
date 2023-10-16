print('pattern 1\n:')
n=6
sp=0
start=5
for i in range(n):
    for i in range(sp):
        print(' ',end=' ')
    for j in range(start):
        print('@',end=' ')
    start-=1
    sp+=1
    print()
print('pattern 2\n')
n=6
space=0
m=1
for i in range(n):
    for j in range(space):
        print(' ',end=' ')
    for k in range(m):
        print('@',end=' ')
    m+=1
    print()
print('pattern 3\n')
n=6
sp=-1
start=1
dummy=1
for i in range(n):
    for i in range(sp):
        print(' ',end=' ')
    for j in range(start):
        print(dummy,end=' ')
    start+=1
    dummy+=1
    sp-=1
    print()
