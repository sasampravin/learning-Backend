ftl=('kiwi','pinapple','dannimma')
with open("fruit.data","a") as fp:
    fp.writelines(str(ftl)+'\n')    
    print("data written to the file successfully")
