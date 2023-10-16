def intro(*s):
    for val in s:
        print("{}".format(val),end="\t")
    print()
    print("~"*50)
print("~"*50)
intro(10)
intro(10,20)
intro(10,20,30)
intro(10,20,30,40)
intro(10,20,30,40,50)
