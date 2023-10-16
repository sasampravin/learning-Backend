class student():
    def __init__(self,no,name):
        self.no=no
        self.name=name
        print('student number is {} and name is {}'.format(self.no,self.name))
    def __del__(self):
        print('garbage collector call destructor')

print('program execution starts')
print()
print('content of first student :')
s=student(11,'samsong')
print()
s=None
print()
print('content of second student :')
s2=student(22,'gelexy')
print()
del s2
print()
print('content of third student :')
s3=student(33,'nokia')
print()
print('program execution ends')
