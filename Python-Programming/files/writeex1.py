try:
    with open("addr1.data","a+") as sp:
        sp.write("jeeva\n")
        sp.write("david\n")
        sp.write("prabhavathi\n")
        print("data written to the file successfully")
except FileNotFoundError:
    print("this file does not exists")
