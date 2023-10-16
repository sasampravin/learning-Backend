i=range(int(input()))
s=list(map(lambda a:a**2,i))
c=list(map(lambda c:c**3,i))
print('Orig.no\t\tsquare\t\tcube')
print('-'*40)
for o,s,c in zip(i,s,c):
    print('{}\t\t{}\t\t{}'.format(o,s,c))

