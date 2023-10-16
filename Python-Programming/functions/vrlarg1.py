def info(no,*n):
    print("~"*40)
    print("No=",no)
    for v in n:
        print("{}".format(v),end="\t")
    print()
    print("~"*40)
info(111,'pavan',25000,'chem')
info(222,'ravi',29000,'phy')
info(333,'juli','soft','tl',1.35)
info(444,'lucky')
info(555,'jan','ceo')
info(666,'jine','sse',2.9,'exse','global')
info(123,'pravin','trainee','soft',35000,'beng','fresher','python','ds')
