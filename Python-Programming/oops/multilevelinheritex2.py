class university:
    def univdata(self):
        self.uname=input("enter University name : ")
        self.uloc=input("enter University Location : ")
    def dispunivdata(self):
        print('-'*40)
        print('University Data ')
        print('-'*40)
        print('University name : ',self.uname)
        print('University location : ',self.uloc)
        print('-'*40)

class college(university):
    def coldata(self):
        self.cname=input('enter College name : ')
        self.cloc=input('enter College location : ')
        self.univdata()
    def dispcoldata(self):
        self.dispunivdata()
        print('-'*40)
        print('College details ')
        print('-'*40)
        print('College name : ',self.cname)
        print('College location : ',self.cloc)
        print('-'*40)

class student(college):
    def stddata(self):
        self.no=int(input('enter student number : '))
        self.name=input('enter student name : ')
        self.crs=input('enter student course : ')
        self.coldata()
    def dispstudent(self):
        self.dispcoldata()
        print('-'*40)
        print('Student details ')
        print('-'*40)
        print('Student number : ',self.no)
        print('Student name : ',self.name)
        print('Student course : ',self.crs)
        print('-'*40)

s=student()
s.stddata()
s.dispstudent()

        
