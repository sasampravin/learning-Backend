def info(no,**n):
    print("No=",no)
    for k,v in n.items():
        print("{}---->{}".format(k,v))
    print()
    print("~"*40)
print("~"*40)
info(no=111,name='pavan',salary=25000,sub='chem')
info(no=222,name='ravi',salary=29000,sub='phy')
info(no=333,name='juli',emp='soft',desg='tl',salary=1.35)
info(no=444,name='lucky')
info(no=555,name='jan',desg='ceo')
info(no=666,name='jine',emp='sse',salary=2.9,desg='exse',company='global')
info(no=123,name='pravin',strain='trainee',emptype='soft',cpay=35000,loc='beng',exp='fresher',skill1='python',skill2='ds')
