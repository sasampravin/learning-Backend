class gatdata:
    def __init__(self,sno,name):
        self.sno=sno
        self.name=name
        self.disp()
    def disp(self):
        print('roll no {} student data\n'.format(self.sno))
        print('student no %d and name "%s"'%(self.sno,self.name))
    def __del__(self):
        print('GC Calls DC')
print('programme execution starts')
f=gatdata(20,'sada')
s=f
t=s
f=None
s=None
t=None
