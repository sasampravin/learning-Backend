class Univ:
    def univdata(self):
        self.uname='SKU'
        self.uloc='ATP'
    def dispunivdata(self):
        print('University name : ',self.uname)
        print('University location : ',self.uloc)
        print()
class College(Univ):
    def coldata(self):
        self.cname='arts'
        self.cloc='atp'
        self.univdata()
    def dispcoldata(self):
        self.dispunivdata()
        print('college name : ',self.cname)
        print('college location : ',self.cloc)
        print()
class Student(College):
    def stdata(self):
        self.sno=20
        self.sname='guru'
        self.crs='maths'
        self.coldata()
    def stdispdata(self):
        self.dispcoldata()
        print('student number : ',self.sno)
        print('student name : ',self.sname)
        print('student course : ',self.crs)

s=Student()
s.stdata()
s.stdispdata()

        
