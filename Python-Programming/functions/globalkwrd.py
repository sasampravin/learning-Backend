a=100
b=200
c=300
d=400
def operations():
    """this program written by spkumar"""
    obj=globals()
    for gvn,gvv in obj.items():
        print('\t{}---->{}'.format(gvn,gvv))

    print("\n Programmer defined global variables ")
    print('val of a=',obj['a'])
    print('val of b=',obj['b'])
    print('val of c=',obj['c'])
    print('val of d=',obj['d'])

    print("\n Programmer defined global variables ")
    print('val of a=',obj.get('a'))
    print('val of b=',obj.get('b'))
    print('val of c=',obj.get('c'))
    print('val of d=',obj.get('d'))

    print("\n Programmer defined global vatiables")
    print('val of a=',globals()['a'])
    print('val of b=',globals()['b'])
    print('val of c=',globals()['c'])
    print('val of d=',globals()['d'])

    print("\n Programmer defined global variables")
    print('val of a=',globals().get('a'))
    print('val of b=',globals().get('b'))
    print('val of c=',globals().get('c'))
    print('val of d=',globals().get('d'))

    values=list(globals().values())
    print('\nval of a=',values[-5])
    print('val of b=',values[-4])
    print('val of c=',values[-3])
    print('val of d=',values[-2])

#main program
operations()
