class account:
    def __getdata(self): #Method encapsulation
        self.a=213
        self.v=443
        self.c=323
        print('value of a :',self.a)
        print('value of v :',self.v)
        print('value of c :',self.c)

account().getdata()

#AttributeError: 'account' object has no attribute 'getdata'
