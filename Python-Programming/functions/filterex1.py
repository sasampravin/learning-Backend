pval=lambda a:a>0
nval=lambda b:b<0
print("enter list of elements seperated with space")
l=[int(i) for i in input().split()]
prval=list(filter(pval,l))
nrval=list(filter(nval,l))
print("given elements=",l)
print('posite values : ',prval)
print('negative values : ',nrval)
