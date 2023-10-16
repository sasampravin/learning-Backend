import aopmenu
aopmenu.menu()
ch=int(input("enter your choice:"))
match(ch):
    case 1:
        a=int(input("enter first value="))
        b=int(input("enter second value="))
        print("addition of {},{} is {}".format(a,b,a+b))
    case 2:
        a=int(input("enter first value="))
        b=int(input("enter second value="))
        print("subtraction of {},{} is {}".format(a,b,a-b))
    case 3:
        a=int(input("enter first value="))
        b=int(input("enter second value="))
        print("multiplication of {},{} is {}".format(a,b,a*b))
    case 4:
        a=int(input("enter first value="))
        b=int(input("enter second value="))
        print("division of {},{} is {}".format(a,b,a/b))
    case 5:
        a=int(input("enter first value="))
        b=int(input("enter second value="))
        print("floor division of {},{} is {}".format(a,b,a//b))
    case 6:
        a=int(input("enter first value="))
        b=int(input("enter second value="))
        print("modulo division of {},{} is {}".format(a,b,a%b))
    case 7:
        a=int(input("enter first value="))
        b=int(input("enter second value="))
        print("exponentiation of {},{} is {}".format(a,b,a**b))
    case _:
        print("your enter wrong operation")
        
