import os
try:
    os.removedirs("D:\India\AP")
    print("Folders removed successfully")
except OSError:
    print("folder is not empty")
except FileNotFoundError:
    print("No such folders available")
    
