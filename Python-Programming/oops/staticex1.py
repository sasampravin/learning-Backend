class student:
    def addinfo(self):
        self.sno=int(input('Enter student no:'))
        self.name=input('Enter student name:')
        self.marks=float(input('Enter student marks:'))
        self.clg=input('Enter student college name:')

class employee:
    def addinfo(self):
        self.eno=int(input('Enter employee no:'))
        self.name=input('Enter employee name:')
        self.sal=float(input('Enter employee salary:'))
        self.comp=input('Enter employee company name:')

class teacher:
    def addinfo(self):
        self.tno=int(input('Enter teacher no:'))
        self.name=input('Enter teacher name:')
        self.sub=input('Enter teacher subject:')
        self.sal=float(input('Enter teacher salary:'))

class blr:
    @staticmethod
    def getdata(sp):
        for k,v in sp.__dict__.items():
            print('{}---->{}'.format(k,v))

s=student()
e=employee()
t=teacher()
s.addinfo()
e.addinfo()
t.addinfo()
print()
blr.getdata(s)
blr.getdata(e)
blr.getdata(t)

