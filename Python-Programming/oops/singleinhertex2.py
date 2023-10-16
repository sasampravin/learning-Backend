class parent:
    def getdata(self):
        self.pname='Parent Name'
        self.gname='Grand patent'
        self.pro='Property'
        self.fame='Identity'
    def dispdata(self):
        self.getdata()
        print('parent name : ',self.pname)
        print('grand parent : ',self.gname)
        print('property : ',self.pro)
        print('identity : ',self.fame)

class child(parent):
    def holedata(self):
        self.cname='Child'
        self.gcname='Grand Child'
    def display(self):
        self.dispdata()
        print()
        print('child name : ',self.cname)
        print('grand child name : ',self.gcname)

c=child()
c.holedata()
c.display()
