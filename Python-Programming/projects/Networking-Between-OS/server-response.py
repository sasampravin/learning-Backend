import socket
s=socket.socket()
s.bind(("localhost",9876))
s.listen(3)
print('Server Side Program is ready to chat')
print('-'*40)
while True:
    cs, ca = s.accept()
    print(f'New client connected: {ca}')
    
    while True:
        csdata = cs.recv(1024).decode()
        
        if not csdata:
            print(f'Client {ca} disconnected')
            break
        
        print(f'client--->{csdata}')
        sdata = input('server--->')
        cs.send(sdata.encode())
        
    cs.close()
