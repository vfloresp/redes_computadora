#!/usr/bin/env python3

import socket

data = ''
HOST = '10.3.72.5'  # The server's hostname or IP address
PORT = 6001        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    try:
        data = s.recv(1024)
    except socket.error as ex:
        print(ex)

print('Received', repr(data))