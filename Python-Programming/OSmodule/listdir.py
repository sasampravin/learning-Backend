import os
try:
    fileslist=os.listdir("D:\ppp")
    print('-'*30)
    print("file names")
    print('-'*30)
    for file in fileslist:
        print("{}".format(file))
    else:
        print('-'*30)
        print("no.of files:{}".format(len(fileslist)))

except FileNotFoundError:
    print("no such files available")
except OSError as e:
    print("dirError:",e)
