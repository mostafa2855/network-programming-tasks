from socket import * 

try: 
    s = socket(AF_INET, SOCK_STREAM)
    host = '127.0.0.1'
    port = 3000
    s.bind((host, port))
    s.listen(5)
    
    conn, addr = s.accept()
    print("Connection from:", addr[0])
    
    while True:
        
        msg_len_str = conn.recv(4).decode('utf-8')
        if not msg_len_str:
            break
        
        try:
            msg_len = int(msg_len_str)
        except ValueError:
            print("Invalid message length received:", msg_len_str)
            continue

        msg = conn.recv(msg_len).decode('utf-8')
        print("Received:", msg)
    
    s.close()

except error as e: 
    print("Error:", e)

except KeyboardInterrupt:
    print("Server terminated by keyboard interrupt.")
