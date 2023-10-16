class aop:
    def __init__(self):
        self.a=100
        self.b=2
        self.c=self.a+self.b
        self.d=self.a-self.b
        self.e=self.a*self.b
        self.f=self.a/self.b
        self.g=self.a//self.b
        self.h=self.a%self.b
        self.i=self.a**self.b
        print('AOP on two values(100,2)')
        print('-'*25)
        print('addition :',self.c)
        print('subtraction :',self.d)
        print('multiplication :',self.e)
        print('division :',self.f)
        print('floor-division :',self.g)
        print('modulo division :',self.h)
        print('exponentiation :',self.i)

aop()
