import threading,time
def square(l):
    for i in l:
        print('thread name:{}--->square({}):{}'.format(threading.current_thread().name,i,i**2))
        time.sleep(1)
def cube(l):
    for i in l:
        print('thread name"{}--->cube({}):{}'.format(threading.current_thread().name,i,i**3))
        time.sleep(1)
bt=time.time()
l=[2,34,-9,-12,14,7]
print('name of the thread in main program is :',threading.current_thread().name)
t1=threading.Thread(target=square,args=(l,))
t2=threading.Thread(target=cube,args=(l,))
print('no.of threads before sub-threads:',threading.active_count())
t1.start()
t2.start()
print('no.of threads after sub-threads:',threading.active_count())
t1.join()
t2.join()
et=time.time()
print('number of threads after sub-threads execution:',threading.active_count())
print('total execution time : {}'.format(et-bt))
