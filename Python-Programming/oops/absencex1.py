class account:
    def __init__(self):
        self.__acno=38274922947534
        self.name='Ranga'
        self.age=48
        self.__pin=43945
        self.branch='StuvertPuram'
        self.pincode=495395
        self.__bal=43,45,560
        self.bname='Turturee'
        self.getdata()
    def getdata(self):
        print('Bank name :',self.bname)
        print('Branch name :',self.branch)
        print('Account Holder name :',self.name)
        print('AH age :',self.age)
        # print('Account number :',self.acno) -->AttributeError: 'account' object has no attribute 'acno'
        #print('PIN Number :',self.pin) -->AttributeError: 'account' object has no attribute 'pin'
        #print('Bank balance :',self.bal) -->AttributeError: 'account' object has no attribute 'bal'
        print('Bank pincode :',self.pincode)

account()
