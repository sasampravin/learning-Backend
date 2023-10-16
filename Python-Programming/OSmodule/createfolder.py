import os
try:
    os.mkdir('D:\India')
    print('Folder created successfully')
except FileExistsError:
    print("This FOlder already Exists")
except FileNotFoundError:
    print("we can't created root or sub or sub-sub folders")

