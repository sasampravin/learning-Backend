import os
try:
    os.rename("D:\html","D:\html5")
    print("folder renamed successfully")
except FileNotFoundError:
    print("No such folders available")
