import socket
import getpass
def port_addr_name():
    addr = input("Input addres: ")
    port = int(input("Input port number: "))
    return (addr, port) 

def inp_pass():
    name = input('Input name: ')
    #password =  getpass.getpass(prompt="Input password: ")
    password = input('Input password: ')
    return (name, password)

def send_pass(sock):
    name = input('Input name: ')
    sock.send(name.encode())
    password =  getpass.getpass(prompt="Input password: ")
    #password = input('Input password: ')
    sock.send(password.encode())

def connect_to_server():
    sock = socket.socket()
    sock.connect(port_addr_name())
    send_pass(sock)
    msg = ""
    while True:
        msg = input()
        if msg == "exit":
            break
        sock.send(msg.encode())
    
    sock.close()

if __name__ == "__main__":
    connect_to_server()


