import pickle
def readstdrec():
    try:
        with open("student.rec",'rb') as rp:
            print("-"*45)
            print("Sno\tSname\tMarks\tCollege")
            print("-"*45)
            while(True):
                try:
                    obj=pickle.load(rp)
                    for val in obj:
                        print("{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("-"*45)
                    break
    except FileNotFoundError:
        print("File does not exist")
readstdrec()
