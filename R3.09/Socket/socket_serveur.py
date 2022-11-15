import socket

def serveur():
    host = socket.gethostname()
    port = 10000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Depuis le client: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__' :
    serveur()
    '''server_socket = socket.socket()
    server_socket.bind(('localhost', 5000))
    while True:
        server_socket.listen(1)
        conn, address = server_socket.accept()
        data = conn.recv(1024).decode()
        conn.send(message.encode())
        if data == "/":
            conn.close()'''