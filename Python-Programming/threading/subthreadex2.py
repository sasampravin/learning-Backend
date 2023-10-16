import threading,time
def multable(n):
    if n<=0:
        print("{} is invalid input.".format(n))
    else:
        print('-'*30)
        print("\nmultiplication table for : {}".format(n))
        print('\nname of the thread execute multable is : {}'.format(threading.current_thread().name))
        print('-'*30)
        print('\nno.of threads active in this program is : {}'.format(threading.active_count()))
        
        for i in range(1,11):
            print("{}x{}={}".format(n,i,n*i))
        print('-'*30)
print('program execution starts')
print('\ndefaul thread name in every program : {}'.format(threading.current_thread().name))
print('\nno.of threads in active : {}'.format(threading.active_count()))
t1=threading.Thread(target=multable,args=(9,))
print('\nis sub thread alive before start : {}'.format(t1.is_alive()))
t1.start()
t1.name='SPK Thread'
print('\nis sub thread alive after start : {}'.format(t1.is_alive()))
print('\nno.of threads active now : {}'.format(threading.active_count()))
t1.join()
print('\nis sub thread alive after join : {}'.format(t1.is_alive()))
print('\nno.of threads active now : {}'.format(threading.active_count()))
print('\nprogram execution ended')
