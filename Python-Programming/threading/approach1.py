import threading,time
def table(n):
    print('Name of the thread executing table() function is : ',threading.current_thread().name)
    if n<=0:
        print('{} is invalid input for the table '.format(n))
    else:
        print('-'*35)
        print('multiplication table for {} '.format(n))
        print('-'*35)
        for i in range(1,11):
            print('{}x{}={}'.format(n,i,n*i))
            time.sleep(1)
        else:
            print('-'*35)

print('main programming starts here')
print('\ndefault thread name for the every program is : ',threading.current_thread().name)
print('\ninitially number of threads in active before start() : ',threading.active_count(),threading.current_thread().name)
t1=threading.Thread(target=table,args=(17,))
t1.start()
print('\nnumber of threads active after t1-thread starts : ',threading.active_count())
print('\nis thread t1 alive now after start : ',t1.is_alive())
t1.join()
print('\nafter t1 join no.of threads in active now : ',threading.active_count())
print('\nis thread t1 alive now after join : ',t1.is_alive())
print('\nprogram ends')
