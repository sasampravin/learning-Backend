class student:
    crs1='python'
    crs2='django'
    def addinfo(self):
        self.no=int(input('sno:'))
        self.name=input('name:')
        self.marks=float(input('marks:'))
    def disp(self):
        print('student no:',self.no)
        print('student name:',self.name)
        print('student marks:',self.marks)
        print('student course1:',student.crs1)
        print('student course2:',student.crs2)

s1=student()
s2=student()
print('s1 content before:',s1.__dict__)
s1.addinfo()
print('s1 content after:',s1.__dict__)
s1.disp()
print('\ns2 content before:',s2.__dict__)
s2.addinfo()
print('s2 content after:',s2.__dict__)
s2.disp()

