class student:
    def addinfo(self):
        self.no=int(input("Enter student no: "))
        self.name=input('Enter student name: ')
        self.marks=float(input('Enter student marks: '))

s1=student()
s2=student()
print('content of s1 obj before:',s1.__dict__)
print('id of s1:',id(s1))
s1.addinfo()
print('content of s1 obj after:',s1.__dict__)
print('id of s1:',id(s1))
print('\ncontent of s2 obj before:',s2.__dict__)
print('id of s2:',id(s2))
s2.addinfo()
print('content of s2 obj after:',s2.__dict__)
print('id of s2:',id(s2))

                          
