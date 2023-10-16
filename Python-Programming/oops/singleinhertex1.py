class parent:
    def __init__(self):
        self.sname='SurName'
        self.fame="Identity"
        self.pro='Properti'
    def disp(self):
        print('surname of parents : ',self.sname)
        print('identity of the parentant : ',self.fame)
        print('propertu of the parent : ',self.pro)
class child(parent):
    def getdata(self):
        self.name='Ninja'
        self.room='single'
        self.disp()
    def display(self):
        print('\nname of the chiod :',self.name)
        print('room of the chiled :',self.room)
c=child()
c.getdata()
c.display()
