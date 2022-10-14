import socket
import logging
from ident import *

logging.basicConfig(filename="server.log", format='%(asctime)s %(message)s', level=logging.INFO)
port = 9090

while True:
    sock = socket.socket()
    res=1

    while True:
        res = sock.connect_ex(("127.0.0.1", port))
        if res != 0:
            break
        port += 1
    
    sock.bind(('', port)) 
    sock.listen(1)
    print(f"Server has started, listens port {port}")
    logging.info(f"Server has started, listens port {port}")
    
    conn, addr = sock.accept()
    print(f"Server has connected to address {addr[0]}") 
    logging.info(f"Server has connected to address {addr[0]}")
    
    name = conn.recv(1024).decode()
    password = conn.recv(1024).decode()
    #print(addr[0], name, password)
    check_user(addr[0], name, password)
    

    while True:
        data = conn.recv(1024).decode()
        if not data or data == "exit":
            break
        print(data)
    print("Connection closed")                                                 
    logging.info("Connection closed") 
    conn.close()

