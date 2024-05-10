from socket import * 

try: 
    s = socket(AF_INET,SOCK_STREAM)
    host='127.0.0.1'
    port=3000
    s.connect((host,port))
    
    while True:
        s.send(input("Client :").encode())
        msg_len = s.recv(4).decode('utf-8')  
        if not msg_len:
            break
        msg_len = int(msg_len)
        msg = s.recv(msg_len).decode('utf-8')
        print("Received:", msg)
        
    s.close()
except error as e : 
    print(e)
except KeyboardInterrupt:
    print("ok")     
           