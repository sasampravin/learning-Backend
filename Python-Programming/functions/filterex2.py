print("enter values seperate with space")
l=[int(val) for val in input().split()]
elist=list(filter(lambda a: a%2==0,l))
olist=list(filter(lambda a: a%2!=0,l))
print("even list=",elist)
print("odd list=",olist)
