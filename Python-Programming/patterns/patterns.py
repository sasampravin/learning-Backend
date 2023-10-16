print('pattern 1\n')
for i in range(1,6):
    for j in range(1,6):
        print(i,end=' ')
    print()
print()
print('pattern 2\n')
dummy=1
for i in range(1,6):
    for j in range(1,6):
        print(dummy,end=' ')
    print()
    dummy+=2
print()
print('pattern 3 \n')
for i in range(1,6):
    for j in range(1,6):
        print(j,end=' ')
    print()
print()
print('pattern 4\n')
for i in range(1,6):
    dummy=1
    for j in range(1,6):
        print(dummy,end=' ')
        dummy+=1
    print()
print()
print('pattern 5\n')
dummy=1
for i in range(1,6):
    for j in range(1,6):
        print(dummy,end='\t')
        dummy+=1
    print()
print()
print('pattern 6\n')
s=65
for i in range(1,6):
    for j in range(1,6):
        print(chr(s),end=' ')
    print()
    s+=1
print()
print('pattern 7\n')
for i in range(1,6):
    s=65
    for j in range(1,6):
        print(chr(s),end=' ')
        s+=1
    print()
print()
print('pattern 8\n')
s=65
for i in range(1,6):
    for j in range(1,6):
        print(chr(s),end=' ')
        s+=1
    print()
print()
print('pattern 9\n')
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('@',end=' ')
        else:
            print('^',end=' ')
    print()
print()
print('pattern 10\n')
n=5
sp=0
stars=1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for h in range(stars):
        print('*',end=' ')
    sp+=1
    print()
print()
print('pattern 10a\n')
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('$',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
print('pattern 10b\n')
n=6
sp=n-1
start=1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for m in range(start):
        print('@',end=' ')
    sp-=1    
    print()
print()
