class getdata:
    def __init__(self,a=200,b=500):
        self.a=a
        self.b=b
        self.disp()
    def disp(self):
        print('value of a :',self.a)
        print('value of b :',self.b)
    def __del__(self):
        print('gc calls dc')

print('program starts')
print('\nFirst data')
f=getdata()
s=f
print('second data',s.__dict__)
t=s
print('third data',t.__dict__)
del f
s=None
del t
