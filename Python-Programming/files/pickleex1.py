import pickle
def emprec():
    nor=int(input("Enter how many records do you want:"))
    if(nor<=0):
        print("invalid number of records")
    else:
        with open("emp.data","ab") as fp:
            for i in range(1,nor+1):
                print("-"*40)
                print("Enter {} Record".format(i))
                print("-"*40)
                eno=int(input("Enter employee number:"))
                ename=input("Enter employee name:")
                sal=float(input("Enter employee salary:"))
                l=list()
                l.append(eno)
                l.append(ename)
                l.append(sal)
                pickle.dump(l,fp)
                print("-"*40)
                print("Employee record saved succefully")
emprec()
