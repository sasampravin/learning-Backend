import os
try:
    os.makedirs("D:\India\AP\KNL\PNTR")
    print("FOlders created successfully")
except FileExistsError:
    print("This folder already exists")
except FileNotFoundError:
    print("We con't create folders")
