import socket
import threading

def broadcast_message(message, sender_socket):
    sender_alias = None
    for client_socket, client_alias in client_sockets:
        if client_socket == sender_socket:
            sender_alias = client_alias
            break
    for client_socket, client_alias in client_sockets:
        if client_socket != sender_socket:
            try:
                client_socket.send(f"{sender_alias}: {message}".encode())
            except:
                print("An error occurred while sending the message.")

def handle_client(client_socket, client_address):
     alias = client_socket.recv(1024).decode()
     client_sockets.append((client_socket, alias))
     print(f"Connected: {client_address} ({alias})")

     while True:
         try:
             data = client_socket.recv(1024).decode()
             broadcast_message(data, alias)
         except:
             print(f"Client disconnected: {client_address} ({alias})")
             client_socket.close()
             client_sockets.remove((client_socket, alias))
             break

# Server configuration
host = '127.0.0.1'
port = 7002

#Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print("Server listening on {}:{}".format(host, port))

#Store client sockets and aliases
client_sockets = []

def accept_connections():
     while True:
         client_socket, client_address = server_socket.accept()
         client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
         client_thread.start()

# Start accepting connections
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()

# Wait for the accept thread to complete
accept_thread.join()

#Close the socket when done
server_socket.close()
