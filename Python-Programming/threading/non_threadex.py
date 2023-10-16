import time,threading
def square(l):
    for i in l:
        print('Thread name : {} ---> square({})={}'.format(threading.current_thread().name,i,i**2))
        time.sleep(1)
def cube(l):
    for j in l:
        print('Thread name : {} ---> cube({})={}'.format(threading.current_thread().name,j,j**3))
        time.sleep(1)
print('program execution started')
bt=time.time()
l=[-2,12,5,3,9,-7,-6]
print('Name of the thread executing main program is ---> ',threading.current_thread().name)
square(l)
cube(l)
et=time.time()
print('no.of threads executing non_thread program is ---> ',threading.active_count())
print('total execution time is ---> ',et-bt)
