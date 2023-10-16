import threading
def square(l):
    return print(l**2)
print('prog execution starts')
t1=threading.Thread(target=square,args=(3,))
t2=threading.Thread(target=square,args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
