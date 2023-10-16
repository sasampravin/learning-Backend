class sample:
    def __init__(slef,c):
        print('\nsample class')
        print('original val of c is %d'%c)
        print('square of c is %d'%c**2)
        print('cube of c is %d'%c**3)
class test(sample):
    def __init__(self,b):
        print('\ntest class')
        print('original val of b %d'%b)
        print('square of b is %d'%b**2)
        print('cube of b is %d'%b**3)
        print()
        super().__init__(4)
class last(test):
    def __init__(self,a):
        print('last class')
        print('original val of a is %d'%a)
        print('square of a is %d'%a**2)
        print('cube of a is %d'%a**3)
        super().__init__(2)

l=last(6)
