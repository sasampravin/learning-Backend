import threading,time
def multable(n):
    if n<=0:
        print("{} is invalid input.".format(n))
    else:
        print('-'*30)
        print("multiplication table for : {}".format(n))
        print('\nname of the thread execute multable is : {}\n'.format(threading.current_thread().name))
        print('-'*30)
        for i in range(1,11):
            print("{}x{}={}".format(n,i,n*i))
        print('-'*30)
print('program execution starts')
print('\ndefaul thread name in every program : {}'.format(threading.current_thread().name))
print('\nno.of threads in active : {}\n'.format(threading.active_count()))
t1=threading.Thread(target=multable,args=(9,))
t2=threading.Thread(target=multable,args=(-19,))
t3=threading.Thread(target=multable,args=(17,))
print('\nis sub thread t1 alive before start : {}'.format(t1.is_alive()))
print('\nis sub thread t2 alive before start : {}'.format(t2.is_alive()))
print('\nis sub thread t3 alive before start : {}'.format(t3.is_alive()))
t1.start()
t2.start()
t3.start()
t1.name='SPK Thread'
t2.name='Gva Thread'
t3.name='PK Thread'
print('\nis sub thread t1 alive after start : {}'.format(t1.is_alive()))
print('\nis sub thread t2 alive after start : {}'.format(t2.is_alive()))
print('\nis sub thread t3 alive after start : {}\n'.format(t3.is_alive()))
print('\nno.of threads active now : {}\n'.format(threading.active_count()))
t1.join()
t2.join()
t3.join()
print('\nis sub thread t1 alive after join : {}'.format(t1.is_alive()))
print('\nis sub thread t2 alive after join : {}'.format(t2.is_alive()))
print('\nis sub thread t3 alive after join : {}'.format(t3.is_alive()))
print('\nno.of threads active now : {}'.format(threading.active_count()))
print('\nprogram execution ended')
