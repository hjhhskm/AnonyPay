import socket

HOST = '127.0.0.2'
PORT = 40097

p_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
p_socket.connect((HOST,PORT))

while True:
    recv = p_socket.recv(1024)
    print(recv)
    data = input("please input the things you want to say")
    p_socket.send(data.encode("utf-8"))
    pass

p_socket.close()


