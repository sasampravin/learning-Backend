import aopmenu
def aop(a,b):
    aopmenu.menu()
    print("addition of {},{} is {}".format(a,b,a+b))
    print("subtraction of {},{} is {}".format(a,b,a-b))
    print("multiplication of {},{} is {}".format(a,b,a*b))
    print("division of {},{} is {}".format(a,b,a/b))
    print("floor division of {},{} is {}".format(a,b,a//b))
    print("modulo division of {},{} is {}".format(a,b,a%b))
    print("exponentiation of {},{} is {}".format(a,b,a**b))
    print("~"*40)
s=int(input("Enter first value="))
p=int(input("Enter second value="))
aop(s,p)
