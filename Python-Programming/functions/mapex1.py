sno=[10,20,30,40]
print('enter names of the students seperated with space')
nl=[val for val in input().split()]
print('enter marks of the student seperate with space')
ml=[int(val) for val in input().split()]
hike=list(map(lambda a: a+a*0.1,ml))
print('-'*30)
print('S.No\tName\tMarks\tHike')
print('-'*30)
for n,nm,m,h in zip(sno,nl,ml,hike):
    print('{}\t{}\t{}\t{}'.format(n,nm,m,h))
    
