import sys

class DepositError(Exception): pass
class WithdrawError(Exception): pass
class InsuffundError(Exception): pass

bal = 500
def atmprojrun():
    attempts = 1
    while True:
        passwd = input("Enter your password:")
        if passwd == "python":
            def atmproject():
                while True:
                    def menu():
                        print("_" * 50)
                        print("\tATM Operations")
                        print("-" * 50)
                        print("\t1.Deposit")
                        print("\t2.Withdraw")
                        print("\t3.Balance Enq")
                        print("\t4.Exit")
                        print("~" * 50)
                    menu()
                    try:
                        ch = int(input("Enter your choice of operation:"))
                        match ch:
                            case 1:
                                try:
                                    def deposit():
                                        damt = float(input("Enter the Deposit amount:"))
                                        if damt <= 0:
                                            raise DepositError
                                        else:
                                            global bal
                                            bal = bal + damt
                                            print("Your account xxxxxx789 credited with INR:{}".format(damt))
                                            print("Your current Balance :{}".format(bal))
                                    deposit()
                                except ValueError:
                                    print("Don't enter str,symbols and alphanumerics for deposit")
                                except DepositError:
                                    print("Don't enter zer0 or negative amount for deposit")
                            case 2:
                                try:
                                    def withdraw():
                                        global bal
                                        wamt = float(input("Enter Withdraw amount :"))
                                        if wamt <= 0:
                                            raise WithdrawError
                                        elif (wamt + 500) > bal:
                                            raise InsuffundError
                                        else:
                                            bal = bal - wamt
                                            print("Your account xxxxxx789 deposited with INR :{}".format(wamt))
                                            print("Your current Balance :{}".format(bal))
                                    withdraw()
                                except ValueError:
                                    print("Don't enter str,symbols and alphanumerics for withdraw")
                                except InsuffundError:
                                    print("Your account does not have funds")
                                except WithdrawError:
                                    print("Don't enter zero or negative amount for withdraw")
                            case 3:
                                def balenq():
                                    print("Your account balance :{}".format(bal))

                                balenq()
                            case 4:
                                print("Thanks for using this program")
                                sys.exit()
                            case _:
                                print("Your selection of operation is wrong try another")
                    except ValueError:
                        print("Don't enter str,symbols and alphanumerics for choice")
            atmproject()
        else:
            if attempts == 3:
                print("Hello dear customer,I think You are wrong person")
                sys.exit()
        attempts = attempts + 1
atmprojrun()



