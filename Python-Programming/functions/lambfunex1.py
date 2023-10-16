big=lambda a,b,c: "three are equal" if(a==b==c) else a if (a>b)and(a>c) else b if (b>a)and(b>c) else c
small=lambda a,b,c: "three are equal" if(a==b==c) else a if(a<b)and(a<c) else b if(b<a)and(b<c) else c

x,y,z=int(input("enter first value:")),int(input("enter second value:")),int(input("enter third value:"))
res=big(x,y,z)
sval=small(x,y,z)
print("big value of ({},{},{}) is :{}".format(x,y,z,res))
print("small value of ({},{},{}) is :{}".format(x,y,z,sval))

