class dispdata:
    def getdata(self):
        #self._a=123 -->AttributeError: 'dispdata' object has no attribute 'a'. Did you mean: '_a'?
        self.b=234
        self.__c=345
        self.___d=456
        self.____e=567
        #print('value of a :',self.a)
        print('value of b :',self.b)
        #print('value of c :',self._c) -->AttributeError: 'dispdata' object has no attribute '_c'
        print('value of c :',self.__c)
        #print('value of d :',self.__d) -->AttributeError: 'dispdata' object has no attribute '_dispdata__d'. Did you mean: '_dispdata___d'?
        #print('vlaue of e:',self.__e) -->AttributeError: 'dispdata' object has no attribute '_dispdata__e'. Did you mean: '_dispdata__c'?
dispdata().getdata()
