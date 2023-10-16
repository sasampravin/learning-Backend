import pickle
def reademprec():
    try:
        with open("emp.data",'rb') as rp:
            print("-"*35)
            print("Eno\tEname\tSalary")
            print("-"*35)
            while(True):
                try:
                    obj=pickle.load(rp)
                    for val in obj:
                        print("{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("-"*35)
                    break
    except FileNotFoundError:
        print("File does not exist")
reademprec()
