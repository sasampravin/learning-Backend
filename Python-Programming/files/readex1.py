try:
    with open("fruit.data","r") as rp:
        fdata=rp.read()
        print("-------filedata------")
        print(fdata)
        print("---------------------")
except FileNotFoundError:
    print("this file does not exists")
