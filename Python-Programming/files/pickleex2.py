import pickle
def stdrec():
    with open("student.rec","ab") as sp:
        while(True):
            try:
                print("-"*40)
                sno=int(input("Enter student number:"))
                sname=input("Enter student name:")
                marks=float(input("Enter stucent marks:"))
                clg=input("Enter student college")
                l=list()
                l.append(sno)
                l.append(sname)
                l.append(marks)
                l.append(clg)
                pickle.dump(l,sp)
                print("-"*40)
                print("Student record saved succefully")
                print("-"*40)
                ch=input("EDo you want to insert another record:(yes/no):")
                if(ch=='no'):
                    print("Thank you for using this programme")
                    break
                if(ch.lower() !='yes'):
                    print("please learn typing:")
            except ValueError:
                print("Don't enter str,symbles and alphanumerics for sno,marks")
                
                    
stdrec()                    
                      
