import socket
import time
import threading

def serveur():
    host = socket.gethostname()
    port = 10000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("connexion depuis" + str(address))

    def msg():
        exec = ''
        while exec != 'stop':
            data = input(" --> ")
            conn.send(message.encode())
            time.sleep(0.5)

            if data == 'bye':
                print("deconnexion du client")
                time.sleep(1)
            if data == 'arret':
                print("arrêt du serveur")
                time.sleep(1)
                conn.close()  # fermer la connexion
                exec = 'stop'

    def msgrcv():
        exec = ''
        while exec != 'stop':
            data = conn.recv(1024).decode()
            if data == 'arret':
                print("arrêt du serveur")
                time.sleep(1)
                conn.close()  # fermer la connexion
                exec = 'stop'
            elif data == 'bye':
                print(' le client: ' + data)
                server_socket.listen(2)
                conn, address = server_socket.accept()
                print("connexion depuis" + str(address))
            else:
                print(' le serveur: ' + data)
                print(' --> ')

    t1 = threading.Thread(target=msg)
    t2 = threading.Thread(target=msgrcv)
    t1.start()
    time.sleep(3)
    t2.start()
    t1.join()
    t2.join()
    print("ok")

if __name__ == '__main__' :
    serveur()

