import socket

def client():
    host = socket.gethostname()  # as both code is running on same pc
    port = 10000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" --> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Depuis le serveur: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__' :
    client()


    '''client_socket = socket.socket()
    client_socket.connect(('localhost', 5000))
    while True :
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        if data == "/":
            client_socket.close()'''