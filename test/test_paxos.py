import socket

HOST = '127.0.0.2'
PORT = 40097

p_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
p_socket.bind((HOST,PORT))
p_socket.listen(5)

while True:
    conn,addr= p_socket.accept()
    print("connect by %s" + str(addr))
    data = input("please input the things you want to say")
    conn.send(data.encode("utf-8"))
    recv = conn.recv(1024)
    print(recv)
    pass
p_socket.close()

