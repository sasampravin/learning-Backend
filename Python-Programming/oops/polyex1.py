class University:
    def getdata(self):
        self.uname='SKU'
        self.uloc='ATP'
    def dispdata(self):
        print('University name : %s'%self.uname)
        print('University location : %s'%self.uloc)
        print()
class College:
    def getdata(self):
        self.cname='ARTS'
        self.cloc="Atp Local"
    def dispdata(self):
        print('College name : %s'%self.cname)
        print('College location : %s'%self.cloc)
        print()
class Student(University,College):
    def getdata(self):
        University.getdata(self)
        College.getdata(self)
        self.sno=111
        self.sname='Gva'
        self.crs='German Lang'
    def dispdata(self):
        University.dispdata(self)
        College.dispdata(self)
        print('Student number : %d'%self.sno)
        print('Student name : %s'%self.sname)
        print('Student course : %s'%self.crs)

s=Student()
s.getdata()
s.dispdata()
