def aop():
    while True:
        def Disp_menu():
            print('-'*35)
            print('ARITHMETIC OPERATION MENU')
            print('-'*35)
            print('1. Addition Operation ')
            print('2. Subtraction Operation')
            print('3. Multiplication Operation')
            print('4. Division Operation')
            print('5. Floor_division Operation')
            print('6. Modulo_division Operation')
            print('7. Exponentiation Operation')
            print('-'*35)
        Disp_menu()
        try:
            ch=int(input('Enter your choice of ARITHMETIC OPERATION : '))
            match(ch):
                case 1:
                    try:
                        a = float(input('Enter value for a : '))
                        b = float(input('Enter value for b : '))
                        print('Addition of values %d,%d is %d'%(a,b,a+b))
                    except ValueError:
                        print("Don't enter str, alphanumerics and symbles for values of a,b")
                case 2:
                    try:
                        a = float(input('Enter value for a : '))
                        b = float(input('Enter value for b : '))
                        print('Subtraction of values %d,%d is %d' % (a, b, a - b))
                    except ValueError:
                        print("Don't enter str, alphanumerics and symbles for values of a,b")
                case 3:
                    try:
                        a = float(input('Enter value for a : '))
                        b = float(input('Enter value for b : '))
                        print('Multiplication of values %d,%d is %d' % (a, b, a * b))
                    except ValueError:
                        print("Don't enter str, alphanumerics and symbles for values of a,b")
                case 4:
                    try:
                        a = float(input('Enter value for a : '))
                        b = float(input('Enter value for b : '))
                        print('Division of values %d,%d is %d' % (a, b, a / b))
                    except ValueError:
                        print("Don't enter str, alphanumerics and symbles for values of a,b")
                case 5:
                    try:
                        a = float(input('Enter value for a : '))
                        b = float(input('Enter value for b : '))
                        print('Floor_division of values %d,%d is %d' % (a, b, a // b))
                    except ValueError:
                        print("Don't enter str, alphanumerics and symbles for values of a,b")
                case 6:
                    try:
                        a = float(input('Enter value for a : '))
                        b = float(input('Enter value for b : '))
                        print('Modulo_division of values %d,%d is %d' % (a, b, a % b))
                    except ValueError:
                        print("Don't enter str, alphanumerics and symbles for values of a,b")
                case 7:
                    try:
                        a = int(input('Enter value for a : '))
                        b = int(input('Enter value for b : '))
                        print('Subtraction of values %d,%d is %d' % (a, b, a ** b))
                    except ValueError:
                        print("Don't enter str, alphanumerics, float and symbles for values of a,b")
                case _:
                    print("Don't enter beyond choice of Operations")
        except ValueError:
            print("Don't enter str, symbles, alphanumerics and float point values for choice")

aop()