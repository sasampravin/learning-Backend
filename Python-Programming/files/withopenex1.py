try:
    with open("student.data","a+") as fp:
        print("we are inside of the with open() as :")
        print("file opened in a+ mode successfully:")
        print("file name :",fp.name)
        print("file mode :",fp.mode)
        print("file type :",type(fp))
        print("is student.data file readable :",fp.readable())
        print("is student.data file writable :",fp.writable())
        print("is student.data fileclosed :",fp.closed)
    print("\nout of with open() as:")
    print("without using fp.close()")
    print("is student.data file closed :",fp.closed)
except FileNotFoundError:
    print("file does not exists")
