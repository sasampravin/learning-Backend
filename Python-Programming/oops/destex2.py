class getdata:
    def __init__(self,a=100,b=200):
        self.a=a
        self.b=b
        self.aop()
    def aop(self):
        print('addition :',self.a+self.b)
        print('subtraction :',self.b-self.a)
        print('multiplication :',self.a*self.b)
        print('division :',self.b/self.a)
    def __del__(self):
        print('\nGC calls Destructor\n')

print('program execution starts')
print()
print('aop of default values 100,200')
getdata()
print()
print('aop of 20,3\n')
getdata(20,3)
print()
print('aop of one default value and 333')
getdata(333)
