a=10
b=20
c=30
d=40
def add():
    a=100
    b=200
    c=300
    d=400
    res=a+b+c+d+globals()['a']+globals().get('b')+globals()['c']+globals().get('d')
    print('result=',res)

add()
