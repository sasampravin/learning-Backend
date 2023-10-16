try:
    with open("addr1.data","r") as rp:
        print("reading the data in the file with readline \n")
        print(rp.readline(),"\n")
        print(rp.readline(),"\n")
        print(rp.readline(),"\n")
        print(rp.readline(),"\n")
        print(rp.read())
except FileNotFoundError:
    print("this file does not exist")
        
