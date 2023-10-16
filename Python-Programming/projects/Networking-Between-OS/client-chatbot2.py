import socket,sys,time
while(True):
    try:
        s=socket.socket()
        s.connect(("localhost",9876))
        connected=True

        while connected:
            csdata=input('client--->')
            if(csdata.lower()=='bye'):
                s.send('By server, I have sone work'.encode())
                connected=False
            else:
                s.send(csdata.encode())
                sdata=s.recv(1024).decode()
                print('server--->{}'.format(sdata))
        s.colse()
        break
    except ConnectionRefusedError:
        print('ConnectionRefusedError: Could not connect to server. Retrying in 5 seconds...')
        time.sleep(3)
    except ConnectionResetError:
        print('ConnectionResetError: Lost connection to server. Retrying in 5 seconds...')
        s.close()
        time.sleep(3)
        