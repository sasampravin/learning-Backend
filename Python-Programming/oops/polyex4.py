class table2:
    def _2table(self):
        self.a=2
        for i in range(1,11):
            print('{}x{}={}'.format(self.a,i,self.a*i))
        print()
class table3:
    def _3table(slef):
        for i in range(1,11):
            print('3x{}={}'.format(i,i*3))
        print()
class table4:
    def _4table(self):
        for i in range(1,11):
            print('4x{}={}'.format(i,i*4))
        print()
class alltables(table2,table3,table4):
    def disp(self):
        print('displaying all the tables\n')
        table2._2table(self)
        table3._3table(self)
        table4._4table(self)

a=alltables()
a.disp()
