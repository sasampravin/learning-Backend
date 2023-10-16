import os
try:
    os.rmdir("D:\India\AP\KNL")
    print("Folder removed successfully")
except OSError:
    print("This folder is not empty")
except FileNotFoundError:
    print("No folder exists in this name")
