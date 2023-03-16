# import socket

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('127.0.0.1', 9999))
# server_socket.listen(5)

# while True:
#     client, address = server_socket.accept()
#     print(f"Connection from {address} has been established!")
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect(('127.0.0.1', 9999))
#     client_socket.send(bytes("Hello World!", "utf-8"))
#     command = "ls -al"
#     client_socket.send(command.encode())


import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()