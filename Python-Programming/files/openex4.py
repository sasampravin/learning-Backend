try:
    fp=open("student.data","x")
except FileNotFoundError:
    print("file does not exit")
else:
    print("File opened in read mode(default mode) successfully")
    print("type of the file :",type(fp))
    print("name of the file :",fp.name)
    print("file opening mmode :",fp.mode)
    print("is student.data file readable :",fp.readable())
    print("is student.data file writable :",fp.writable())
    print("is student .data file closed :",fp.closed)
finally:
    print("we are at finally block:")
    fp.close()
    print("is student.data file closed :",fp.closed)
