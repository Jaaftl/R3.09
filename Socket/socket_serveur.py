import socket
import time

def serveur():
    host = socket.gethostname()
    port = 10000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print ("connexion depuis" + str(address))

    msg = ''



    while msg != 'arret':
        data = conn.recv(1024).decode()
        if data == 'bye':
            print ('client déconnecté')
            time.sleep(3)
            server_socket.listen(2)
            conn, address = server_socket.accept()
            print("connexion depuis" + str(address))
        elif data != '':
            print("Depuis le client: " + str(data))
            msg = input(' --> ')
            conn.send(msg.encode()) # envoie msg à client
            if msg == 'bye':
                time.sleep(1)
                print ('client déconnecté')
                time.sleep(3)
                server_socket.listen(2)
                conn, address = server_socket.accept()
                print("connexion depuis" + str(address))
    print ("arret du serveur")
    conn.close()  # fermer la connexion


if __name__ == '__main__' :
    serveur()

