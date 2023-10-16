class student:
    @classmethod
    def courses(cls):
        cls.crs1='python'
        cls.crs2='flask'
    def addinfo(self):
        self.no=int(input('Enter student no:'))
        self.name=input('Enter student name:')
        self.marks=float(input('Enter student marks:'))
    def disp(self):
        print('student no:',self.no)
        print('student name:',self.name)
        print('student marks:',self.marks)
        self.courses()
        print('student course1:',self.crs1)
        print('student course2:',student.crs2)

s1=student()
s2=student()
s1.addinfo()
s1.disp()
print('-'*40)
s2.addinfo()
s2.disp()
